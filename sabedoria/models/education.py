from datetime import date

from .db import Base, db


class Education(Base):
    """Represent database model education"""

    __tablename__ = "educations"

    university = db.Column(db.String)
    url  = db.Column(db.String)
    location  = db.Column(db.String)
    start = db.Column(db.Date(default=date.today))
    end = db.Column(db.Date(default=date.today))
    title  = db.Column(db.JSON)
    thesis  = db.Column(db.JSON)

    @staticmethod
    def get(idn):
        """Get a liquid by id"""
        return db.session.get(Education, idn)


    def serialize(self):
        """Serialize model to dict"""
        return super(Education, self).serialize({
            "title": self.title,
            "university": self.university,
            "thesis": self.thesis,
            "url": self.url,
            "location": self.location,
            "start": self.start.isoformat(),
            "end": self.end.isoformat()
        })
