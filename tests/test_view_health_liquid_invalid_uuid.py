from flask import url_for

from base import Base


class ApiV1(Base):


    def test_liquid_get_invalid_uuid(self):

        with self.app.test_request_context():
            headers={
                "Authorization": f"Bearer {self.token}"
            }

            null_uuid = "00000000-not-exist-000000000000"
            specific_liq = self.client.get(url_for("v1.liquid_get_by_id",
                                                   lq_id=null_uuid),
                                           headers=headers)
            self.assertEqual(specific_liq.status_code, 404)
            self.assertEqual(specific_liq.json["status"], "error")
            self.assertEqual(specific_liq.json["message"], "Invalid UUID")
            self.assertEqual(specific_liq.json["url"], None)


    def test_liquid_delete_invalid_uuid(self):

        with self.app.test_request_context():
            headers={
                "Authorization": f"Bearer {self.token}"
            }

            null_uuid = "00000000-not-exist-000000000000"
            specific_liq = self.client.delete(url_for("v1.liquid_delete_by_id",
                                                      lq_id=null_uuid),
                                              headers=headers)
            self.assertEqual(specific_liq.status_code, 404)
            self.assertEqual(specific_liq.json["status"], "error")
            self.assertEqual(specific_liq.json["message"], "Invalid UUID")
            self.assertEqual(specific_liq.json["url"], None)
