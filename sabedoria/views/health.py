import json
import uuid
from datetime import datetime

from flask import Blueprint, current_app, request
from flask_httpauth import HTTPTokenAuth

from ..models import health

bp = Blueprint("v1", __name__, url_prefix="/v1")
auth = HTTPTokenAuth(scheme="Bearer")


@auth.verify_token
def verify_token(token):
    """Simplified function to check token"""

    if current_app.config["TOKEN"] == token:
        return True
    return False


@auth.error_handler
def auth_error(status):
    """Custom error catch"""

    return {
        "url": None,
        "status": "error",
        "message": f"Autentication error: {status}"
    }, 401


@bp.route("/health", methods=["GET"])
def health_get():
    """Simple GET return to healthcheck"""
    return "OK"

@bp.route("/health", methods=["HEAD"])
def health_head():
    """Simple HEAD return to healthcheck"""
    return None


@bp.route("/liquid", methods=["GET"])
@auth.login_required
def liquid_get():
    """Get all liquid resources or by date range"""

    # verificar quais filtros podem ser utilizados

    order = health.Liquid.creation_date.asc()
    liquids = health.Liquid().query.order_by(order)

    return [liquid.serialize() for liquid in liquids]


@bp.route("/liquid/today", methods=["GET"])
@auth.login_required
def liquid_get_by_today():
    """Get all entries of liquid that inserted today"""

    now = datetime.utcnow()
    start = datetime(now.year, now.month, now.day, 0, 0, 0)
    end = datetime(now.year, now.month, now.day, 23, 59, 59)

    query_filters = [
        health.Liquid.creation_date > start,
        health.Liquid.creation_date < end
    ]

    liquids = health.Liquid().query.filter(*query_filters)

    return [liquid.serialize() for liquid in liquids]


@bp.route("/liquid/<lq_id>", methods=["GET"])
@auth.login_required
def liquid_get_by_id(lq_id):
    """Get specific liquid resource"""

    try:
        uuid.UUID(lq_id)
    except ValueError:
        return {
                "url": None,
                "status": "error",
                "message": "Invalid UUID"
         }, 404

    liquid = health.Liquid.get(lq_id)

    if liquid is None:
        return {
                "url": None,
                "status": "error",
                "message": "Resource not found"
         }, 404

    return liquid.serialize()


@bp.route("/liquid", methods=["POST"])
@auth.login_required
def liquid_post():
    """Create a new liquid resource"""

    # Aqui precisa saber se precisa de um try catch
    # ou outra forma de detectar errado

    content_type = request.headers.get("Content-Type")
    if content_type == "application/json":
        req_json = request.get_json()

    elif content_type == "text/plain":
        req_json = json.loads(request.data)

    elif content_type == "multipart/form-data":
        req_json = request.form

    if "creation_date" not in req_json:
        req_json["creation_date"] = datetime.utcnow()

    req_json["last_modification"] = datetime.utcnow()

    liquid = health.Liquid(**req_json)
    liquid.save()

    return liquid.serialize(), 200


@bp.route("/liquid/<lq_id>", methods=["DELETE"])
@auth.login_required
def liquid_delete_by_id(lq_id):
    """Delete specific liquid by UUID"""

    try:
        uuid.UUID(lq_id)
    except ValueError:
        return {
                "url": None,
                "status": "error",
                "message": "Invalid UUID"
         }, 404


    liquid = health.Liquid.get(lq_id)

    if liquid is None:
        return {
                "url": None,
                "status": "error",
                "message": "Resource not found"
         }, 404

    liquid.delete()

    return {}, 200
