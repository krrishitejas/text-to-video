# text_to_video.py
import torch
from PIL import Image
from moviepy.editor import ImageSequenceClip
from diffusers import StableDiffusionPipeline

# Set up the Stable Diffusion pipeline
model_id = "CompVis/stable-diffusion-v1-4"
pipe = StableDiffusionPipeline.from_pretrained(model_id)
pipe.to("cuda" if torch.cuda.is_available() else "cpu")

# Define text prompts
prompts = [
    "A serene landscape with mountains",
    "A bustling city at night",
    "A calm beach with a sunset",
]

# Generate images
images = []
for prompt in prompts:
    image = pipe(prompt).images[0]
    image_path = f"{prompt.replace(' ', '_')}.png"
    image.save(image_path)
    images.append(image_path)

# Convert images to video
clip = ImageSequenceClip(images, fps=1)  # Adjust fps as needed
clip.write_videofile("output_video.mp4", codec="libx264")

