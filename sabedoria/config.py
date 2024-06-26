import logging
import os


class Config():

    db_url = "postgresql://sabedoria:sabedoria@localhost:5432/sabedoria"

    DEBUG = bool(os.getenv("DEBUG", False))
    LOG_LEVEL = logging.INFO
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", db_url)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    LANGS = os.getenv("LANGS", "").split(",")
    TESTING = bool(os.getenv("TESTING", False))
    TOKEN = os.getenv("TOKEN")


class TestConfig(Config):
    DEBUG = True
    TESTING = True


class DevConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass
