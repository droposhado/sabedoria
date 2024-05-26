
from .db import Base, db


class Platform(Base):
    """Represent database model platform"""

    __tablename__ = "platforms"

    name = db.Column(db.String)
    url = db.Column(db.String)
    courses = db.relationship("Course", backref="platform")


    @staticmethod
    def get(idn):
        """Get a liquid by id"""
        return db.session.get(Platform, idn)


    def serialize(self):
        """Serialize model to dict"""
        return super(self.__class__, self).serialize({
            "name": self.name,
            "url": self.url,
            "courses": self.courses
        })
