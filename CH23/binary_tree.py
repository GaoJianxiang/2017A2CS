#Binary Tree Initialize & Insert
#S3 Opt3 Stefan Yuzhao Heng

nullP = -1

class Node:
    def __init__(self):
        self.listV = "N"
        self.leftP = nullP
        self.righP = nullP

class Tree:
    def __init__(self):
        self.rootP = nullP
        self.freeP = 0
        self.record = []

        for i in range(10):
            newN = Node()
            newN.leftP = i+1
            self.record.append(newN)
        newN.leftP = nullP

    def OutputListPointer(self):
        print(self.rootP,self.freeP)

    def OutputRecord(self):
        for i in range(10):
            print("[",self.record[i].listV,self.record[i].leftP,self.record[i].righP,"]")

    def OutputList(self):
        currP = self.rootP
        print("[",end="")
        while currP != nullP:
            print(self.record[currP].listV,end=",")
            currP = self.record[currP].righP
        print("]")

    def InsertValue(self,newV):
        if self.freeP != nullP:
            newP = self.freeP
            self.freeP = self.record[newP].leftP
            self.record[newP].listV = newV
            self.record[newP].leftP = nullP
            self.record[newP].righP = nullP
            if self.rootP == nullP:
                self.rootP = newP
            else:
                currP = self.rootP
                while currP != nullP:
                    prevP = currP
                    if newV < self.record[currP].listV:
                        turnL = True
                        currP = self.record[currP].leftP
                    elif newV > self.record[currP].listV:
                        turnL = False
                        currP = self.record[currP].righP
                    else:
                        print("Value inserted")
                if turnL:
                    self.record[prevP].leftP = newP
                else:
                    self.record[prevP].righP = newP

    def FindValue(self,requV):
        currP = self.rootP
        while currP != nullP and self.record[currP].listV != requV:
            if self.record[currP].listV > requV:
                currP = self.record[currP].leftP
            else:
                currP = self.record[currP].righP
        return currP

t = Tree()

t.InsertValue(3)
t.InsertValue(2)
t.InsertValue(5)
t.InsertValue(8)
t.OutputRecord()
print(t.FindValue(2),t.FindValue(5))