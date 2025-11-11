from pathlib import Path
import subprocess

from loguru import logger

from scripts.lib import format_logger


def rust_tests() -> None:
    # Run the Rust tests using cargo
    result = subprocess.run(["cargo", "test"], capture_output=True, text=True)

    # Print the output of the tests
    # print(result.stdout)
    if result.returncode != 0:
        logger.error("Rust tests failed.")
        logger.error(result.stdout)
        raise RuntimeError("Rust tests failed.")
    else:
        logger.info("Rust tests passed successfully.")


def run_tests() -> None:
    format_logger(log_file=Path("logs") / "tests.log")
    logger.info("Running the tests...")

    logger.info("Running Rust tests...")
    rust_tests()

    logger.success("All tests completed successfully.")
