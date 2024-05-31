import uuid
import os


def write_image_data(image_data, file_name, dirr="res"):

    if not os.path.exists(dirr):
        os.makedirs(dirr)

    filename = f"{dirr}/{file_name}_{uuid.uuid4()}.jpg"

    try:
        with open(filename, "wb") as file:
            file.write(image_data)
    except OSError as e:
        print(f"An error occurred: {e}")
