from functools import wraps

from flask import Blueprint, current_app, request
from flask_httpauth import HTTPTokenAuth

from . import core

bp = Blueprint("infos", __name__, url_prefix="/v1")
auth = HTTPTokenAuth("Bearer")


@auth.verify_token
def verify_token(token):
    """Simplified function to check token"""
    if current_app.config["TOKEN"] == token:
        return True
    return False


@auth.error_handler
def auth_error(status):
   return {
       "url": None,
       "status": "error",
       "message": "Autentication error"
   }, 401


def check_language(func):
    """Reusable function to check if language is supported"""

    @wraps(func)
    def wrapped(*args, **kwargs):
        lang = request.headers.get("Accept-Language")

        if lang is None:
            return {
                "url": "/v1/lang",
                "status": "error",
                "message": "Please send Accept-Language header"
            }, 406

        if lang not in current_app.config["LANGS"]:
            return {
                "url": "/v1/lang",
                "status": "error",
                "message": "Informed language is not supported"
            }, 406

        return func(*args, **kwargs)
    return wrapped


@bp.route("/", methods=["GET"])
@auth.login_required
@check_language
def index():
    """Main route with all infos returned"""

    lang = request.headers.get("Accept-Language")

    br_token = current_app.config["BASEROW_TOKEN"]
    br_url = current_app.config["BASEROW_URL"]

    name = current_app.config["NAME"]

    cfg = current_app.config

    socials = core.get_socials(current_app.config)

    descriptions = core.get_descriptions(br_url, br_token,
                                         cfg["DESCRIPTION_TABLE_ID"], lang)

    courses = core.get_courses(br_url, br_token, cfg["COURSE_TABLE_ID"])

    jobs = core.get_jobs(br_url, br_token, cfg["JOB_TABLE_ID"], lang)

    projects = core.get_projects(br_url, br_token, cfg["PROJECT_TABLE_ID"], lang)

    educations = core.get_educations(br_url, br_token, cfg["EDUCATION_TABLE_ID"], lang)

    interests = core.get_interests(br_url, br_token, cfg["INTEREST_TABLE_ID"], lang)

    res = {
        "name": name,
        "socials": socials,
        "descriptions": descriptions,
        "interests": interests,
        "courses": courses,
        "educations": educations,
        "jobs": jobs,
        "projects": projects
    }

    return res


@bp.route("/social", methods=["GET"])
@auth.login_required
def social():
    """Returning socials"""

    res = core.get_socials(current_app.config)

    return res


@bp.route("/course", methods=["GET"])
@auth.login_required
def course():
    """Returning course from baserow"""

    br_token = current_app.config["BASEROW_TOKEN"]
    br_url = current_app.config["BASEROW_URL"]
    courses_table_id = current_app.config["COURSE_TABLE_ID"]

    res = core.get_courses(br_url, br_token, courses_table_id)

    return res


@bp.route("/job", methods=["GET"])
@auth.login_required
@check_language
def job():
    """Returning job from baserow"""

    lang = request.headers.get("Accept-Language")
    br_token = current_app.config["BASEROW_TOKEN"]
    br_url = current_app.config["BASEROW_URL"]
    jobs_table_id = current_app.config["JOB_TABLE_ID"]

    res = core.get_jobs(br_url, br_token, jobs_table_id, lang)

    return res


@bp.route("/project", methods=["GET"])
@auth.login_required
@check_language
def project():
    """Returning project from baserow"""

    lang = request.headers.get("Accept-Language")
    br_token = current_app.config["BASEROW_TOKEN"]
    br_url = current_app.config["BASEROW_URL"]
    projects_table_id = current_app.config["PROJECT_TABLE_ID"]

    res = core.get_projects(br_url, br_token, projects_table_id, lang)

    return res


@bp.route("/education", methods=["GET"])
@auth.login_required
@check_language
def education():
    """Returning education list from baserow"""

    lang = request.headers.get("Accept-Language")
    br_token = current_app.config["BASEROW_TOKEN"]
    br_url = current_app.config["BASEROW_URL"]
    educations_table_id = current_app.config["EDUCATION_TABLE_ID"]

    res = core.get_educations(br_url, br_token, educations_table_id, lang)

    return res


@bp.route("/interest", methods=["GET"])
@auth.login_required
@check_language
def interest():
    """Returning interest list from baserow"""

    lang = request.headers.get("Accept-Language")
    br_token = current_app.config["BASEROW_TOKEN"]
    br_url = current_app.config["BASEROW_URL"]
    interests_table_id = current_app.config["INTEREST_TABLE_ID"]

    res = core.get_interests(br_url, br_token, interests_table_id, lang)

    return res


@bp.route("/lang", methods=["GET"])
@auth.login_required
def language():
    """Return list with supported languages"""

    return current_app.config["LANGS"]
