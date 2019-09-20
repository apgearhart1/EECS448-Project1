from player import Player
from boats import Boat
#from board import board

class Executive:

	def __init__(self):
		self.player1 = Player()
		self.player2 = Player()
		self.turns = 1
	
	def selectBoats(self, numBoats, player):	
		if player == "player1":
			for i in range(1,numBoats):
				self.player1.placeShip(i)
		if player == "player2":
			for j in range(1,numBoats):
				self.player2.placeShip(j)
		else:
			return "Error, boats could not be placed"

		
	def playerTurn(self):
		if self.turns % 2 == 0:
			self.turns += 1
			return "player2"
			
		else:
			self.turns += 1
			return "player1"
		
	def attack(self, location):
		if self.playerTurn() == "player1":
			for i in self.player2.getShipList():
				if self.player2.getShip(i).getcoordinates() == location:
					self.player2.getShip(i).hit(location)
					
		elif self.playerTurn() == "player2":
			for i in self.player1.getShipList():
				if self.player1.getShip(i).getcoordinates() == location:
					self.player1.getShip(i).hit(location)
					
	def checkWin(self):
		if self.player1.getCoordinateList() == []:
			return True
		if self.player2.getCoordinateList() == []:
			return True
		return False
					
			