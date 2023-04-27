import logging
import os


class Config():
    BASEROW_TOKEN = os.getenv("BASEROW_TOKEN")
    BASEROW_URL = os.getenv("BASEROW_URL")
    DEBUG = bool(os.getenv("DEBUG", False))
    LANGS = os.getenv("LANGS").split(",")
    LOG_LEVEL = logging.INFO
    TESTING = bool(os.getenv("TESTING", False))
    TOKEN = os.getenv("TOKEN")

    COURSE_TABLE_ID = os.getenv("COURSE_TABLE_ID")
    JOB_TABLE_ID = os.getenv("JOB_TABLE_ID")
    PROJECT_TABLE_ID = os.getenv("PROJECT_TABLE_ID")
    EDUCATION_TABLE_ID = os.getenv("EDUCATION_TABLE_ID")
    INTEREST_TABLE_ID = os.getenv("INTEREST_TABLE_ID")
    DESCRIPTION_TABLE_ID = os.getenv("DESCRIPTION_TABLE_ID")

    NAME = os.getenv("NAME")
    GITHUB = os.getenv("GITHUB")
    LINKEDIN = os.getenv("LINKEDIN")
    EMAIL = os.getenv("EMAIL")
    SITE = os.getenv("SITE")


class DevConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass
