from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
from diffusers import DiffusionPipeline
import torch
import configini


class BasePipeline:
    def __init__(self, model):
        self.model = model

    def generate(self, user_input):
        pass


class TextGenerationPipeline(BasePipeline):
    def __init__(self, model):
        super().__init__(model)
        model = AutoModelForCausalLM.from_pretrained(self.model, ignore_mismatched_sizes=True)
        if configini.general__use_CUDA:
            model.to(torch.device("cuda"))
        tokenizer = AutoTokenizer.from_pretrained(self.model)
        if configini.general__use_CUDA:
            self.pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer, device=torch.device("cuda"))
        else:
            self.pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer)

    def generate(self, user_input, max_output_len=64):
        response = self.pipeline(user_input, max_length=len(user_input) + max_output_len)[0]["generated_text"]
        response = response[(len(user_input) + 1):]
        return response


class Text2ImagePipeline(BasePipeline):
    def __init__(self, model):
        super().__init__(model)
        if configini.patches__GTX1660_patch:
            self.pipeline = DiffusionPipeline.from_pretrained(self.model, torch_dtype=torch.float32, safety_checker=None, requires_safety_checker=False)
        else:
            self.pipeline = DiffusionPipeline.from_pretrained(self.model, torch_dtype=torch.float16, safety_checker=None, requires_safety_checker=False)
        if configini.general__use_CUDA and configini.patches__GTX1660_patch:
            self.pipeline.enable_sequential_cpu_offload()
        elif configini.general__use_CUDA:
            self.pipeline.to(torch.device("cuda"))

    def generate(self, user_input, width=1920, height=1080):
        response = self.pipeline(user_input, negative_prompt="lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry", width=width, height=height).images[0]
        return response
