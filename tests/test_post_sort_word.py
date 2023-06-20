import unittest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class SortEndpointTestCase(unittest.TestCase):
    def test_sort_words(self):
        payload = {
            "words": ["banana", "apple", "orange", "grape"],
            "order": "asc"
        }
        expected_result = ['banana', 'apple', 'orange', 'grape']
        response = client.post("api/sort", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_result)

    def test_sort_words_reverse(self):
        payload = {
            "words": ["banana", "apple", "orange", "grape"],
            "order": "desc"
        }
        expected_result = ['grape', 'orange', 'apple', 'banana']

        response = client.post("api/sort", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_result)
