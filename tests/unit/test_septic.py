import json
from ..base_test import BaseTest


class SepticTest(BaseTest):
    def test_get_property(self):
        with self.app as client:
            params = {'address': '43 Valmonte Plaza', 'zipcode': '90274'}
            response = self.app.get(
                '/api/v1/',
                data=json.dumps(params),
                headers={'Content-Type': 'application/json'})
            self.assertEqual(response.status_code, 200)
            self.assertTrue(json.loads(response.data)['has_septic'])

    def test_empty_data(self):
        response = self.app.get('/api/v1/',
                                headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 400)

    def test_no_address(self):
        with self.app as client:
            params = {'address': '43 Valmonte Plaza'}
            response = self.app.get(
                '/api/v1/',
                data=json.dumps(params),
                headers={'Content-Type': 'application/json'})
            self.assertEqual(response.status_code, 422)

    def test_no_zipcode(self):
        with self.app as client:
            params = {'zipcode': '90274'}
            response = self.app.get(
                '/api/v1/',
                data=json.dumps(params),
                headers={'Content-Type': 'application/json'})
            self.assertEqual(response.status_code, 422)
