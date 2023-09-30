from flask import Blueprint


bp = Blueprint("webhook", __name__, url_prefix="/webhook")


@bp.route("/", methods=["GET"])
def index():
    """Main route with all infos returned"""

    return "OK"
