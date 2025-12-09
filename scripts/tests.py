from pathlib import Path
import subprocess

from loguru import logger

from scripts.lib import format_logger


def rust_tests() -> None:
    # Run the Rust tests using cargo
    result = subprocess.run(
        ["cargo", "test", "--release", "--all"], text=True, stderr=subprocess.PIPE
    )

    if result.returncode != 0:
        logger.error("Rust tests failed.")
        logger.error("\n" + result.stderr)
        raise RuntimeError("Rust tests failed.")
    else:
        logger.info("Rust tests passed successfully.")


def get_pb_id_and_slug(problem_dir: Path) -> tuple[str, str]:
    """Extracts the problem ID and slug from the problem directory name."""
    dir_name = problem_dir.name
    id, slug = dir_name.split("-", 1)
    id = id.lstrip("0")  # Remove leading zeros
    return id, slug


def cpp_tests(build: bool = False, logger_init: bool = True) -> None:
    if logger_init:
        format_logger(log_file=Path("logs") / "tests.log")
    if build:
        # Build the C++ tests using CMake
        logger.info("Building C++ tests...")
        subprocess.run(["cmake", "-S", ".", "-B", "build"], check=True)
        subprocess.run(["cmake", "--build", "build"], check=True)
    # Run the C++ tests
    logger.info("Running C++ tests...")
    for problem_dir in Path("build/problems").iterdir():
        pb_id, pb_slug = get_pb_id_and_slug(problem_dir)
        executable = problem_dir / f"{pb_slug}"
        path = f"./{executable.absolute().relative_to(Path.cwd())}"
        logger.info(f"Running tests for problem {pb_id}-{pb_slug}...")
        subprocess.run([path], check=True)
    logger.success("All C++ tests passed successfully.")


def python_tests() -> None:
    result = subprocess.run(["pytest"], check=True, text=True, stderr=subprocess.PIPE)

    if result.returncode != 0:
        logger.error("Python tests failed.")
        logger.error("\n" + result.stderr)
        raise RuntimeError("Rust tests failed.")
    else:
        logger.info("Rust tests passed successfully.")


def run_tests() -> None:
    format_logger(log_file=Path("logs") / "tests.log")
    logger.info("Running the tests...")

    logger.info("Running Rust tests...")
    rust_tests()

    logger.info("Running C++ tests...")
    cpp_tests(logger_init=False)

    logger.info("Running Python tests...")
    python_tests()

    logger.success("All tests completed successfully.")
