from board import board 
from boats import Boat
import copy


class Player:
	def __init__(self):
		# this player's ships
		self.shipList = [] 
		self.shipCoordinateList = []
		# this player's board
		self.myBoard = board(8,8)
		# opponent's board		
		self.opBoard = board(8,8)

	def shipsDestroyed(self):
		"""Checks to see how many ships have been destroyed


        Returns:
        Returns the number of a player's ships that have been destroyed
        """
		# increment counter for every ship that is destroyed 
		counter = 0
		for i in range(len(self.shipList)):
			if self.shipList[i].checkDestroyed():
				counter = counter + 1
		return counter
	

	def placeShip(self, ship):		
		"""Places a ship in the player's ship list

        Args:
        ship - the ship object that needs to be placed 

        Returns:
        Returns true if the ship could be placed, false otherwise
        """
		self.shipList.append(ship)
		self.shipCoordinateList.append(ship.getCoordinates())
		
			
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
		
	def removeShip(self, coordinates):
		"""Removes ship from the players current list of ships and list of ship coordinates 

        Args:
        coordinates - coordinates of the ship we want to remove 

        Returns:
        Returns true if the ship was successfully removed, false otherwise
        """
		for ship in self.shipList:
			for i in range(0,4):
				if self.shipList[i].getCoordinates() == coordinates:
					self.shipList.pop(i)
					self.shipCoordinateList.remove(coordinates)
					return True
				
		return False
				
	def setOpBoard(self, opBoard):
		"""Copies oponent's board for this player

        Args:
        opBoard - oponent's board object

        Returns:
        None
        """

		self.opBoard = opBoard
		
	def getMyBoard(self):
		"""Gets this player's board

        Args:
        None

        Returns:
        This player's board object
        """
		return self.myBoard
		
	def getOpBoard(self):
		"""Gets this opponent's board

        Args:
        None

        Returns:
        Opponent's board object
        """
		return self.opBoard
	
	def addToBoard(self):
		"""Populates board according to this player's current list of ships

        Args:
        None

        Returns:
        None
        """
		self.myBoard.populateBoard(self.shipList)
	
	def addToHitList(self, i, j):
		for k in range(0, len(self.shipList)):
			if (i,j) in self.shipList[k].getCoordinates():
				self.shipList[k].hit((i,j))