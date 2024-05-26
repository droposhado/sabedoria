# from datetime import datetime

import flask_sqlalchemy
from sqlalchemy import text
from sqlalchemy.dialects.postgresql import UUID

db = flask_sqlalchemy.SQLAlchemy()


class Base(db.Model):
    """Base class with common methods"""

    __abstract__ = True

    id = db.Column(UUID(as_uuid=True),
                primary_key=True,
                unique=True,
                server_default=text("gen_random_uuid()"),)
    creation_date = db.Column(db.DateTime)
    last_modification = db.Column(db.DateTime)


    def save(self):
        """Create new item"""

        # But need save to update, but exists
        if not self.id:
            db.session.add(self)
        # self.last_modification = datetime.utcnow()
        db.session.commit()
        db.session.flush()


    def delete(self):
        """Delete item"""

        db.session.delete(self)
        db.session.commit()


    def serialize(self, obj):
        """Serialize base model to dict"""
        return obj.update({
            "id": self.id,
            "creation_date": self.creation_date.isoformat(),
            "last_modification": self.last_modification.isoformat()
        })
