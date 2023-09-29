from flask import url_for

from base import Base


class Family400(Base):

    def test_401(self):

        with self.app.test_request_context():
            response = self.client.get(url_for("v1.liquid_get"))
            self.assertEqual(response.status_code, 401)
