import datetime
class LibraryItem:
    def __init__(self, t, a, i):
        self.__Title = t
        self.__Author__Artist = a
        self.__ItemID = i
        self.__OnLoan = False
        self.__DueDate = datetime.date.today()
        self.__BorrowerID = None

    def GetTitle(self):
        return(self.__Title)

    def Borrowing(self):
        self.__OnLoan = True
        self.__DueDate = self.__DueDate + datetime.timedelta(weeks=3)

    def Returning(self):
        self.__OnLoan = False

    def PrintDetails(self):
        print(self.__Title,'; ',self.__Author__Artist,';', end='')
        print(self.__ItemID,';',self.__OnLoan,';',self.__DueDate)

class Book(LibraryItem):
    def __init__(self, t, a, i):
        LibraryItem.__init__(self, t, a, i)
        self.__IsRequested = False
        self.__RequestedBy = None
    def GetIsRequested(self):
        return(self.__IsRequested)

    def SetIsREquested(self):
        self.__IsRequested = True

    def RequestBy(self):
        return self.__RequestedBy

    def PrintDetails(self):
        print('book details')
        LibraryItem.PrintDetails(self)
        print(self.__IsRequested,self.__RequestedBy)


class CD(LibraryItem):
    def __init__(self, t, a, i):
        LibraryItem.__init__(self, t, a, i)
        self.__Genre = ""

    def GetGenre(self):
        return(self.__Genre)

    def SetGenre(self, g):
        self.__Genre = g

class Borrower:
	def __init__(self,bname,email,borrowerid):
		self.__borrowerName = bname
		self.__emailAddress = email
		self.__borrowerID = borrowerid
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
		print(self.__borrowerName, self.__borrowerID,self.__emailAddress,self.__itemsOnLoan)

def menu():
    print('1 - Add a new borrower')
    print('2 - Add a new book')
    print('3 - Add a new CD')
    print('4 - Borrow book')
    print('5 - Return book')
    print('6 - Borrow CD')
    print('7 - Return CD')
    print('8 - Request book')
    print('9 - Print all details')
    print('99 - Exit program')
    print
    print('Enter your menu choice: ')

def main():
    Finish= False
    nextborrowerid=1
    nextbookid=1
    nextcdid=1

    while Finish ==False:
        menu()
        menuchoice = int(input())
        if menuchoice == 1:
            bname = input('name:')
            email = input('email address:')
            borrowerid = nextborrowerid
            nextborrowerid = nextborrowerid+1
            borrower = Borrower(bname,email,borrowerid)
        elif menuchoice == 2:
            title=input('title:')
            author = input('author:')
            itemid=nextbookid
            nextbookid = nextbookid+1
            book= Book(title,author,itemid)
        elif menuchoice == 3:
            title = input('title:')
            artist = input('artist:')
            itemid = nextcdid
            nextcdid = nextcdid + 1
            cd = CD(title, artist, itemid)
        elif menuchoice == 4:
            borrowerid = input('Borrower ID:')
            itemid = input('book id:')
            Book.Requestby(itemid,borrower)







B = Book("bitch","ken",11)

B.PrintDetails()
