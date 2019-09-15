from board import board 
from boats import boat


class Player:
	def __init__(self, myBoard, theirBoard):
		# this player's list of ships
		self.shipList = [] 
		# this player's board
		self.myBoard = myBoard(8,8)
		# opponent's board		
		self.theirBoard = theirBoard(8,8)

	def shipsDestroyed(self):
		counter = 0
		for i in self.shipList:
			if shelf.shipList[i].checkDestroyed():
				counter = counter + 1
				
	
		return counter
	

	def placeShip(self, length):
		# print coordinates and store them in a tuple
		print("Select x coordinate: ")
		x = input()
		print("Select y coordinate: ")
		y = input()
		location = (x,y) 
		# creates a new ship
		tempShip = boat(length, location)
		
		if tempShip.validPlace(length, location):
			self.shipList.append(tempShip)
			# place ship on board here
			return True
			
		else:
			return False
		
		
	def attack(self, location):
		 #write code that uses board methods
		for i in location:
			for j in location:
				#attack opponent board at i,j  
	
