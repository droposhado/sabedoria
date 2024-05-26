from datetime import date

from sqlalchemy.dialects.postgresql import UUID

from .db import Base, db


class Job(Base):
    """Represent database model job"""

    __tablename__ = "jobs"

    title = db.Column(db.JSON)
    description = db.Column(db.JSON)
    url  = db.Column(db.String)
    location  = db.Column(db.String)
    start = db.Column(db.Date(default=date.today))
    end = db.Column(db.Date(default=date.today))

    employer_id = db.Column(UUID, db.ForeignKey("employer.id"))

    location_type  = db.Column(db.String)
    contract_type  = db.Column(db.String)

    skills = db.Column(db.ARRAY(db.String))


    @staticmethod
    def get(idn):
        """Get a liquid by id"""
        return db.session.get(Job, idn)


    def serialize(self):
        """Serialize model to dict"""
        return super().serialize({
            "title": self.title,
            "description": self.description,
            "url": self.url,
            "location": self.location,
            "start": self.start.isoformat(),
            "end": self.end.isoformat(),
            "employer_id": self.employer_id,
            "location_type": self.location_type,
            "contract_type": self.contract_type,
            "skills": self.skills
        })
