
from flask import Flask
from main import rendering

import json
import unittest


app = Flask(__name__)
app.register_blueprint(rendering)

test_client = app.test_client()


class TestRendering(unittest.TestCase):

    # string rendering testing
    def test_string_rendering(self):

        with test_client.get("/string/") as response:

            self.assertEqual(
                response.status_code,
                200
            )

            self.assertEqual(
                response.get_data(as_text=True),
                "<h1>Hello, world!</h1>"
            )

    # template string rendering testing
    def test_template_string_rendering(self):

        with test_client.get("/template/string/") as response:

            self.assertEqual(
                response.status_code,
                200
            )

            self.assertEqual(
                response.get_data(as_text=True),
                "&lt;h1&gt;Hello, world!&lt;/h1&gt;"
            )

    # template rendering with escaped data testing
    def test_template_escaped_rendering(self):

        with test_client.get("/template/escaped/") as response:

            self.assertEqual(
                response.status_code,
                200
            )

            self.assertIn(
                "&lt;h1&gt;Hello, world!&lt;/h1&gt;",
                response.get_data(as_text=True)
            )

    # template rendering with unescaped data testing
    def test_template_unescaped_rendering(self):

        with test_client.get("/template/unescaped/") as response:

            self.assertEqual(
                response.status_code,
                200
            )

            self.assertIn(
                "<h1>Hello, world!</h1>",
                response.get_data(as_text=True)
            )

    # json rendering testing
    def test_json_rendering(self):

        with test_client.get("/json/") as response:

            self.assertEqual(
                response.status_code,
                200
            )

            self.assertEqual(
                json.loads(response.get_data(as_text=True)),
                {
                    "text": "<h1>Hello, world!</h1>"
                }
            )


if __name__ == "__main__":
    unittest.main()
