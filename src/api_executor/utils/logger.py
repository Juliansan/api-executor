import sys
from datetime import datetime
from pathlib import Path

from loguru import logger


def setup_logging(*, debug: bool = False) -> None:
    logger.remove()

    file_level = "DEBUG" if debug else "INFO"

    # Terminal: only show errors/criticals
    logger.add(
        sys.stderr,
        level="ERROR",
        format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | {message}",
    )

    # File: store everything at the chosen verbosity
    log_dir = Path("logs")
    log_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    logger.add(
        str(log_dir / f"app-{timestamp}.log"),
        level=file_level,
        rotation="10 MB",
        retention="30 days",
        compression="zip",
    )
