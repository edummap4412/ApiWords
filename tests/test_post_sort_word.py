import unittest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class SortEndpointTestCase(unittest.TestCase):
    def test_sort_words(self):
        payload = {
            "words": ["banana", "apple", "orange", "grape"],
            "reverse": False
        }
        expected_result = ["apple", "banana", "grape", "orange"]

        response = client.post("api/sort", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['words'], expected_result)

    def test_sort_words_reverse(self):
        payload = {
            "words": ["banana", "apple", "orange", "grape"],
            "reverse": True
        }
        expected_result = ["orange", "grape", "banana", "apple"]

        response = client.post("api/sort", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_result)
