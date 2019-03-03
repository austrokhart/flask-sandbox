
from flask import Flask, url_for
from main import static_files

import unittest


app = Flask(__name__)
app.register_blueprint(static_files)

test_client = app.test_client()


class TestStaticFiles(unittest.TestCase):

    # testing access to static files
    def test_static_files(self):

        # ResourceWarning: unclosed file... if don't use "with" construction

        with test_client.get("/static/style.css") as response:

            self.assertEqual(
                response.status_code,
                200
            )

        with test_client.get("/static/script.js") as response:

            self.assertEqual(
                response.status_code,
                200
            )

        with test_client.get("/static/doesnt.exist") as response:

            self.assertEqual(
                response.status_code,
                404
            )


if __name__ == "__main__":
    unittest.main()
