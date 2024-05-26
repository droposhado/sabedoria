from datetime import date

from sqlalchemy.dialects.postgresql import UUID

from .db import Base, db


class Course(Base):
    """Represent database model course"""

    __tablename__ = "courses"

    title = db.Column(db.String)
    minutes = db.Column(db.String)
    end = db.Column(db.Date(default=date.today))
    status = db.Column(db.String)
    private = db.Column(db.Boolean)
    platform_id = db.Column(UUID, db.ForeignKey("platform.id"))
    skills = db.Column(db.ARRAY(db.String))

    # dont need separated table, because only used in 1 certicate
    certificate_url  = db.Column(db.String)
    certificate_credential  = db.Column(db.String)
    certificate_download_url  = db.Column(db.String)


    @staticmethod
    def get(idn):
        """Get a liquid by id"""
        return db.session.get(Course, idn)


    def serialize(self):
        """Serialize model to dict"""
        return super().serialize({
            "title": self.title,
            "minutes": self.minutes,
            "end": self.end.isoformat(),
            "status": self.status,
            "private": self.private,
            "platform_id": self.platform_id,
            "skills": self.skills,
            "certificate_url": self.certificate_url,
            "certificate_credential": self.certificate_credential,
            "certificate_download_url": self.certificate_download_url
        })
