from .db import Base, db


class Employer(Base):
    """Represent database model employer"""

    __tablename__ = "employers"

    name = db.Column(db.String)
    description = db.Column(db.JSON)
    url = db.Column(db.String)
    jobs = db.relationship("Job", backref="employer")


    @staticmethod
    def get(idn):
        """Get a liquid by id"""
        return db.session.get(Employer, idn)


    def serialize(self):
        """Serialize model to dict"""
        return super(Employer, self).serialize({
            "name": self.name,
            "description": self.description,
            "url": self.url,
            "jobs": self.jobs
        })
