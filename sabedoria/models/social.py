
from .db import Base, db


class Social(Base):
    """Represent database model social"""

    __tablename__ = "socials"

    name = db.Column(db.String, unique=True)
    value = db.Column(db.String)


    @staticmethod
    def get(idn):
        """Get a liquid by id"""
        return db.session.get(Social, idn)


    # def serialize(self):
    #     """Serialize model to dict"""
    #     return super().serialize({
    #         "name": self.name,
    #         "value": self.value
    #     })
