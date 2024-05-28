from .db import Base, db


class Project(Base):
    """Represent database model project"""

    __tablename__ = "projects"

    name = db.Column(db.String)
    slug = db.Column(db.String)
    internal_code = db.Column(db.String)
    site_url = db.Column(db.String)
    repo_url = db.Column(db.String)
    archived = db.Column(db.Boolean)
    pinned = db.Column(db.Boolean)
    private = db.Column(db.Boolean)
    description = db.Column(db.JSON)
    skills = db.Column(db.ARRAY(db.String))


    @staticmethod
    def get(idn):
        """Get a liquid by id"""
        return db.session.get(Project, idn)


    # def serialize(self):
    #     """Serialize model to dict"""
    #     return super().serialize({
    #         "name": self.name,
    #         "slug": self.slug,
    #         "internal_code": self.internal_code,
    #         "site_url": self.site_url,
    #         "repo_url": self.repo_url,
    #         "archived": self.archived,
    #         "pinned": self.pinned,
    #         "private": self.private,
    #         "description": self.description,
    #         "skills": self.skills
    #     })
