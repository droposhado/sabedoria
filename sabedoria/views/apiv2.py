from functools import wraps

from flask import Blueprint, current_app, request
from flask_httpauth import HTTPTokenAuth


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


@bp.route("/", methods=["GET"])
@auth.login_required
@check_language
def index():
    """Main route with all infos returned"""
    return {}


@bp.route("/social", methods=["GET"])
@auth.login_required
def social():
    """Returning socials"""
    return {}


@bp.route("/course", methods=["GET"])
@auth.login_required
def course():
    """Returning course"""
    return []


@bp.route("/job", methods=["GET"])
@auth.login_required
@check_language
def job():
    """Returning job"""
    return []


@bp.route("/project", methods=["GET"])
@auth.login_required
@check_language
def project():
    """Returning project"""
    return []


@bp.route("/education", methods=["GET"])
@auth.login_required
@check_language
def education():
    """Returning education list"""
    return []


@bp.route("/interest", methods=["GET"])
@auth.login_required
@check_language
def interest():
    """Returning interest list"""
    return []


@bp.route("/lang", methods=["GET"])
@auth.login_required
def language():
    """Return list with supported languages"""

    return current_app.config["LANGS"]
