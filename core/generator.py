import os
import base64
from core.api import Text2ImageAPI
from dotenv import load_dotenv

load_dotenv()


def image_generation(prompt, exercise):
    full = prompt + ' ' + exercise
    api = Text2ImageAPI('https://api-key.fusionbrain.ai/', os.getenv('api_key'), os.getenv('secret_key'))
    model_id = api.get_model()
    uuid = api.generate(full, model_id)
    images = api.check_generation(uuid)

    image_base64 = images[0]

    image_data = base64.b64decode(image_base64)

    return image_data
