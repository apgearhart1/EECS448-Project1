class board:
	def __init__(self, rowSize, colSize, boatlist):
		self.rowSize = rowSize
		self.colSize = colSize
		self.boardStorage = [[0 for y in range(colSize)] for x in range(rowSize)]
        for boat in boatlist:
            for coordinate in boat.getCoordinates():
                self.boardStorage[coordinate[0]][coordinate[1]] = 1
		self.hits = [[]]
		self.misses = [[]]
		
	def isMiss(self, xPos, yPos):
		if(self.misses[xPos][yPos] == True):
			return True
        
		return False
		
	def isHitt(self, xPos, yPos):
		if(self.hits[xPos][yPos] == True):
			return True
		else:
			return False
        
	def getSize(self):
		return (self.rowSize, self.colSize)
		
	def testBoard(self):
		b = [[0 for y in range(8)] for x in range(8)]
		print(b)

    def isBoat(xPos, yPos):
        if(self.boardStorage[xPos][yPos] == 1):
            return True
        return False


