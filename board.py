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
        """Checks if there is a miss at a given square
        
        Args:
        xPos (int): the x position for the tile to check
        yPos (int): the y position for the tile to check
        
        Returns:
        True if there is a miss
        """
		if(self.misses[xPos][yPos] == True):
			return True
        
		return False
		
	def isHitt(self, xPos, yPos):
        """Checks if there is a hit at a given square
        
        Args:
        xPos (int): the x position for the tile to check
        yPos (int): the y position for the tile to check
        
        Returns:
        True if there is a hit
        """
		if(self.hits[xPos][yPos] == True):
			return True
		else:
			return False
        
	def getSize(self):
        """Returns size of the board
    
        Returns:
        Size of the board
        """
		return (self.rowSize, self.colSize)
		
	def testBoard(self):
        """Prints out the board for testing purposes
        """
		b = [[0 for y in range(8)] for x in range(8)]
		print(b)

    def isBoat(self, xPos, yPos):
        """Checks if there is a boat tile at a given square
            
        Args:
        xPos (int): the x position for the tile to check
        yPos (int): the y position for the tile to check
            
        Returns:
        True if there is a boats at the given tile
        """
        if(self.boardStorage[xPos][yPos] == 1):
            return True
        return False


