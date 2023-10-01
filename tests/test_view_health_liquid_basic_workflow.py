from flask import url_for

from base import Base


class ApiV1(Base):


    def test_liquid_basic_workflow(self):

        with self.app.test_request_context():
            headers={
                "Authorization": f"Bearer {self.token}"
            }

            get_empty = self.client.get(url_for("v1.liquid_get"), headers=headers)
            self.assertEqual(get_empty.status_code, 200)

            empty_list = []
            self.assertEqual(type(get_empty.json), type(empty_list))
            self.assertEqual(len(get_empty.json), len(empty_list))

            ins_one = self.client.post(url_for("v1.liquid_post"), json={
                "client_name": "tests",
                "client_version": "0.0.1",
                "creation_date": "2023-01-01T01:01:01Z",
                "last_modification": "2023-01-01T01:01:01Z",
                "quantity": 1,
                "unit": "ml",
                "type": "water",
                "username": "hello"
            }, headers=headers)
            self.assertIsNotNone(ins_one.json["id"])

            one_liq = self.client.get(url_for("v1.liquid_get"), headers=headers)
            self.assertEqual(one_liq.status_code, 200)
            self.assertEqual(len(one_liq.json), 1)

            ins_two = self.client.post("/v1/liquid", json={
                "client_name": "tests",
                "client_version": "0.0.2",
                "creation_date": "2023-02-02T02:02:02Z",
                "last_modification": "2023-02-02T02:02:02Z",
                "quantity": 1,
                "unit": "ml",
                "type": "water",
                "username": "hello"
            }, headers=headers)
            self.assertIsNotNone(ins_two.json["id"])

            two_liq = self.client.get(url_for("v1.liquid_get"), headers=headers)
            self.assertEqual(two_liq.status_code, 200)
            self.assertEqual(len(two_liq.json), 2)

            get_all = self.client.get(url_for("v1.liquid_get"), headers=headers)
            self.assertEqual(len(get_all.json), 2)

            self.assertIsNotNone(ins_two.json["id"])
            to_delete_id = str(ins_two.json["id"])
            del_one = self.client.delete(url_for("v1.liquid_delete_by_id",
                                                 lq_id=to_delete_id),
                                         headers=headers)
            self.assertEqual(del_one.status_code, 200)

            getOne = self.client.get(url_for("v1.liquid_get"), headers=headers)
            self.assertEqual(len(getOne.json), 1)
