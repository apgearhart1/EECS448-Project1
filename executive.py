from player import Player

class Executive:

	def __init__(self):
		self.player1 = Player()
		self.player2 = Player()
	
	def select():
		print("Select number of boats")
		num = input()
		
		if num > 0 and num < 6:
			for i in range(num):
				self.player1.placeShip(i)
			for j in range(num):
				self.player2.placeShip(j)
		
		