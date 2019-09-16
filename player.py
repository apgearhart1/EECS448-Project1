from board import board 
from boats import boat


class Player:
	def __init__(self):
		# this player's ships
		self.shipList = [] 
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
	

	def placeShip(self, length):
		# need to get coordinates from click and store them in location variable 
		
		# creates a new ship
		tempShip = boat(length, location)
		
		if tempShip.validPlace(length, location):
			self.shipList.append(tempShip)
			self.myBoard.place(location)
			return True			
		else:
			#print("Invalid placement")
			return False
			
	def getShipList()
		return self.shipList
	
		
			
		
	
