import socket

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template(template_name_or_list="index.html")


if __name__ == "__main__":
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    app.run(host=ip, port=80, debug=True)
