class boat:
    def __init__(self, size, coordinates):
        self.size = size
        self.coordinates = coordinates
        self.destroyed = False
        self.hitlist = []
    def validPlace(self, coordinates):
        for i in range(0, len(coordinates)):
            if i != (len(coordinates) - 1):
                if (coordinates[i][0] == coordinates[i+1][0]) or (coordinates[i][1] == coordinates[i+1][1]):
                    return False
            else:
                if (coordinates[i][0] != coordinates[i-1][0]) or (coordinates[i][1] == coordinates[i-1][1]):
                    return False
        return True

    def checkDestroyed(self):
        if(len(self.hitlist) == self.size):
            self.destroyed = True
            return True
        else:
            self.destroyed = False
            return False
    def hit(self, coordinate):
        if coordinate not in self.coordinates:
            return "Miss!"
        else:
            if self.destroyed == False and coordinate not in self.hitlist:
                self.hitlist.append(coordinate)
            check = checkDestroyed(self)
            if check == True:
                return "Hit Confirmed & Boat is Destroyed!"
            else:
                return "Hit Confirmed!"
    def getCoordinates(self):
        return self.coordinates
    def getSize(self):
        return self.size