#from board import board 
from boats import Boat


class Player:
	def __init__(self):
		# this player's ships
		self.shipList = [] 
		self.shipCoordinateList = []
		# this player's board
		self.myBoard = board(8,8,[])
		# opponent's board		
		self.opBoard = board(8,8,[])

	def shipsDestroyed(self):
		# increment counter for every ship that is destroyed 
		counter = 0
		for i in self.shipList:
			if shelf.shipList[i].checkDestroyed():
				counter = counter + 1
		return counter
	

	def placeShip(self, ship):			
		if ship.validPlace(ship.getCoordinates()):
			self.shipList.append(ship)
			self.shipCoordinateList.append(ship.getCoordinates())
			#self.myBoard.place(location)
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
		
	def removeShip(coordinates):
		for ship in self.ShipList:
			if self.shipList[ship].getCoordinates() == coordinates:
				self.shipList.pop(ship)
				self.shipCoordinateList.remove(coordinates)
				return True
			else:
				return False
		
			
		
	
