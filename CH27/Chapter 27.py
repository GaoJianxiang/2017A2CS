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



class borrower:
    def __init__(self,borrowerName,emailAddress,borrowerID):
        self.__borrowerName = borrowerName
        self.__emailAddress = emailAddress
        self.__borrowerID = borrowerID
        self.__itemsOnLoan = 0

    def __repr__(self):
        return "Borrower: \n Name: %s;\n Addr: %s;\n ID: %s;\n LoanNo: %d;\n" %(self.__borrowerName, self.__emailAddress, self.__borrowerID, self.__itemsOnLoan)

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
        print(self)



B = Book("bitch","ken",11)

B.PrintDetails()
