from base import Base
from flask import url_for


class ApiV1(Base):


    def test_health_get(self):

        with self.app.test_request_context():
            health = self.client.get(url_for("v2.health_method_get"))
            self.assertEqual(health.status_code, 200)
            self.assertEqual(health.text, "OK")


    def test_health_head(self):

        with self.app.test_request_context():
            health = self.client.head(url_for("v2.health_method_head"))
            self.assertEqual(health.status_code, 200)
            self.assertEqual(health.text, "")
