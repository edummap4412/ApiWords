import unittest
from fastapi.testclient import TestClient
from api.app.main import app


class TestSortEndpointTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.client = TestClient(app)

    def test_sort_words(self):
        payload = {
            "words": ["banana", "apple", "orange", "grape"],
            "order": "asc"
        }
        expected_result = ['banana', 'apple', 'orange', 'grape']
        response = self.client.post("api/sort", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_result)

    def test_sort_words_reverse(self):
        payload = {
            "words": ["banana", "apple", "orange", "grape"],
            "order": "desc"
        }
        expected_result = ['grape', 'orange', 'apple', 'banana']

        response = self.client.post("api/sort", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_result)
