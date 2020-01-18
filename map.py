from sweeps import Sweeps


class Map:
    def getSector(x, y):
		SID = x + "." + y
		Sweeps.apicall("sector", sectorID=SID)

    @staticmethod
    @property
    def worldmap():
        return [idstring for x in ]


class Sector:
    def __init__(self, sid=None, data=None):
        if data != None:
            self.data = data
        elif id != None:
                self.data = Sweeps.apicall("sector", sectorID=sid)

    @property
    def entities(self):
        return self.data.entities

    @property
    def energy(self):
        ar = []
        for i in self.data.entities:
            if i.type == "energy":
                ar += i
        return ar
