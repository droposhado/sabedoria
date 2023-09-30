import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()

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
