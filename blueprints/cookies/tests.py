
from flask import Flask
from main import cookies

import unittest


app = Flask(__name__)
app.register_blueprint(cookies)

test_client = app.test_client()


class TestCookies(unittest.TestCase):

    # testing cookie data getting and setting
    def test_cookies(self):

        test_name = "Bill"

        with test_client.post("/name/", data={"name": test_name}) as response:

            self.assertEqual(
                response.status_code,
                200
            )

        with test_client.get("/name/") as response:

            self.assertEqual(
                response.get_data(as_text=True),
                test_name
            )


if __name__ == "__main__":
    unittest.main()
