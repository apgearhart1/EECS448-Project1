class Player:
	def __init__(self, myBoard, theirBoard):
		# this player's list of ships
		self.shipList = [] 
		# this player's board
		self.myBoard = myBoard
		# opponent's board		
		self.theirBoard = theirBoard 

	

	def placeShip(length):
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
			return "Player ship placed!"
			
		else:
			return "Ship could not be placed!"
		
		
	#def attack(self, location):
		# write code that uses board methods
		#for i in location:
			#for j in location:
				# attack opponent board at i,j  
		
	#def shipsDestroyed():
		#for i in self.shipList
			# put board code here 