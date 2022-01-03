class priorityQueue:
    def __init__(self):
        self.arr = []
        self.len = 0
        self.dict = {}
    def swap(self, i, j ):
        self.dict[self.arr[j][0]] = i
        self.dict[self.arr[i][0]] = j
        temp = self.arr[i]
        self.arr[i]= self.arr[j]
        self.arr[j] = temp

    def heapify(self,index):
        l = 2*index+1
        r = l+1
        if l>=self.len:
            return
        elif r == self.len:
            if self.arr[l][1]>self.arr[index][1]:
                self.swap(index,l)
        else:
            largest = l if self.arr[l][1] > self.arr[r][1] else r
            if self.arr[largest][1] > self.arr[index][1]:
                self.swap(index,largest)
                self.heapify(largest)

    def heapsort(self):
        for i in range(self.len//2-1,-1,-1):
            self.heapify(i)

    def upheapify(self):
        index = self.len -1
        parent = (index-1)//2
        while parent>=0:
            if self.arr[parent][1] < self.arr[index][1]:
                self.swap(index,parent)
                index = parent
                parent = (parent-1)//2
            else:
                break
    def insert(self, nodeList):
        self.arr.append(nodeList)
        self.dict[nodeList[0]] = self.len
        self.len+=1
        self.upheapify()
    
    def dequeue(self):
        if self.len==1:
            self.arr = []
            self.len = 0
            self.dict = {}
        elif self.len == 0:
            raise IndexError("funcking idiot, there's nothing to dequeue")
        else:
            del self.dict[self.arr[0][0]]
            self.arr[0] = self.arr.pop()
            self.len -= 1
            self.heapify(0)

    def delete(self,key):
        index = self.dict[key]
        del self.dict[key]
        if index == self.len -1:
            self.arr.pop()
            self.len -= 1
        else:
            self.arr[index] = self.arr.pop()
            self.len -= 1
            self.heapify(index)    
            

if __name__ == '__main__':

    myQ = priorityQueue()

    myQ.insert(["q",8])
    myQ.insert(["a",4])
    myQ.insert(["w",6])
    myQ.insert(["x",10])
    print(myQ.arr)
    print(myQ.dict)
    myQ.delete('a')
    print(myQ.arr)
    print(myQ.dict)
    print(myQ.len)
        

        
