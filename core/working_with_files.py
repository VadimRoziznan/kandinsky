import uuid
import os


def write_image_data(image_data, prompt, dirr="res"):
    try:
        truncated_prompt = prompt[:20]
    except Exception as e:
        print(e)
        truncated_prompt = "image"

    if not os.path.exists(dirr):
        os.makedirs(dirr)

    filename = f"{dirr}/{truncated_prompt.split('.')[0]}_{uuid.uuid4()}.jpg"

    try:
        with open(filename, "wb") as file:
            file.write(image_data)
    except OSError as e:
        print(f"An error occurred: {e}")
