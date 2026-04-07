from pathlib import Path

import mysql.connector


def _cargar_env():
    env_path = Path(__file__).resolve().parent.parent / ".env"
    config = {}

    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        config[key.strip()] = value.strip()

    return config


def get_env_config():
    return _cargar_env()


def get_db_connection():
    config = _cargar_env()
    return mysql.connector.connect(
        host=config.get("server"),
        port=int(config.get("port", 3306)),
        database=config.get("database"),
        user=config.get("user"),
        password=config.get("password"),
    )
