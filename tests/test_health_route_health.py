from flask import url_for

from base import Base


class Health(Base):


    def test_health_get(self):

        with self.app.test_request_context():
            health = self.client.get(url_for("v1.health_get"))
            self.assertEqual(health.status_code, 200)
            self.assertEqual(health.text, "OK")


    def test_health_head(self):

        with self.app.test_request_context():
            health = self.client.head(url_for("v1.health_head"))
            self.assertEqual(health.status_code, 200)
            self.assertEqual(health.text, "")
