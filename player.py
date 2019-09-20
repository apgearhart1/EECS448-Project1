#from board import board 
from boats import Boat
import copy


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
		"""Checks to see how many ships have been destroyed


        Returns:
        Returns the number of a player's ships that have been destroyed
        """
		# increment counter for every ship that is destroyed 
		counter = 0
		for ship in self.shipList:
			if self.shipList[ship].checkDestroyed():
				counter = counter + 1
		return counter
	

	def placeShip(self, ship):		
		"""Places a ship on the player's board

        Args:
        ship - the ship object that needs to be placed on the board

        Returns:
        Returns true if the ship could be placed, false otherwise
        """
		if ship.validPlace(ship.getCoordinates()):
			self.shipList.append(ship)
			self.shipCoordinateList.append(ship.getCoordinates())
			#self.myBoard.place(location)
			return True			
		else:
			#print("Invalid placement")
			return False
			
	def getShipList(self):
		"""Gets the list of ships for this player

        Returns:
        Returns this player's list of ships
        """
		return self.shipList
		
	def getShip(self, index):
		"""Gets a specific ship in the player's list, ships should be organised by length i.e. a ship of size 3 is in the 3rd index 

        Args:
        index - the index of the player's ship

        Returns:
        Returns the ship object we want
        """
		return self.shipList[index]
		
	def getCoordinateList(self):
		"""Gets this player's current list of ship coordinates

        Returns:
        Returns the list of ship coordinates
        """
		return self.shipCoordinateList 
		
	def removeShip(coordinates):
		"""Removes ship from the players current list of ships and list of ship coordinates 

        Args:
        coordinates - coordinates of the ship we want to remove 

        Returns:
        Returns true if the ship was successfully removed, false otherwise
        """
		for ship in self.ShipList:
			if self.shipList[ship].getCoordinates() == coordinates:
				self.shipList.pop(ship)
				self.shipCoordinateList.remove(coordinates)
				return True
			else:
				return False
				
	def setOpBoard(opBoard):
		"""Copies oponent'ss board for this player

        Args:
        opBoard - oponent's board object

        Returns:
        None
        """
		self.opBoard = copy.deepcopy(opBoard)
		
		
			
		
	
