from functools import cached_property
import shutil
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, TextIO

import loguru
import polars as pl
from loguru import logger
import toml

from scripts import CSV_FILE, DEF_CPP_FILE, DEF_PY_FILE, DEF_RUST_FILE


def rotation_fn(_msg: loguru.Message, file_opened: TextIO) -> bool:
    """Rotation function for logfiles.

    Args:
        _msg (loguru.Message): Message.
        file_opened (TextIO): File object.

    Returns:
        bool: True (should change file) if file is more than a week old or bigger than 2MiB.
    """
    file = Path(file_opened.name)
    # File is more than 1 week old
    is_old = datetime.now().timestamp() - file.stat().st_ctime > 7 * 86400
    # File is >2MiB
    is_big = file.stat().st_size > (2 << 20)  # Multiplies by 1024 instead of 1000
    return is_old or is_big


def format_logger(*, log_file: Path = Path("logs") / "leetcode.log") -> None:
    """Formats a loguru logger, can be called from anywhere to set it up.

    Args:
        log_file (Path, optional): File to store the logs. Defaults to LOG_DIR/"neuro.log".
    Raises:
        ValueError: If verbosity isn't in [0,6].
    """

    # Adds the segment on multiple lines to disable each at will by commenting
    format = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green>"
    format += " | <level>{level:<8}</level>"
    format += " | <level>{message}</level>"

    # Function name is defined separately because it's only used in the logfile to avoid cluttered terminal
    f_name = " | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan>"

    # Resets all previously existing sinks
    logger.remove()

    # Log file
    logger.add(
        log_file,
        format=format + f_name,
        enqueue=True,
        level="DEBUG",
        rotation=rotation_fn,
    )
    logger.info(f"Launched program with command {' '.join(sys.argv)}")

    # Console log
    logger.add(sys.stderr, format=format, level="DEBUG", enqueue=True)


class Problem:
    def __init__(
        self,
        slug: str,
        question_id: int,
        title: str,
        difficulty: str,
        tags: list[str],
        content: str = "",
    ) -> None:
        self.notes: str = ""
        self.languages: list[str] = ["rust", "cpp", "python"]

        self.id = int(question_id)
        self.slug = slug
        self.name = title
        self.difficulty = difficulty
        self.tags = tags

        self.content = content

    @staticmethod
    def from_post(slug: str, data: dict[str, Any]) -> Problem:
        logger.info(f"Parsing problem data for slug {slug}")
        try:
            tags = [tag["name"] for tag in data["topicTags"]]
            problem = Problem(
                slug=slug,
                question_id=data["questionId"],
                title=data["title"],
                difficulty=data["difficulty"],
                tags=tags,
                content=data["content"],
            )
        except KeyError:
            logger.error("Could not parse problem from post data")
            raise KeyError("Could not parse problem from post data")
        except Exception as e:
            logger.error(f"Unexpected error when parsing problem from post data: {e}")
            raise e

        return problem

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "slug": self.slug,
            "name": self.name,
            "difficulty": self.difficulty,
            "tags": ";".join(self.tags),
        }

    @cached_property
    def dir(self) -> Path:
        return Path(f"problems/{self.id:04d}-{self.slug}")

    def update_csv(self) -> None:
        if CSV_FILE.exists():
            data = pl.read_csv(CSV_FILE)
        else:
            data = pl.DataFrame()

        pb_dict = self.to_dict()
        problem_df = pl.DataFrame([pb_dict])

        if data.is_empty():
            data = problem_df
        elif self.id in data["id"].to_list():
            logger.error(f"Problem with id {self.id} already exists in database")
            raise ValueError(f"Problem with id {self.id} already exists in database")
        else:
            data = pl.concat([data, problem_df], how="vertical").unique(subset=["id"])

        data.sort("id").write_csv(CSV_FILE)

    def generate_readme(
        self, description_file: str = "PROBLEM.md", link_file: str = "README.md"
    ) -> None:
        """Generates two readme files, one with extracted info from leetcode that has a license
        that prohibits me to upload it on github, and will only have a link for the description

        Args:
            problem (Problem): Problem object with relevant info
            description_file (str, optional): File with description (must be gitignore). Defaults to "PROBLEM.md".
            link_file (str, optional): File with only the link (can be hidden in editor). Defaults to "README.md".
        """
        readme = f"# {self.id}. {self.name}\n\n"
        readme += f"**Difficulty:** {self.difficulty}<br>\n"
        readme += f"**Tags:** {', '.join(self.tags)}\n\n"
        readme += "## Description\n"
        readme_link_only = readme
        readme += self.content.replace("<pre>", '<pre style="color:#ABB2BF">')
        readme_link_only += f"https://leetcode.com/problems/{self.slug}/"

        with open(self.dir / f"{description_file}", "w") as f:
            f.write(readme)
        with open(self.dir / f"{link_file}", "w") as f:
            f.write(readme_link_only)

    def init_files(self) -> None:
        logger.debug(f"Initializing language files for problem {self.name}")
        N = len(self.languages)
        for i, lang in enumerate(self.languages):
            if lang == "rust":
                logger.debug(f"[{i}/{N}] Initializing Rust files")
                self.init_rust()
            elif lang == "cpp":
                logger.debug(f"[{i}/{N}] Initializing C++ files")
                self.init_cpp()
            elif lang == "python":
                logger.debug(f"[{i}/{N}] Initializing Python files")
                self.init_python()
            else:
                logger.warning(
                    f"Language {lang} not supported, skipping initialization"
                )

    def init_rust(self) -> None:
        shutil.copy(DEF_RUST_FILE, self.dir / "solution.rs")

        cargo_struct = {
            "package": {
                "name": self.slug,
                "version": "0.1.0",
                "edition": "2024",
            },
            "lib": {
                "name": self.slug.replace("-", "_"),
                "path": "solution.rs",
            },
        }
        with open(self.dir / "Cargo.toml", "w") as f:
            toml.dump(cargo_struct, f)

    def init_cpp(self) -> None:
        shutil.copy(DEF_CPP_FILE, self.dir / "solution.cpp")
        target = self.slug
        compiler_flags = "-Wall -Wextra -Wpedantic"

        cmake_content = "cmake_minimum_required(VERSION 3.10)\n"

        cmake_content += f"project({target})\n\n"
        cmake_content += "set(CMAKE_CXX_STANDARD 23)\n\n"

        cmake_content += f"add_executable({target} solution.cpp)\n"
        cmake_content += f"target_compile_options({target} PRIVATE {compiler_flags})\n"

        with open(self.dir / "CMakeLists.txt", "w") as f:
            f.write(cmake_content)

    def init_python(self) -> None:
        shutil.copy(DEF_PY_FILE, self.dir / "solution.py")

    def generate_desktop_file(self) -> None:
        diff = self.difficulty.lower()
        path = Path(".").absolute() / f"data/code-{diff}.svg"

        file_content = "[Desktop Entry]\n"
        file_content += f"Icon={path}\n"
        file_content += "Type=Directory\n"
        file_content += f"Name=LeetCode - {self.id}. {self.name}\n"
        file_content += f"Comment=LeetCode Problem {self.id} - {self.name}\n"

        desktop_file_path = self.dir / ".directory"
        with open(desktop_file_path, "w") as f:
            f.write(file_content)


# string-to-integer-atoi

#         DESKTOP_TEMPLATE = """[Desktop Entry]
# Icon=/home/matt/Programming/LeetCode/data/code-easy.svg
# """
