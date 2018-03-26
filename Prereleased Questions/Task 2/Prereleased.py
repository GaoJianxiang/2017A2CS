#2.3
class Toy:
	def __init__(self):
		self.__Name = ""
		self.__ID = ""
		self.__Price = 0
		self.__MinimumAge = 0

	def GetName(self):
		return self.__Name

	def GetID(self):
		return self.__ID

	def GetPrice(self):
		return self.__Price

	def GetMinimumAge(self):
		return self.__MinimumAge

	def SetName(self,n):
		self.__Name = n

	def SetID(self,i):
		self.__ID = i

	def SetPrice(self,p):
		self.__Price = p

	def SetMinimumAge(self,m):
		self.__MinimumAge = m


#2.4
class ComputerGame:
	def __init__(self):
		Toy.__init__(self)
		self.__Category = ""
		self.__Console = ""

	def GetCategory(self):
		return self.__Category

	def GetConsole(self):
		return self.__Console

	def SetCategory(self,c):
		self.__Category = c

	def SetConsole(self,c):
		self.__Console = c

class Vehicle:
	def __init__(self):
		Toy.__init__(self)
		self.__Type = ""
		self.__Height = 0
		self.__Length = 0
		self.__Weight = 0

	def GetType(self):
		return self.__Type

	def GetHeight(self):
		return self.__Height

	def GetLength(self):
		return self.__Length

	def GetWeight(self):
		return self.__Weight

	def SetType(self,t):
		self.__Type = t

	def SetHeight(self,h):
		self.__Height = h

	def SetLength(self,l):
		self.__Length = l

	def SetWeight(self,w):
		self.___Weight = w

#2.5
class Toy(self):
	def SetMinimumAge(self):
#2.6
toyArray = []
newToy = Vehicle()
newToy.SetName("Red Sports Car")
newToy.SetID("RSC13")
newToy.SetMinimumAge(6)
newToy.SetType("Car")
newToy.SetHeight(3.3)
newToy.SetLength(12.1)
newToy.SetWeight(0.08)
toyArray.append(newToy)

#2.7
class Toy:
	def PrintInfo(self):
		print(" Name:",self.__name)
		print(" ID:",self.__ID)
		print(" Price:",self.__Price)
		print(" Minimum age:",self.__MinimumAge)

class ComputerGame(self):
	def PrintInfo(self):
		print("Computer game:")
		toy.PrintInfo(self)
		print(" Category:",self.__Category)
		print(" Console:",self.__Console)

class Vehicle(self):
	def PrintInfo(self):
		print("Vehicle:")
		toy.PrintInfo(self)
		print(" Type:",self.__Type)
		print(" Height:",self.__Height)
		print(" Length:",self.__Length)
		print(" Weight:",self.__Weight)

def FindToy(ID):
	for i in toyArray:
		if i.GetID == ID:
			i.PrintInfo()
			break
	print("Requested toy not found")

