from flask import Blueprint, current_app, request

from . import core

bp = Blueprint("webhook", __name__, url_prefix="/webhook")



@bp.route("/", methods=["GET"])
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

