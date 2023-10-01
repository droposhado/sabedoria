from flask import url_for

from base import Base


class StaticRobotsTxt(Base):

    def test_robotstxt_check_if_exists(self):
        with self.app.test_request_context():
            rv = self.client.get(url_for("static", filename="robots.txt"))
            self.assertEqual(rv.status_code, 200)
