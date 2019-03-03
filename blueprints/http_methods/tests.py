
from flask import Flask
from main import http_methods

import json
import unittest


app = Flask(__name__)
app.register_blueprint(http_methods)

test_client = app.test_client()


class TestHTTPMethods(unittest.TestCase):

    # testing a get request
    def test_get_method(self):

        with test_client.get("/?arg1=apple&arg2=pear") as response:

            self.assertEqual(
                json.loads(
                    response.get_data(as_text=True)
                ),
                {
                    "request_method": "GET",
                    "request_variables": {

                    },
                    "request_args": {
                        "arg1": "apple",
                        "arg2": "pear"
                    },
                    "request_data": {

                    }
                }
            )

    # testing a post request
    def test_post_method(self):

        with test_client.post(
            "/?arg1=apple&arg2=pear",
            data={
                "data_piece1": "grass",
                "data_piece2": "dirt"
            }
        ) as response:

            self.assertEqual(
                json.loads(
                    response.get_data(as_text=True)
                ),
                {
                    "request_method": "POST",
                    "request_variables": {

                    },
                    "request_args": {
                        "arg1": "apple",
                        "arg2": "pear"
                    },
                    "request_data": {
                        "data_piece1": "grass",
                        "data_piece2": "dirt"
                    }
                }
            )


if __name__ == "__main__":
    unittest.main()
