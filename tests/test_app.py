import unittest
from unittest.mock import Mock, patch

import requests

from app import app


class NasaApodTests(unittest.TestCase):
    def setUp(self):
        app.config.update(TESTING=True)
        self.client = app.test_client()

    def test_health_routes(self):
        for path in ("/healthz", "/apod/healthz"):
            with self.subTest(path=path):
                response = self.client.get(path)
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.get_json(), {"status": "ok"})

    @patch("app.requests.get")
    def test_apod_routes_render_image(self, get):
        response = Mock()
        response.json.return_value = {
            "date": "2026-08-22",
            "title": "Test Nebula",
            "media_type": "image",
            "url": "https://example.invalid/nebula.jpg",
            "explanation": "A test explanation.",
        }
        get.return_value = response

        for path in ("/", "/apod/"):
            with self.subTest(path=path):
                page = self.client.get(path)
                self.assertEqual(page.status_code, 200)
                self.assertIn("Test Nebula", page.text)
                self.assertIn("/shared-style/portal-theme.css", page.text)

    @patch("app.requests.get", side_effect=requests.RequestException("private detail"))
    def test_api_error_is_safe_for_browser(self, _get):
        page = self.client.get("/apod/")
        self.assertEqual(page.status_code, 200)
        self.assertIn("temporarily unavailable", page.text)
        self.assertNotIn("private detail", page.text)


if __name__ == "__main__":
    unittest.main()
