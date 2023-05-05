from pathlib import Path

log_dir = Path(__file__).parents[1] / "logs"

LOG_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "app": {
            "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "fmt": "[%(asctime)s] [%(process)s] [%(levelname)s] %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S %z",
        },
    },
    "handlers": {
        "std_out_handler": {
            "formatter": "app",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
        "json_lines_handler": {
            "formatter": "app",
            "class": "logging.FileHandler",
            # NOTE: whatever is in 'filename' should be what is mounted in docker-compose
            "filename": f"{log_dir / 'logs.jsonl'}",
            "mode": "a",
        },
    },
    "root": {
        "handlers": ["std_out_handler", "json_lines_handler"],
        "level": "DEBUG",
    },
    "loggers": {
    },
}
