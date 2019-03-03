
from flask import Flask
from main import errors

import unittest


app = Flask(__name__)
app.register_blueprint(errors)

test_client = app.test_client()


class TestErrors(unittest.TestCase):

    # testing error 404
    def test_404(self):

        with test_client.get("/404/") as response:

            self.assertEqual(
                response.status_code,
                404
            )

    # testing error 404 with a custom template
    def test_404_custom(self):

        with test_client.get("/404/custom/") as response:

            self.assertEqual(
                response.status_code,
                404
            )

            self.assertEqual(
                response.get_data(as_text=True),
                "<h1>the custom error template</h1>"
            )

    # testing error 500
    def test_500(self):

        with test_client.get("/500/") as response:

            self.assertEqual(
                response.status_code,
                500
            )


if __name__ == "__main__":
    unittest.main()