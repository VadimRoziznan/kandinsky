import uuid


def write_image_data(image_data, prompt, dirr="res"):
    try:
        truncated_prompt = prompt[:20]
    except Exception as e:
        print(e)
        truncated_prompt = "image"

    filename = f"{dirr}/{truncated_prompt.split('.')[0]}_{uuid.uuid4()}.jpg"

    try:
        with open(filename, "wb") as file:
            file.write(image_data)
    except OSError as e:
        print(f"An error occurred: {e}")
