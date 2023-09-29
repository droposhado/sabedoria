import os
import unittest

from sabedoria.models.db import db


class Base(unittest.TestCase):

    def setUp(self):

        self.app = sabedoria.create_app(config_string="sabedoria.config.TestConfig")
        self.client = self.app.test_client()
        self.token = os.getenv("TOKEN")

        with self.app.app_context():

            db.drop_all()
            db.create_all()


    def setDown(self):

        with self.app.app_context():

            db.drop_all()
