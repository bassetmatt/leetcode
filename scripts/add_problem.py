import os

import click
from loguru import logger


from scripts.leetcode_api import fetch_problem
from scripts.lib import format_logger


@click.command("add_problem", help="Add a new problem to the database")
@click.option(
    "-s",
    "--slug",
    required=True,
    type=str,
    help="name of the problem, lowercase with hyphens",
)
def add_problem(slug: str) -> None:
    format_logger()
    logger.info(f"Adding problem with slug: {slug}")
    problem = fetch_problem(slug)

    os.makedirs(problem.dir, exist_ok=True)

    # Initialize language files
    problem.init_files()

    # Testcases and README
    open(problem.dir / "testcases.txt", "w").close()
    logger.info("Generating README files...")
    problem.generate_readme()

    # Update JSON database
    logger.info("Updating problems database...")
    problem.update_csv()

    # Generate Desktop Entry for directory
    logger.info("Generating Desktop Entry...")
    problem.generate_desktop_file()
