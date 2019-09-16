#from player import Player
#from boat import boat
#from board import board

class Executive:

	def __init__(self):
		self.player1 = Player()
		self.player2 = Player()
		self.turns = 1
	
	def select(self):	
		check = False
		while not check:
			print("Select number of boats (1-5)")
			num = input()
			if num > 0 and num < 6:
				for i in range(num):
					self.player1.placeShip(i)
				for j in range(num):
					self.player2.placeShip(j)
				check = True
			else:
				print("Invalid number of boats!")
		
	def playerTurn(self):
		if self.turns % 2 == 0:
			self.turns += 1
			return "player2"
			
		else:
			self.turns += 1
			return "player1"
		
	def attack(self):
		if self.playerTurn() == "player1":
			#check where the player clicks here 
			#location = where the player clicks
			tempShipList = self.player2.getShipList()
			for i in tempShipList:
				if self.player2.getShip(i).getcoordinates() == location:
					self.player2.getShip(i).hit(location)
		elif self.playerTurn() == "player2":
			tempShipList = self.player1.getShipList()
			for i in tempShipList:
				if self.player1.getShip(i).getcoordinates() == location:
					self.player1.getShip(i).hit(location)
					
			