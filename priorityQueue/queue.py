from priorityqueue import priorityQueue
with open("priority.csv",'r+') as f:
    lines = [l for l in (line.strip() for line in f) if l]
    # lines = f.readlines()
    
Pqueue = []
for line in lines:
    if line[-1] == '\n':
        line = line[:-1]
    temp = line.split(',')
    temp[1] = int(temp[1])
    Pqueue.append(temp)
# print(Pqueue)

pQueue = priorityQueue()
for pair in Pqueue:
    pQueue.insert(pair)
f.close()

f = open("priority.csv",'w')
for pair in pQueue.arr:
    f.write((lambda x:x[0]+', '+str(x[1])+'\n')(pair))
f.close()