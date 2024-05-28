from base import Base
from flask import url_for


class ApiV2(Base):


    def test_social_401(self):

        with self.app.test_request_context():
            health = self.client.get(url_for("v2.social_method_get"))
            self.assertEqual(health.status_code, 401)


    def test_social_get(self):

        with self.app.test_request_context():
            headers={
                "Authorization": f"Bearer {self.token}"
            }

            get_empty = self.client.get(url_for("v2.social_method_get"),
                                        headers=headers)
            self.assertEqual(get_empty.status_code, 200)
            self.assertEqual(get_empty.json, {})
