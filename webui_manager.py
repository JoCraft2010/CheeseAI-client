import webbrowser
from flask import Flask, render_template
from webui import transformers_webui, diffusers_webui


def index():
    return render_template("index.html")


def four_zero_four(e):
    return render_template("errorhandlers/404.html"), 404


def five_zero_zero(e):
    return render_template("errorhandlers/500.html"), 500


def start():
    app = Flask("CheeseAI client")

    app.route("/")(index)

    transformers_webui.register_all(app)
    diffusers_webui.register_all(app)

    app.errorhandler(404)(four_zero_four)
    app.errorhandler(500)(five_zero_zero)

    webbrowser.open_new('http://127.0.0.1:80/')
    app.run(host="127.0.0.1", port=80, debug=False)
