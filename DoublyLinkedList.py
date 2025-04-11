
class Node:
    
    def __init__(self,data):
        self._data = data
        self._prev = None
        self._next = None

    def getPrev(self):
        return self._prev
    
    def setPrev(self,node):
        self._prev = node
    
    def getNext(self):
        return self._next
    
    def setNext(self,node):
        self._next = node
        
    def getData(self):
        return self._data

class DSA:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def addFirst(self,value):
        node = Node(value)
        
        if self.head == None:
            self.head = self.tail = node
        else:
            
            self.head.setNext(node)
            node.setPrev(self.head)
            self.head = node
        
    def addLast(self,value):
        node = Node(value)
        
        if self.tail == None:
            self.tail = self.head = node
        else:
            self.tail.setPrev(node)
            node.setNext(self.tail)
            self.tail = node
            
    def remove(self,index):
        
        current = self.tail
        i = 0
        while(current):
            if index == i:
                prev = current.getPrev()
                nextt = current.getNext()
                if prev:
                    prev.setNext(nextt)
                else:
                    self.tail = self.tail.getNext()
                
                if nextt:
                    nextt.setPrev(prev)
                else:
                    self.head = self.head.getPrev()
                
                return
            
            else:
                current = current.getNext()
                i = i + 1
    
    def getLength(self):
        current = self.tail
        length = 0
        while(current):
            length = length + 1
            current = current.getNext()
            
        return length
            
    def printContent(self,):
        current = self.tail
        while(current):
            print("{}".format(current.getData()),end="")
            current = current.getNext()
            if current:
                print("-> ",end="")
                
        print()
            
dsa = DSA()
dsa.addFirst(1)
dsa.addFirst(10)
dsa.addFirst(11)
dsa.addLast(18)
dsa.addFirst(92)
dsa.addLast(100)
dsa.printContent()
dsa.remove(5)
dsa.addFirst(250)
dsa.printContent()
dsa.remove(0)
dsa.addLast(450)
dsa.printContent()

    
    


