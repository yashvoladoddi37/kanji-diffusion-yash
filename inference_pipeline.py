# git clone https://github.com/huggingface/diffusers
# pip install git+https://github.com/huggingface/diffusers
# pip install -r requirements.txt
# huggingface-cli login

from diffusers import StableDiffusionPipeline
import torch

model_path = "yashvoladoddi37/kanji-diffusion-v1-4"
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16, use_safetensors = True).to("cuda")
pipe.unet.load_attn_procs(model_path)
pipe.to("cuda")

prompt = "A Kanji meaning baby robot"
image = pipe(prompt).images[0]
image.save("baby-robot-kanji-v1-4.png")