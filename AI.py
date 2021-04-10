import copy
import sys
#Name Abdul Aziz Muhammad Ibrahim Isa
#Roll No P17-6143
# Artificial Intelligence Assignment # 1
sys.setrecursionlimit(99999)
class TreeNode:
    goalx =[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,'_']]
    goal = [['_',1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
    goalFlag, Treelevel, level, cost = 0,0,0,0
    queue = []
    hashtable = []
    def __init__(self, x):
        self.state = x
        self.right = None
        self.left = None
        self.up = None
        self.down = None
                
    def flatten(self,input):
        new_list = []
        for i in input:
            for j in i:
                new_list.append(j)
        return new_list
    def blank_space(self,start):
        space, count = '_', 1
        for i in range(len(start)-1, -1, -1):
            if space in start[i]:
                if count % 2 != 0:
                    return True
                else:
                    return False
            count += 1
    #TreeNode.blank_space = blank_space
    def check_inversions(self,start):
        track = []
        inversions, count, max = 0,1, 16
        start = self.flatten(start)
        for i in range (0, len(start)):
            for j in range(1, max):
                if start[i] == '_':
                    break
                elif int(start[i]) > j:
                    if j not in track:
                        inversions += 1
                elif int(start[i]) == 1:
                    continue
            track.append(start[i])
           # print("inversions for ", start[i], " are ", inversions)
        if inversions % 2 == 0:
            return True
        else:
            return False
    #TreeNode.check_inversions = check_inversions
    def find(self,inp):
        for i in range(0, len(inp)):
            for j in range(0, len(inp[i])):
                if(inp[i][j] == '_'):
                    return[i, j]
    def traversal(self, temp):
        self.queue.append(temp.state)
       # print("state at Treelevel", self.Treelevel)
       # for i in temp.state:
         #   print(i)
        index = self.find(temp.state)
        if(temp.state == self.goalx or temp.state == self.goal):
            self.goalFlag = 1
            print("goal found")
            for i in self.queue:
                print(i)
            print("cost == no of moves == ",len(self.queue) - 1)
            sys.exit()
            return
        #if(Treelevel == level and goalFlag == 0):
        if(self.goalFlag == 1):
            return
        if(self.Treelevel < self.level):
                if(self.level - self.Treelevel == 1):
                    if(index[0] != 0):
                        #print("moving up")
                        #up child possible
                        st = copy.deepcopy(temp.state)
                        self.goalFlag = 2
                        st[index[0] - 1][index[1]],st[index[0]][index[1]] = st[index[0]][index[1]], st[index[0] - 1][index[1]]
                        if st not in self.hashtable:
                            self.hashtable.append(st)
                            temp.up = TreeNode(st)
                            self.Treelevel += 1
                            self.traversal(temp.up)
                            self.Treelevel -= 1
                    if(index[1] < 3):
                        #right child possible
                        #print("moving right")
                        st = copy.deepcopy(temp.state)
                        self.goalFlag = 2
                        st[index[0]][index[1] + 1],st[index[0]][index[1]] = st[index[0]][index[1]], st[index[0]][index[1] + 1]
                        if st not in self.hashtable:
                            self.hashtable.append(st)
                            temp.right = TreeNode(st)
                            self.Treelevel += 1
                            self.traversal(temp.right)
                            self.Treelevel -= 1        
                    if(index[1] != 0):
                        #print("moving left")
                        #left child possible
                        st = copy.deepcopy(temp.state)
                        self.goalFlag = 2
                        st[index[0]][index[1] - 1],st[index[0]][index[1]] = st[index[0]][index[1]], st[index[0]][index[1] - 1]
                        if st not in self.hashtable:
                            self.hashtable.append(st)
                            temp.left = TreeNode(st)
                            self.Treelevel += 1
                            self.traversal(temp.left)
                            self.Treelevel-= 1
                    
                    if(index[0] < 3):
                      #  print("moving down")
                        # down child possible 
                        st = copy.deepcopy(temp.state)
                        self.goalFlag = 2
                        st[index[0] + 1][index[1]],st[index[0]][index[1]] = st[index[0]][index[1]], st[index[0] + 1][index[1]]
                        if st not in self.hashtable:
                            self.hashtable.append(st)
                            temp.down = TreeNode(st)
                            self.Treelevel += 1
                            self.traversal(temp.down)
                            self.Treelevel -= 1
                    self.goalFlag = 0
                   # print("goal flag changed")
                else:
                    if(temp.up != None):
                        #print("moving up")
                        self.Treelevel += 1
                        self.traversal(temp.up)
                        self.Treelevel -= 1
                    if(temp.left != None):
                        #print("moving left")
                        self.Treelevel += 1
                        self.traversal(temp.left)
                        self.Treelevel -= 1
                    if(temp.right != None):
                        #print("moving right")
                        self.Treelevel += 1
                        self.traversal(temp.right)
                        self.Treelevel -= 1
                    if(temp.down != None):
                        #print("moving down")
                        self.Treelevel += 1
                        self.traversal(temp.down)
                        self.Treelevel -= 1
        if( self.goalFlag == 0):
            #print("inside")
            self.queue.clear()
            self.Treelevel = 0
            self.level += 1
            self.traversal(self)
        else:
            self.queue.pop()
            return
    def menu(self,start):
        if( self.blank_space(start) == self.check_inversions(start)):
            print("the start state can be solvable with goal state 1")
           # goalflag = 1
        else:
            print("the start state can be solvable with goal state 2")
            #goalflag = 2
            x = copy.deepcopy(self)
            self.hashtable.append(x.state)
        self.traversal(x)    
            

start, x = [], 0
for i in range(0, 4):
    new = []
    for j in range(0, 4):
        x = input("please insert the start state ranging from 1 - 15 and blankspace as _ ")
        if(x == '_'):
            new.append(x)
        else:
            new.append(int(x))
    start.append(new)
print(start)
t= TreeNode(start)
t.menu(start)
