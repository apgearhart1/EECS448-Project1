class board:
    def __init__(self, size):
        self.size = size
        self.hits = [[]]
        self.misses = [[]]
    def isMiss(self, xPos, yPos):
        if(self.misses[xPos][yPos] == True):
            return True
        
        return False
    def isHitt(self, xPos, yPos):
        if(self.hits[xPos][yPos] == True):
            return True
        
        return False
        
    def getSize(self):
        return self.size
