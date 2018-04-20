import time
from copy import deepcopy

class Node():
    #array contain nodes form root to leaf
    def __init__(self, a=[],cost=0):
        self.array=a
        self.cost=cost
    def depth(self):
        return len(self.array)

    def setcost(self,c):
        self.cost=c

    def getcost(self):
        return self.cost

    def endnode(self):
        return self.array[-1]

    def printNode(self):
        for i in self.array:
            for j in eval(i):
                print (str(j)+"\n")
            print ("\n")
    def expand(self,a):
            self.array.append(a)
    def hn(self):
        return h1(self.endnode())


# A*(star) algorithem
def greedy(root,goal):
    leaf = [root]
    expanded = []
    expanded_nodes=0
    while leaf:
        i = 0
        # print(leaf[i].depth())
        for j in range(1, len(leaf)):
            if leaf[i].hn() > leaf[j].hn():
                i = j
        path = leaf[i]
        leaf = leaf[:i] + leaf[i+1:]    #DELETE THE LEAF HAS BEEN SELECTED FROM LEAVES
        endnode = path.endnode()
        if endnode in expanded: continue
        for k in moves_possible(endnode):
            if k in expanded: continue
            x=deepcopy(path)
            x.expand(k)
            x.setcost(path.getcost()+1)
            leaf.append(x)
        # print(len(leaf))
        # for x in leaf:
        #     x.printNode()
        #     print("#######")
        expanded.append(endnode)
        expanded_nodes += 1
        if endnode == goal: break
    print(expanded_nodes)
    path.printNode()
    # print ("Expanded nodes:",expanded_nodes)
    return path
# ================================================================================
def moves_possible(m):
    output = []
    matrix = eval(m)
    i = 0
    while 0 not in matrix[i]: i += 1
    j = matrix[i].index(0)

    if j > 0:
      matrix[i][j], matrix[i][j-1] = matrix[i][j-1], matrix[i][j]   #left
      output.append(str(matrix))
      matrix[i][j], matrix[i][j-1] = matrix[i][j-1], matrix[i][j]

    if j < 2:
      matrix[i][j], matrix[i][j+1] = matrix[i][j+1], matrix[i][j]   #right
      output.append(str(matrix))
      matrix[i][j], matrix[i][j+1] = matrix[i][j+1], matrix[i][j]

    if i > 0:
      matrix[i][j], matrix[i-1][j] = matrix[i-1][j], matrix[i][j];  #up
      output.append(str(matrix))
      matrix[i][j], matrix[i-1][j] = matrix[i-1][j], matrix[i][j];

    if i < 2:
      matrix[i][j], matrix[i+1][j] = matrix[i+1][j], matrix[i][j]   #down
      output.append(str(matrix))
      matrix[i][j], matrix[i+1][j] = matrix[i+1][j], matrix[i][j]

    return output
# ================================================================
"""
READ FROM FILE
"""
current = []
for line in open('test4.txt').readlines():
    l1=line.split()
    l2=[]
    for x in l1:
        l2.append(int(x))
    current.append(l2)
current=str(current)

goal = str([[1, 2, 3],[4, 5, 6,], [7, 8, 0]])

def check(puzzle,e,row, col):
    for i in range(3):
        for j in range(3):
            if e == puzzle[i][j]:
                 return (abs(i - row) + abs(j - col))

def h1(endnode):
    x=0
    g=eval(goal)
    e=eval(endnode)
    # print(g[0][0])
    # print(endnode)
    for i in range(len(e)):
        for j in range(len(e[i])):
            x += check(g,e[i][j],i,j)
    return x


a=[]
a.append(current)
root=Node(a)
# h1(root.endnode())
# root.printNode()
# print(root.depth
start=time.time()

path = greedy(root,goal)
# path.printNode()
end=time.time()
total=end-start
print ("time  = :",total)
