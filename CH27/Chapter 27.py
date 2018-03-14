import datetime
class LibraryItem:
    def __init__(self,tittle, author, itemID,BorrowerID):
        self.__Tittle = tittle
        self.__Author__Artist = author
        self.__ItemID = itemID
        self.__OnLoan = False
        self.__BorrowerID = BorrowerID

        self.__DueDate = datetime.date.today()

    def GetAuthor(self):
        return(self.__Author__Artist)

    def GetItem(self):
        return(self.__ItemID)

    def GetLoan(self):
        return (self.__OnLoan)

    def GetBorrowerID(self):
        return(self.__BorrowerID)

    def GetDuedate(self):
        return (self.__DueDate)

    def GetTitle(self):
        return(self.__Tittle)

    def Borrowing(self,itemID,x):
        if x.GetItemsOnLoan() < 5:
            self.__OnLoan = True
            self.__BorrowerID = x.GetBorrowerID()
            self.__DueDate = self.__DueDate + datetime.timedelta(weeks=3)
            x.update(1)
        else:
            print('too many books on loan')



    def Returnning(self,itemID,x):
        self.__OnLoan = False
        x.update(-1)

    def PrintDetails(self):
        print(self.__IsRequested)



class Book(LibraryItem):
    def __init__(self,tittle,author,itemID):
        LibraryItem.__init__(self,tittle,author, itemID)
        self.__IsRequested = False
        self.__RequestedBy = 0

    def GetIsRequested(self):
        return(self.__IsRequested)

    def GetRequestBy(self):
        return(self.__IsRequested)

    def SetIsRequested(self,itemID,x):
        self.__IsRequested = True
        self.__RequestedBy = x.GetBorrowerID()

    def PrintDetails(self):
        print('Book Details: ')
        LibraryItem.PrintDetails(self)
        print(self.__IsRequested,';',self.__RequestedBy)

class CD(LibraryItem):
    def __init__(self,tittle,author,itemID):
        LibraryItem.__init__(self,tittle,author,itemID)
        self.__Genre = ""

    def GetGenre(self):
        return(self.__Genre)

    def SetGenre(self,g):
        self.__Genre = g

    def PrintDetails(self):
        print("CD Details: ")
        LibraryItem.PrintDetails(self)
        print(self.__Genre)


class Borrower(LibraryItem):
    def __init__(self,BorrowerID,email,BorrowerName):
        self.__BorrowerID = BorrowerID
        self.__email = email
        self.__BorrowerName = BorrowerName
        self.__itemsOnloan = 0

    def __repr__(self):
        return ("Borrower: \n Name: %s;\n Addr: %s;\n ID: %s;\n LoanNo: %d;\n")%(self.__borrowerName, self.__emailAddress, self.__borrowerID, self.__itemsOnLoan)

    def GetBorrowerName(self):
        return self.__BorrowerName

    def GetBorrowerID(self):
        return self.__BorrowerID

    def GetEmailAddress(self):
        return self.__email

    def GetItemsOnLoan(self):
        return self.__itemsOnloan

    def update(self, BorrowerName):
        self.__itemsOnloan = self.__itemsOnloan + BorrowerName

    def PrintDetails(self):
        print("Details of borrower: ")
        print(self.__BorrowerName,';',self.__BorrowerID,';',end='')
        print(self.__email,';',self.__itemsOnloan)

# Display Menu
def DisplayMenu():
    print('1, Add a new borrower')
    print('2, Add a new book')
    print('3, Add a new CD')
    print('4, Borrow book')
    print('5, Return book')
    print('6, Borrow CD')
    print('7, Return CD')
    print('8, Request book')
    print('9, Print all details')
    print('10, Exit program')

def main():
    Finish = False
    NextBorrowerID = 1
    NextBookID = 1
    NextCDID = 1

    while Finish == False:
        DisplayMenu()
        MenuChoice = int(input())
        if MenuChoice == 1:
            BName = input('Name: ')
            Email = input('email address: ')
            BorrowerID = NextBorrowerID
            NextBorrowerID += 1
            Borrower = Borrower(BorrowerID, Email, BName)

        elif MenuChoice == 2:
            Tittle = input("Tittle: ")
            Author = input('Author: ')
            ItemID = NextBookID
            NextBookID += 1
            Book = Book(Tittle,Author,ItemID)

        elif MenuChoice == 3:
            Tittle = input('Tittle: ')
            Artist = ('Artist: ')
            ItemID = NextCDID
            NextCDID += 1
            CD = CD(Tittle,Artist,ItemID)

        elif MenuChoice == 4:
            BorrowerID = input('Borrower: ')
            Email = input('Email: ')
            ItemID = input('Book ID: ')
            Book.Borrowing(ItemID, BorrowerID)

        elif MenuChoice == 5:
            BorrowerID = input('Borrower ID: ')
            ItemID = input('Book ID: ')
            Book.Returnning (ItemID,BorrowerID)

        elif MenuChoice == 6:
            BorrowerID = input('Borrower ID: ')
            ItemID = input('CD ID: ')
            CD.Borrowing(ItemID,BorrowerID)

        elif MenuChoice == 7:
            BorrowerID = input('Borrower ID: ')
            ItemID = input('CD ID: ')
            CD.Returnning (ItemID,BorrowerID)

        elif MenuChoice == 8:
            BorrowerID = input('Borrower ID')
            ItemID = input('Book ID: ')
            Book.SetIsRequested(ItemID,BorrowerID)







