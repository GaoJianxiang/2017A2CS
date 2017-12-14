#Kevin Gao
nullPtr = -1
class listNode:
    def __init__(self):
        self.value = ""
        self.nextPtr = nullPtr

class List():
    def __init__(self):
        self.freePtr = 0
        self.startPtr = nullPtr
        self.records = []
        newNode = None
        for i in range (0,10):
            newNode = listNode()
            newNode.nextPtr = i + 1
            self.records.append(newNode)
        newNode.nextPtr = nullPtr
    def insertNode(self, newItem):
        if self.freePtr != nullPtr:
            self.newPtr = self.freePtr
            self.records[self.freePtr].value = newItem
            self.freePtr = self.records[self.freePtr].nextPtr
            thisnodePtr = self.startPtr
            prevnodePtr = nullPtr
            while thisnodePtr != nullPtr and self.records[thisnodePtr].value < newItem:
                prevnodePtr = thisnodePtr
                thisnodePtr = self.records[thisnodePtr].nextPtr
            if prevnodePtr == nullPtr:
                self.records[self.newPtr].nextPtr = self.startPtr
                self.startPtr = self.newPtr
            else:
                self.records[self.newPtr].nextPtr = self.records[prevnodePtr].nextPtr
                self.records[prevnodePtr].nextPtr = self.newPtr
    def findNode(self,dataItem):
        currentPtr = self.startPtr
        while currentPtr != nullPtr and self.records[currentPtr].value != dataItem:
            currentPtr = self.records[currentPtr].nextPtr
        print (currentPtr)
    
    def deleteNode(self,dataItem):
        thisNodePtr = self.startPtr
        while thisNodePtr!=nullPtr and self.records[thisNodePtr].value != dataItem:
            prevnodePtr = thisNodePtr
            thisNodePtr = self.records[thisNodePtr].nextPtr
        if thisNodePtr != nullPtr:
            if thisNodePtr == self.startPtr:
                self.startPtr=self.records[self.startPtr].nextPtr
            else:
                self.records[prevnodePtr].nextPtr=self.records[thisNodePtr].nextPtr
        self.records[thisNodePtr].Ptr = self.freePtr
        self.freePtr=thisNodePtr

    def printList(self):
        currentPtr = self.startPtr
        while currentPtr != nullPtr:
            print(self.records[currentPtr].value, end=" ")
            currentPtr = self.records[currentPtr].nextPtr
        




l = List()
l.insertNode(2)
l.insertNode(9)
l.insertNode(1)
l.insertNode(3)
l.insertNode(6)
l.insertNode(4)
l.deleteNode(3)
l.findNode(9)

l.printList()
