
from flask import Flask
from main import redirects

import unittest


app = Flask(__name__)
app.register_blueprint(redirects)

test_client = app.test_client()


class TestRedirects(unittest.TestCase):

    # testing redirect
    def test_redirect(self):

        with test_client.get("/redirect/", follow_redirects=True) as response:

            self.assertEqual(
                response.get_data(as_text=True),
                "the default route"
            )


if __name__ == "__main__":
    unittest.main()
