import json

from core.generator import image_generation
from core.working_with_files import write_image_data


try:
    with open("prompts.json", "r") as file:
        data = json.load(file)
except FileNotFoundError as e:
    print(e)

for el in data:
    image_data = image_generation(el["prompt"], el["decor"])
    write_image_data(
        image_data,
        el["task"],
    )
