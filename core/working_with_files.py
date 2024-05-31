import json
import uuid
import os


def write_image_data(image_data, file_name, dir="images"):

    if not os.path.exists(dir):
        os.makedirs(dir)

    filename = f"{dir}/{file_name}__{uuid.uuid4()}.jpg"

    try:
        with open(filename, "wb") as file:
            file.write(image_data)
    except OSError as e:
        print(f"An error occurred: {e}")


def open_file():
    try:
        with open("prompts.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError as e:
        print(e)
        data = []

    return data
