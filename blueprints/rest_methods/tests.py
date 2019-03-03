
from flask import Flask
from main import rest_methods

import json
import unittest


app = Flask(__name__)
app.register_blueprint(rest_methods)

test_client = app.test_client()


class TestRESTMethods(unittest.TestCase):

    # testing a get request
    def test_get_method(self):

        with test_client.get("/one/") as response:

            self.assertEqual(
                json.loads(response.get_data(as_text=True)),
                {
                    "request_method": "GET",
                    "request_variables": {
                        "id": "one"
                    },
                    "request_args": {

                    },
                    "request_data": {

                    }
                }
            )

    # testing a post request
    def test_post_method(self):

        with test_client.post(
            "/one/",
            data={
                "arg1": "apple",
                "arg2": "pear"
            }
        ) as response:

            self.assertEqual(
                json.loads(response.get_data(as_text=True)),
                {
                    "request_method": "POST",
                    "request_variables": {
                        "id": "one"
                    },
                    "request_args": {

                    },
                    "request_data": {
                        "arg1": "apple",
                        "arg2": "pear"
                    }
                }
            )

    # testing a put request
    def test_put_method(self):

        with test_client.put(
            "/one/",
            data={
                "arg1": "apple",
                "arg2": "pear"
            }
        ) as response:

            self.assertEqual(
                json.loads(response.get_data(as_text=True)),
                {
                    "request_method": "PUT",
                    "request_variables": {
                        "id": "one"
                    },
                    "request_args": {

                    },
                    "request_data": {
                        "arg1": "apple",
                        "arg2": "pear"
                    }
                }
            )

    # testing a delete request
    def test_delete_method(self):

        with test_client.delete(
            "/one/",
            data={
                "arg1": "apple",
                "arg2": "pear"
            }
        ) as response:

            self.assertEqual(
                json.loads(response.get_data(as_text=True)),
                {
                    "request_method": "DELETE",
                    "request_variables": {
                        "id": "one"
                    },
                    "request_args": {

                    },
                    "request_data": {
                        "arg1": "apple",
                        "arg2": "pear"
                    }
                }
            )


if __name__ == "__main__":
    unittest.main()
