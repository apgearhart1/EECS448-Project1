from board import board 
from boats import Boat


class Player:
	def __init__(self):
		# this player's ships
		self.shipList = [] 
		self.shipCoordinateList = []
		# this player's board
		self.myBoard = myBoard(8,8)
		# opponent's board		
		self.theirBoard = theirBoard(8,8)

	def shipsDestroyed(self):
		# increment counter for every ship that is destroyed 
		counter = 0
		for i in self.shipList:
			if shelf.shipList[i].checkDestroyed():
				counter = counter + 1
		return counter
	

	def placeShip(self, length, location):	
		# creates a new ship
		tempShip = Boat(length, location)
		
		if tempShip.validPlace(length, location):
			self.shipList.append(tempShip)
			self.shipCoordinateList.append(location)
			self.myBoard.place(location)
			return True			
		else:
			#print("Invalid placement")
			return False
			
	def getShipList(self):
		return self.shipList
		
	def getShip(self, index):
		return self.shipList[index]
		
	def getCoordinateList(self):
		return self.shipCoordinateList 
		
			
		
	
