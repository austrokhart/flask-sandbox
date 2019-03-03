
from flask import Flask
from main import routing

import unittest


app = Flask(__name__)
app.register_blueprint(routing)

test_client = app.test_client()


class TestRouting(unittest.TestCase):

    # testing a default route
    def test_default_route(self):

        with test_client.get("/") as response:

            self.assertEqual(
                response.get_data(as_text=True),
                "the default route"
            )

    # testing a sub route
    def test_sub_route(self):

        with test_client.get("/sub/route/") as response:

            self.assertEqual(
                response.get_data(as_text=True),
                "the sub route"
            )

    # testing of getting a path of a route from another one
    def test_from_one_route_to_other_route(self):

        with test_client.get("/from/one/route/to/other/route/") as response:

            self.assertEqual(
                response.get_data(as_text=True),
                "/sub/route/"
            )


if __name__ == "__main__":
    unittest.main()
