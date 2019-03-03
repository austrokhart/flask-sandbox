
from flask import Flask
from main import files_uploading

import unittest
import os

from datetime import datetime
from werkzeug.utils import secure_filename
from io import BytesIO


app = Flask(__name__)
app.register_blueprint(files_uploading)


test_client = app.test_client()

current_dir = os.path.dirname(os.path.realpath(__file__))
upload_dir = os.path.join(current_dir, "files")


class TestFilesUploading(unittest.TestCase):

    # file uploading testing
    def test_file_uploading(self):

        # the file
        file_name = "test_file.jpg"
        temp_name = secure_filename(str.join(" ", ["temp", str(datetime.now())]))

        # open the file as bytes
        with open(os.path.join(current_dir, file_name), "rb") as file:

            # use BytesIO to include file data to request
            with test_client.post("/", data={
                "file": (BytesIO(file.read()), temp_name)
            }) as response:

                # check that the file was written and remove them after
                self.assertTrue(os.path.isfile(os.path.join(upload_dir, temp_name)))
                os.remove(os.path.join(upload_dir, temp_name))


if __name__ == "__main__":
    unittest.main()
