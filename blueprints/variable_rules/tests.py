
from flask import Flask
from main import variable_rules

import unittest


app = Flask(__name__)
app.register_blueprint(variable_rules)

test_client = app.test_client()


class TestVariableRules(unittest.TestCase):

    # testing a default type (string)
    def test_default_type(self):

        with test_client.get("/") as response:

            self.assertEqual(
                response.status_code,
                404
            )

        with test_client.get("/12345/") as response:

            self.assertEqual(
                response.get_data(as_text=True),
                "12345"
            )

        with test_client.get("/12345.678/") as response:

            self.assertEqual(
                response.get_data(as_text=True),
                "12345.678"
            )

        with test_client.get("/apple/") as response:

            self.assertEqual(
                response.get_data(as_text=True),
                "apple"
            )

        with test_client.get("/apple/pear/") as response:

            self.assertEqual(
                response.status_code,
                404
            )

    # testing an integer type
    def test_integer_type(self):

        with test_client.get("/integer/") as response:

            # this is strange, but the endpoint name is returned
            self.assertEqual(
                response.get_data(as_text=True),
                "integer"
            )

        with test_client.get("/integer/12345/") as response:

            self.assertEqual(
                response.get_data(as_text=True),
                "12345"
            )

        with test_client.get("/integer/12345.678/") as response:

            self.assertEqual(
                response.status_code,
                404
            )

        with test_client.get("/integer/apple/") as response:

            self.assertEqual(
                response.status_code,
                404
            )

        with test_client.get("/integer/apple/pear/") as response:

            self.assertEqual(
                response.status_code,
                404
            )

    # testing a float type
    def test_float_type(self):

        with test_client.get("/float/") as response:

            self.assertEqual(
                response.get_data(as_text=True),
                "float"
            )

        with test_client.get("/float/12345/") as response:

            self.assertEqual(
                response.status_code,
                404
            )

        with test_client.get("/float/12345.678/") as response:

            self.assertEqual(
                response.get_data(as_text=True),
                "12345.678"
            )

        with test_client.get("/float/apple/") as response:

            self.assertEqual(
                response.status_code,
                404
            )

        with test_client.get("/float/apple/pear/") as response:

            self.assertEqual(
                response.status_code,
                404
            )

    # testing a path type
    def test_path_type(self):

        with test_client.get("/path/") as response:

            self.assertEqual(
                response.get_data(as_text=True),
                "path"
            )

        with test_client.get("/path/12345/") as response:

            self.assertEqual(
                response.get_data(as_text=True),
                "12345"
            )

        with test_client.get("/path/12345.678/") as response:

            self.assertEqual(
                response.get_data(as_text=True),
                "12345.678"
            )

        with test_client.get("/path/apple/") as response:

            self.assertEqual(
                response.get_data(as_text=True),
                "apple"
            )

        with test_client.get("/path/apple/pear/") as response:

            self.assertEqual(
                response.get_data(as_text=True),
                "apple/pear"
            )


if __name__ == "__main__":
    unittest.main()
