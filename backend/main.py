import os
from flask import Flask, render_template, send_from_directory

APP_DIR = os.path.abspath(os.path.dirname(__file__))
STATIC_FOLDER = os.path.join(APP_DIR, '../frontend/build/static')
TEMPLATE_FOLDER = os.path.join(APP_DIR, '../frontend/build/')

app = Flask(__name__, static_folder=STATIC_FOLDER, template_folder=TEMPLATE_FOLDER)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(TEMPLATE_FOLDER, 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/api/greeting")
def hello_world():
    return "Welcome to the Showcase!"

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

if __name__ == "__main__":
    app.run(use_reloader=True, debug=True, host= "0.0.0.0", port=5000, threaded=True)
