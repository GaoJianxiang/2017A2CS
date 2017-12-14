#S3 Opt3 Stefan Yuzhao Heng
NP = -1

class Node:
    def __init__(self):
        self.value = " "
        self.nextP = NP

class List:
    def __init__(self):
        self.FP = 0
        self.SP = 0
        self.record = []
        
        for i in range(10):
            newNode = Node()
            newNode.nextP = i+1
            self.record.append(newNode)
        newNode.nextP = NP
    
    def OutputNodes(self):
        CP = l.SP
        while CP != NP:
            print(l.record[CP].value,end=",")
            CP = l.record[CP].nextP
        print()

    def UpdateValue(self,index,temp):
        self.record[index].value = temp

l = List()
print(l.record)

l.UpdateValue(0,"I")
l.UpdateValue(1,"am")

l.OutputNodes()
