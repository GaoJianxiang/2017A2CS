class borrower:
	def __init__(self):
		self.__borrowerName = ""
		self.__emailAddress = ""
		self.__borrowerID = None
		self.__itemsOnLoan = 0

	def __repr__(self):
		return (self.__borrowerName, self.__emailAddress, self.__borrowerID, self.__itemsOnLoan)
	def GetBorrowerName(self):
		return self.__borrowerName

	def GetEmailAddress(self):
		return self.__emailAddress

	def GetBorrwerID(self):
		return self.__borrowerID

	def GetItemsOnLoan(self):
		return self.__itemsOnLoan

	def UpdateItemsOnLoan(self):
		self.__itemsOnLoan += 1

	def PrintDetails(self):
		print(self.__borrowerName)

B = borrower()
B.UpdateItemsOnLoan()
print(B)


def DetermineSalary(salary):
	if salary > 50:
		if salary >= 90:
			return ('Project Manager')
		elif salary < 90 and salary >70:
			return ('Consultant')
		else:
			return ('Lead Developer')
	return('Manager')

