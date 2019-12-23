import json, requests

class Map:
    # needs map in json to init
    # TODO: minimize use of the /getMap endpoint to prevent CPU melting. Possibly cache some form of the map, but what data changes little enough to be worth caching?

    # Is it even worth having this class be initialized? or should this just be a utility class
    def __init__(self, map):
        
    # getSector won't be functional until we transition to [x].[y]-formatted sector ID system instead of (x, y) coordinates
    def getSector(id):
        body = json.dumps({'id': id})
        s = requests.put(constants.BASE_URL + 'getSector', body)
        return s
        
        
# This class makes much more sense to instantiate
class Sector:
    def __init__():
        

    @property
    def entities():


    
