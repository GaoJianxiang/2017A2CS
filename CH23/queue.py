# S3C2 Kevin
class Node():
    def __init__(self):
        self.Next=None
        self.value=None
        self.endP=None

class Run():
    def __init__(self):   
        self.NullPtr=-1
        self.StartPtr=self.NullPtr
        self.FreePtr=0
        self.List=[0]*10
        self.index=0
        for i in range(10):
            self.List[i]=Node()
            self.List[i].NextPtr=i+1
        self.List[9].NextPtr=self.NullPtr

    def InsertNode(self,data):
        if self.index==10:
            print("error")
        elif self.StartPtr==self.NullPtr:
            self.StartPtr = 0
            self.List[0].NextPtr = self.NullPtr
            self.List[self.FreePtr].value = data
            self.FreePtr = 1
        else:
            d=self.StartPtr
            NewPtr = self.FreePtr
            self.List[self.FreePtr].value = data
            self.FreePtr = self.List[self.FreePtr].NextPtr
            self.List[NewPtr].NextPtr = NewPtr-1
            self.StartPtr = NewPtr

    def SearchNode(self,data):
        for i in range(self.index-1):
            if data>self.List[self.StartPtr].value:
                self.StartPtr = self.List[self.StartPtr].NextPtr
            if data == self.List[self.StartPtr].value:
                return self.StartPtr
        print("error")

    def PrintList(self):
        s=self.StartPtr
        while s != self.NullPtr:
            print(self.List[s].value, end=" ")
            s = self.List[s].NextPtr
        print("")
    def DeleteNode(self):
        thisnodePtr = self.StartPtr
        while self.List[thisnodePtr].NextPtr != self.NullPtr:
            prevnodePtr = thisnodePtr
            thisnodePtr = self.List[thisnodePtr].NextPtr
        self.List[prevnodePtr].NextPtr = self.NullPtr
        self.List[thisnodePtr].NextPtr = self.FreePtr
        self.FreePtr = thisnodePtr
l=Run()
l.InsertNode(1)
l.InsertNode(3)
l.InsertNode(2)
l.InsertNode(5)
l.PrintList()
l.DeleteNode()
l.PrintList()

