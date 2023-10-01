from base import Base


class ApiV1(Base):


    def test_liquid_get_not_exist(self):

        with self.app.test_request_context():
            headers={
                "Authorization": f"Bearer {self.token}"
            }

            null_uuid = "00000000-0000-0000-0000-000000000000"
            specific_liq = self.client.get(f"/v1/liquid/{null_uuid}",
                                           headers=headers)
            self.assertEqual(specific_liq.status_code, 404)
            self.assertEqual(specific_liq.json["status"], "error")
            self.assertEqual(specific_liq.json["message"], "Resource not found")
            self.assertEqual(specific_liq.json["url"], None)


    def test_liquid_delete_not_exist(self):

        with self.app.test_request_context():
            headers={
                "Authorization": f"Bearer {self.token}"
            }

            null_uuid = "00000000-0000-0000-0000-000000000000"
            specific_liq = self.client.delete(f"/v1/liquid/{null_uuid}",
                                              headers=headers)
            self.assertEqual(specific_liq.status_code, 404)
            self.assertEqual(specific_liq.json["status"], "error")
            self.assertEqual(specific_liq.json["message"], "Resource not found")
            self.assertEqual(specific_liq.json["url"], None)
