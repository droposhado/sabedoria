from sqlalchemy import text
from sqlalchemy.dialects.postgresql import UUID

from db import db


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
