import os

from flask import url_for

from base import Base


class ApiV2(Base):


    def test_language_401(self):

        with self.app.test_request_context():
            health = self.client.get(url_for("v2.language_method_get"))
            self.assertEqual(health.status_code, 401)


    def test_lang_get(self):

        with self.app.test_request_context():
            headers={
                "Authorization": f"Bearer {self.token}"
            }

            LANGS = os.getenv("LANGS", "").split(",")
            get_empty = self.client.get(url_for("v2.language_method_get"), headers=headers)
            self.assertEqual(get_empty.status_code, 200)
            self.assertEqual(get_empty.json, LANGS)
