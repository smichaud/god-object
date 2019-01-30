import os
from glob import glob
from flask import Flask, jsonify, render_template, send_from_directory, request
from werkzeug.utils import secure_filename
from flask_cors import CORS

APP_DIR = os.path.abspath(os.path.dirname(__file__))
STATIC_FOLDER = os.path.join(APP_DIR, "../frontend/build/static")
TEMPLATE_FOLDER = os.path.join(APP_DIR, "../frontend/build/")
UPLOAD_FOLDER = os.path.join(APP_DIR, "../data")
ALLOWED_EXTENSIONS = set(["jpg", "jpeg"])


app = Flask(__name__, static_folder=STATIC_FOLDER, template_folder=TEMPLATE_FOLDER)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
CORS(app)


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        TEMPLATE_FOLDER, "favicon.ico", mimetype="image/vnd.microsoft.icon"
    )


@app.route("/api/photo", methods=["POST"])
def post_photo():
    if request.method == "POST":
        if "file" not in request.files:
            return jsonify({"info": "No 'file' in 'request.files'"})

        file = request.files["file"]
        if file.filename == "":
            return jsonify({"info": "No filename"})
        elif file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            return jsonify({"info": "Success"})
        else:
            return jsonify({"info": "Invalid extension"})


@app.route("/api/photos/", methods=["GET"])
def get_photos():
    filenames = []
    for filename in glob("/home/smichaud/Workspace/showcase/data/*.jpg"):
        filenames.append(os.path.basename(filename))

    filenames.sort(reverse=True)
    return jsonify({"filenames": filenames})


@app.route("/photos/<path:filename>", methods=["GET"])
def get_photo(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def index(path):
    return render_template("index.html")


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


if __name__ == "__main__":
    app.run(use_reloader=True, debug=True, host="0.0.0.0", port=5000, threaded=False)
