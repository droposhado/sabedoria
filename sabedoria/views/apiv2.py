from functools import wraps

from flask import Blueprint, current_app, request
from flask_httpauth import HTTPTokenAuth
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select

from sabedoria import core, models


bp = Blueprint("v2", __name__, url_prefix="/api/v2")
auth = HTTPTokenAuth("Bearer")


@auth.verify_token
def verify_token(token):
    """Simplified function to check token"""
    if current_app.config["TOKEN"] == token:
        return True
    return False


@auth.error_handler
def auth_error(status):
    """Auth customization error"""
    return {
        "url": None,
        "status": "error",
        "message": f"Autentication error ({status})"
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


@bp.route("/health", methods=["GET"])
def health_method_get():
    """Simple GET return to healthcheck"""
    try:
        models.db.db.session.execute(select(1))
        return "OK", 200
    except SQLAlchemyError:
        return "", 500


@bp.route("/", methods=["GET"])
@auth.login_required
@check_language
def index_method_get():
    """Main route with all infos returned"""
    return {}


@bp.route("/social", methods=["GET"])
@auth.login_required
def social_method_get():
    """Returning socials"""

    socials = models.social.Social().query.all()
    res = core.get_social(socials)
    return res


@bp.route("/course", methods=["GET"])
@auth.login_required
def course_method_get():
    """Returning course"""
    return []


@bp.route("/job", methods=["GET"])
@auth.login_required
@check_language
def job_method_get():
    """Returning job"""
    return []


@bp.route("/project", methods=["GET"])
@auth.login_required
@check_language
def project_method_get():
    """Returning project"""
    return []


@bp.route("/education", methods=["GET"])
@auth.login_required
@check_language
def education_method_get():
    """Returning education list"""
    return []


@bp.route("/interest", methods=["GET"])
@auth.login_required
@check_language
def interest_method_get():
    """Returning interest list"""
    return []


@bp.route("/lang", methods=["GET"])
@auth.login_required
def language_method_get():
    """Return list with supported languages"""

    return current_app.config["LANGS"]
