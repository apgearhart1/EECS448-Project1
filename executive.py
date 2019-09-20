from player import Player
from boats import Boat
#from board import board

class Executive:

	def __init__(self):
		self.player1 = Player()
		self.player2 = Player()
		self.turns = 1
	
	def selectBoats(self, numBoats):
		"""Places ships on the board based on the number of boats specified before the game starts 

        Args:
        numBoats - the number of boats to be placed on the boards. 
        """	
		for i in range(1,numBoats):
			self.player1.placeShip(i)
		for j in range(1,numBoats):
			self.player2.placeShip(j)

		
	def playerTurn(self):
		"""Checks to see which player's turn it is

        Returns:
        Returns a string for player1 or player2 depending on who's turn it is 
        """
		if self.turns % 2 == 0:
			self.turns += 1
			return "player2"
			
		else:
			self.turns += 1
			return "player1"
		
	def attack(self, location):
		"""Attacks a ship at a specified location 

        Args:
        location - a tuple containing the cooardinates of the ship to be attacked
        """
		if self.playerTurn() == "player1":
			for i in self.player2.getShipList():
				if self.player2.getShip(i).getcoordinates() == location:
					self.player2.getShip(i).hit(location)
					
		elif self.playerTurn() == "player2":
			for i in self.player1.getShipList():
				if self.player1.getShip(i).getcoordinates() == location:
					self.player1.getShip(i).hit(location)
					
	def checkWin(self):
		"""Checks to see if the game has been won

        Returns:
        Returns true if the game has been won, false otherwise
        """
		# Need to specify which player won at the end of the game 
		if self.player1.getCoordinateList() == []:
			return True
		if self.player2.getCoordinateList() == []:
			return True
		return False
					
			