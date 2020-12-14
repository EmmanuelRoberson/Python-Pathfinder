class WayPoint:
    
    def __init__(self, xVal, yVal):
        self.x = xVal #x positional value
        self.y = yVal #y positional value
        self.neighbors = [] #list of neighbor waypoints
        self.parent = None #parent waypoint

    def get_neighbors(self): #return neighbor waypoints
        return self.neighbors