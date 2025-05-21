import logging
import os


# log_dir = os.path.join(os.getcwd(), "logs")
log_dir = '/shared/logs'
os.makedirs(log_dir, exist_ok=True)

log_file = os.path.join(log_dir, "test_db_features.log")

logger = logging.getLogger("test_db_logger")
logger.setLevel(logging.INFO)

if not logger.handlers:
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(logging.Formatter(
        "[%(asctime)s][%(levelname)s]: %(message)s",
        "%Y-%m-%d %H:%M:%S"
    ))

    logger.addHandler(file_handler)
