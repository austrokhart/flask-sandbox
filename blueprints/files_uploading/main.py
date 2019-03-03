
from flask import Blueprint, request, render_template
from os import path
from werkzeug.utils import secure_filename


files_uploading = Blueprint("files_uploading", __name__, template_folder="templates")

current_dir = path.dirname(path.realpath(__file__))
upload_dir = path.join(current_dir, "files")


@files_uploading.route("/", methods=["GET", "POST"])
def file_uploading():

    uploaded_files = []

    if request.method == "POST":

        for name, file in request.files.items():

            filename = secure_filename(file.filename)

            file.save(path.join(upload_dir, filename))
            uploaded_files.append(filename)

    return render_template("files_uploading/file_uploading.html", title=files_uploading.name, uploaded_files=uploaded_files)
