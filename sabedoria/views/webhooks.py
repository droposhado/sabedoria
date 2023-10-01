from flask import Blueprint


bp = Blueprint("webhook", __name__, url_prefix="/webhook")


@bp.route("/quayio/repository-push", methods=["POST"])
def quayio_repository_push():
    """Receives respository push event from quay.io"""

    return "OK"
