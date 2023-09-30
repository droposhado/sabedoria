from sqlalchemy import text
from sqlalchemy.dialects.postgresql import UUID

from .db import db, Base


class Language(Base):
    """Represent database model language"""

    __tablename__ = "languages"

    name = db.Column(db.String)
    code = db.Column(db.String)

    @staticmethod
    def get(idn):
        """Get a liquid by id"""
        return db.session.get(Language, idn)


    def serialize(self):
        """Serialize model to dict"""
        return {
            "id": self.id,
            "name": self.name,
            "code": self.code
        }
