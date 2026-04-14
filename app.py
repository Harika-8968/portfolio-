from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Certificates route
@app.route("/certificates/<path:filename>")
def certificates(filename):
    return send_from_directory(
        os.path.join(app.root_path, "static/certificates"),
        filename
    )


if __name__ == "__main__":
    app.run(debug=True)