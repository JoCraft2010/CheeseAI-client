import os
from transformers import pipeline
from diffusers import DiffusionPipeline
import torch


def install_model(*args):
    mname = "".join(args)
    try:
        pipeline(model=mname)
    except:
        DiffusionPipeline.from_pretrained(mname, torch_dtype=torch.float32, safety_checker=None, requires_safety_checker=False)
    print(f"Installation for model {mname} done.")


def list_installed_models():
    cache_dir = os.path.expanduser("~/.cache/huggingface/hub")
    models = [m[8:].replace("--", "/", 1) for m in os.listdir(cache_dir)[:-2]]
    return models
