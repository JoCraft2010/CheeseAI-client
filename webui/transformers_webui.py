from flask import render_template, request
from markupsafe import Markup
import helper_tools
import threading
from pipeline_manager import TextGenerationPipeline
from pipeline_cache import pipeline


def transformers_index():
    models = [f"<a href=\"/transformers/model_menu?m={m}\">{m}</a>" for m in helper_tools.list_installed_models()]
    return render_template("transformers/index.html", installed_models=Markup("".join(models)))


def transformers_model_menu():
    if "m" in request.args:
        return render_template("transformers/model_menu.html", model=request.args["m"])
    else:
        return redirect("/")


def transformers_simple_chat():
    if "m" in request.args:
        return render_template("transformers/simple_chat.html", model=request.args["m"])
    else:
        return redirect("/")


def transformers_irt_generative_chat():
    if "m" in request.args:
        return render_template("transformers/irt_generative_chat.html", model=request.args["m"])
    else:
        return redirect("/")


def transformers_add_model():
    return render_template("transformers/add_model.html")


def transformers_install_model():
    if "model_name" in request.args:
        thread = threading.Thread(target=helper_tools.install_model, args=(request.args["model_name"]))
        thread.start()
        return render_template("transformers/installing.html")
    else:
        return redirect("/")


def transformers_api_chat_request():
    global pipeline
    if "model" in request.args and "value" in request.args and "length" in request.args:
        model = request.args["model"]
        value = request.args["value"]
        length = request.args["length"]
        if pipeline[0] != model:
            pipeline[0] = model
            pipeline[1] = TextGenerationPipeline(model)
        response = pipeline[1].generate(value, int(length))
        return {
            "message": response
        }
    else:
        return {}


def transformers_api_chat_request_small():
    global pipeline
    if "model" in request.args and "value" in request.args:
        model = request.args["model"]
        value = request.args["value"]
        if pipeline[0] != model:
            pipeline[0] = model
            pipeline[1] = TextGenerationPipeline(model)
        response = pipeline[1].generate(value, 1)
        return {
            "message": response
        }
    else:
        return {}


def register_all(app):
    app.route("/transformers")(transformers_index)
    app.route("/transformers/model_menu", methods=['GET'])(transformers_model_menu)
    app.route("/transformers/simple_chat", methods=['GET'])(transformers_simple_chat)
    app.route("/transformers/irt_generative_chat", methods=['GET'])(transformers_irt_generative_chat)
    app.route("/transformers/add_model")(transformers_add_model)
    app.route("/transformers/install_model", methods=['GET'])(transformers_install_model)
    app.route("/transformers/api_chat_request", methods=['GET'])(transformers_api_chat_request)
    app.route("/transformers/api_chat_request_small", methods=['GET'])(transformers_api_chat_request_small)
