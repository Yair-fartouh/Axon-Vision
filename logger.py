import logging
import os
from logging.handlers import RotatingFileHandler


class Logger:
    _initialized = False
    _LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
    _LOG_NAME = "log.log"
    _DEFAULT_LOG_LEVEL = logging.INFO

    @staticmethod
    def get_logger(name: str, log_name: str = _LOG_NAME) -> logging.Logger:
        if not Logger._initialized:
            os.makedirs(Logger._LOG_DIR, exist_ok=True)
            log_path = os.path.join(Logger._LOG_DIR, log_name)

            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S"
            )

            # (Rotating File Handler)
            file_handler = RotatingFileHandler(
                log_path,
                maxBytes=2 * 1024 * 1024,  # 2 MB
                backupCount=10,  # Keep 10 backup files.
                encoding="utf-8"
            )
            file_handler.setFormatter(formatter)
            file_handler.setLevel(logging.DEBUG)

            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(formatter)
            stream_handler.setLevel(Logger._DEFAULT_LOG_LEVEL)

            logging.basicConfig(
                level=logging.DEBUG,
                handlers=[file_handler, stream_handler]
            )

            Logger._initialized = True

        return logging.getLogger(name)
