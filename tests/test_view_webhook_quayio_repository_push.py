import json
import os

from flask import url_for

from base import Base


class Webhook(Base):


    def test_view_webhook_quayio_repository_push_ok(self):

        test_folder = os.path.dirname(os.path.abspath(__file__))
        data_file = os.path.join(test_folder,
                                 "data/quay.io-repository-push.json")
        self.assertTrue(os.path.exists(data_file))

        with open(data_file, "r") as content:
            data = json.load(content)

        with self.app.test_request_context():

            send = self.client.post(url_for("webhook.quayio_repository_push"),
                                    json=data)
            self.assertEqual(send.status_code, 200)
