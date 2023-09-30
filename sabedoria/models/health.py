from sqlalchemy import text
from sqlalchemy.dialects.postgresql import UUID

from .db import db, Base


class Liquid(Base):
    """Represent database model liquid"""

    __tablename__ = "liquids"

    client_name = db.Column(db.String)
    client_version = db.Column(db.String)
    creation_date = db.Column(db.DateTime)
    last_modification = db.Column(db.DateTime)
    quantity = db.Column(db.Integer)
    unit = db.Column(db.String)
    type = db.Column(db.String)
    username = db.Column(db.String)


    @staticmethod
    def get(idn):
        """Get a liquid by id"""
        return db.session.get(Liquid, idn)


    def serialize(self):
        """Serialize model to dict"""
        return {
            "id": self.id,
            "client_name": self.client_name,
            "client_version": self.client_version,
            "creation_date": self.creation_date.isoformat(),
            "last_modification": self.last_modification.isoformat(),
            "quantity": self.quantity,
            "unit": self.unit,
            "type": self.type,
            "username": self.username
        }
