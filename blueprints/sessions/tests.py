
from flask import Flask
from main import sessions
from config import secret_key

import unittest


app = Flask(__name__)
app.secret_key = secret_key
app.register_blueprint(sessions)

test_client = app.test_client()


class TestSessions(unittest.TestCase):

    def test_sessions(self):

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
