import json, requests
import sweeps

class Boi:
    def __init__(self, id):
        body = json.dumps({'key': sweeps.APIKey, 'id': id})
        boi_json = requests.put(BASE_URL+'getBoi', body).json()
        self.x = boi_json.x
        self.y = boi_json.y
        self.sector = boi_json.sectorID
        self.energy = boi_json.energy
               
    def move(direction):
        
    def detect(direction):

    def eat(direction):
