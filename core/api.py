import requests
import json
import time
from tqdm import tqdm


class Text2ImageAPI:

    def __init__(self, url, api_key, secret_key):
        self.URL = url
        self.AUTH_HEADERS = {
            "X-Key": f"Key {api_key}",
            "X-Secret": f"Secret {secret_key}",
        }

    def get_model(self):
        response = requests.get(
            self.URL + "key/api/v1/models", headers=self.AUTH_HEADERS
        )
        data = response.json()
        return data[0]["id"]

    def generate(self, prompt, model, images=1, width=1024, height=1024):
        params = {
            "type": "GENERATE",
            "style": "string",
            "numImages": images,
            "width": width,
            "height": height,
            "generateParams": {
                "query": f"{prompt} для учебника по математики, мультфильм."
            },
        }

        data = {
            "model_id": (None, model),
            "params": (None, json.dumps(params), "application/json"),
        }
        response = requests.post(
            self.URL + "key/api/v1/text2image/run",
            headers=self.AUTH_HEADERS,
            files=data,
        )
        data = response.json()
        return data["uuid"]

    def check_generation(self, request_id, attempts=100, delay=24):
        while attempts > 0:
            response = requests.get(
                self.URL + "key/api/v1/text2image/status/" + request_id,
                headers=self.AUTH_HEADERS,
            )
            data = response.json()

            print("status:", data["status"])
            if data["status"] == "DONE":
                return data["images"]

            for i in tqdm(range(delay), desc="Loading", mininterval=0.1):
                time.sleep(1)
            attempts -= 1
