import os
import unittest

import sabedoria


class Base(unittest.TestCase):

    def setUp(self):

        self.app = sabedoria.create_app(config_string="sabedoria.config.TestConfig")
        self.client = self.app.test_client()
        self.token = os.getenv("TOKEN")

        with self.app.app_context():

            sabedoria.models.db.db.drop_all()
            sabedoria.models.db.db.create_all()


    def setDown(self):

        with self.app.app_context():

            sabedoria.models.db.db.drop_all()
