import unittest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class VowelCountEndpointTestCase(unittest.TestCase):
    def test_count_vowels(self):
        payload = {
            "words": ["banana", "apple", "orange", "grape"]
        }
        expected_result = {
            "banana": 3,
            "apple": 2,
            "orange": 3,
            "grape": 2
        }

        response = client.post("api/vowel_count", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_result)
