from .db import Base, db


class Interest(Base):
    """Represent database model interest"""

    __tablename__ = "interests"

    text = db.Column(db.JSON)

    @staticmethod
    def get(idn):
        """Get a liquid by id"""
        return db.session.get(Interest, idn)


    def serialize(self):
        """Serialize model to dict"""
        return super(self.__class__, self).serialize({
            "text": self.title
        })