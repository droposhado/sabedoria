from datetime import datetime

from flask import url_for

from base import Base


class ApiV1(Base):


    def test_liquid_route_today(self):

        with self.app.test_request_context():
            headers={
                "Authorization": f"Bearer {self.token}"
            }

            get_empty = self.client.get(url_for("v1.liquid_get"),
                                        headers=headers)
            self.assertEqual(get_empty.status_code, 200)

            empty_list = []
            self.assertEqual(type(get_empty.json), type(empty_list))
            self.assertEqual(len(get_empty.json), len(empty_list))

            now = datetime.utcnow().isoformat()
            ins_one = self.client.post(url_for("v1.liquid_post"), json={
                "client_name": "tests",
                "client_version": "0.0.1",
                "creation_date": now,
                "last_modification": now,
                "quantity": 1,
                "unit": "ml",
                "type": "water",
                "username": "hello"
            }, headers=headers)
            self.assertIsNotNone(ins_one.json["id"])

            one_liq = self.client.get(url_for("v1.liquid_get"),
                                      headers=headers)
            self.assertEqual(one_liq.status_code, 200)
            self.assertEqual(len(one_liq.json), 1)

            old_date = datetime(2020, 1, 1, 1, 1, 1)
            ins_two = self.client.post(url_for("v1.liquid_post"), json={
                "client_name": "tests",
                "client_version": "0.0.2",
                "creation_date": old_date.isoformat(),
                "last_modification":  old_date.isoformat(),
                "quantity": 1,
                "unit": "ml",
                "type": "water",
                "username": "hello"
            }, headers=headers)
            self.assertIsNotNone(ins_two.json["id"])

            today_liqs = self.client.get(url_for("v1.liquid_get_by_today"),
                                         headers=headers)
            self.assertEqual(today_liqs.status_code, 200)
            self.assertEqual(len(today_liqs.json), 1)
