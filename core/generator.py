import os
import base64
from core.api import Text2ImageAPI
from core.working_with_files import write_image_data, open_file
from dotenv import load_dotenv

load_dotenv()


def image_generation(prompt, decor):
    full = prompt + " " + decor
    api = Text2ImageAPI(
        "https://api-key.fusionbrain.ai/", os.getenv("api_key"), os.getenv("secret_key")
    )
    model_id = api.get_model()
    uuid = api.generate(full, model_id)
    images = api.check_generation(uuid)

    image_base64 = images[0]

    image_data = base64.b64decode(image_base64)

    return image_data


def generating_images_all_tasks():
    data = open_file()

    for el in data:
        image_data = image_generation(el["prompt"], el["decor"])
        write_image_data(
            image_data,
            el["task"],
        )
    return


def generate_task_images(task_name):
    data = open_file()

    for el in data:
        if el["task"] == task_name:
            image_data = image_generation(el["prompt"], el["decor"])
            write_image_data(
                image_data,
                el["task"],
            )
    return
