from main.apikeys import NASA_API_KEY
import requests
import json

    

url = "https://api.nasa.gov/mars-photos/api/v1/rovers/"

class ImagesParser:
    def __init__(self, rover, camera, sol):
        self.rover = rover
        self.camera = camera
        self.sol = sol
        self.images = []

    def get_main_url(self):
        return url + self.rover + "/photos?sol=" + self.sol + "&camera=" + self.camera + "&api_key=" + NASA_API_KEY

    def get_images_links(self):
        r = requests.get(self.get_main_url())
        images_json = r.content
        images = json.loads(images_json)
        return images
    