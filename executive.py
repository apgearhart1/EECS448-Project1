from player import Player

class Executive:

	def __init__(self):
		self.player1 = Player()
		self.player2 = Player()
		self.turns = 1
	
	def select():	
		check = False
		while not check:
			print("Select number of boats (1-5): ")
			num = input()
			if num > 0 and num < 6:
				for i in range(num):
					self.player1.placeShip(i)
				for j in range(num):
					self.player2.placeShip(j)
				check = True
			else:
				print("Invalid number of boats!")
		
	def turn(self):
		if self.turns % 2 == 0:
			self.turns += 1
			return "player2"
			
		else:
			self.turns += 1
			return "player1"
		
		