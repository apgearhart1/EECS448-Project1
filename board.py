class board:
	def __init__(self, rowSize, colSize):
		self.rowSize = rowSize
		self.colSize = colSize
		self.boardStorage = [[0 for y in range(colSize)] for x in range(rowSize)]
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