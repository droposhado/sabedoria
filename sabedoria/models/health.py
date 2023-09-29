from sqlalchemy import text
from sqlalchemy.dialects.postgresql import UUID

from .db import db


class Base(db.Model):
    """Base class with common methods"""

    __abstract__ = True

    id = db.Column(UUID(as_uuid=True),
                primary_key=True,
                unique=True,
                server_default=text("gen_random_uuid()"),)


    def save(self):
        """Create new item"""

        # But need save to update, but exists
        if not self.id:
            db.session.add(self)
        db.session.commit()
        db.session.flush()


    def delete(self):
        """Delete item"""

        db.session.delete(self)
        db.session.commit()


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

