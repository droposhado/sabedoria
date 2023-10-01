import json
import os

from flask import url_for

from base import Base


class Webhook(Base):


    def test_view_webhook_quayio_repository_push_ok(self):

        data_file = "data/quay.io-repository-push.json"
        self.assertTrue(os.path.exists(data_file))
        data = json.loads(data_file)

        with self.app.test_request_context():

            send = self.client.post(url_for("webhook.quayio_repository_push"),
                                    json=data)
            self.assertEqual(send.status_code, 200)
