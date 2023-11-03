from flask import render_template, request, jsonify, make_response
from markupsafe import Markup
import helper_tools
import threading
from pipeline_cache import pipeline
from pipeline_manager import Text2ImagePipeline
import io
import base64


def diffusers_index():
    models = [f"<a href=\"/diffusers/model_menu?m={m}\">{m}</a>" for m in helper_tools.list_installed_models()]
    return render_template("diffusers/index.html", installed_models=Markup("".join(models)))


def diffusers_model_menu():
    if "m" in request.args:
        return render_template("diffusers/model_menu.html", model=request.args["m"])
    else:
        return redirect("/")


def diffusers_simple_image_generation():
    if "m" in request.args:
        return render_template("diffusers/simple_image_generation.html", model=request.args["m"])
    else:
        return redirect("/")


def diffusers_add_model():
    return render_template("diffusers/add_model.html")


def diffusers_install_model():
    if "model_name" in request.args:
        thread = threading.Thread(target=helper_tools.install_model, args=(request.args["model_name"]))
        thread.start()
        return render_template("diffusers/installing.html")
    else:
        return redirect("/")


def diffusers_api_chat_request():
    global pipeline
    if "model" in request.args and "value" in request.args and "width" in request.args and "height" in request.args:
        model = request.args["model"]
        value = request.args["value"]
        width = request.args["width"]
        height = request.args["height"]
        if pipeline[0] != model:
            pipeline[0] = model
            pipeline[1] = Text2ImagePipeline(model)

        print(f"\nGenerating image for prompt \"{value}\" using model \"{model}\" at resolution {width}x{height}.")

        image = pipeline[1].generate(value, width=int(width), height=int(height))

        image_byte_array = io.BytesIO()
        image.save(image_byte_array, format='JPEG')
        image_byte_array = image_byte_array.getvalue()
        image_base64 = base64.b64encode(image_byte_array).decode('utf-8')

        response = {
            "image": image_base64
        }

        return make_response(jsonify(response))
    else:
        return {}


def register_all(app):
    app.route("/diffusers")(diffusers_index)
    app.route("/diffusers/model_menu", methods=['GET'])(diffusers_model_menu)
    app.route("/diffusers/simple_image_generation", methods=['GET'])(diffusers_simple_image_generation)
    app.route("/diffusers/add_model")(diffusers_add_model)
    app.route("/diffusers/install_model", methods=['GET'])(diffusers_install_model)
    app.route("/diffusers/api_chat_request", methods=['GET'])(diffusers_api_chat_request)
