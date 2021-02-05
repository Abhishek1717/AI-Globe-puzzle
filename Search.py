import queue
import copy
import gc
import heapq
from itertools import count
import sys
import time

Start=time.time()   # time to terminate after  1 hour
PERIOD_OF_TIME = 3600

class node:
    def __init__(self):
        self.lat=[0]*30
        self.lon=[0]*30
        self.cost=0
        self.f=0           ##for RBFS
        self.actions=[]    #sequence of actions that led to this state.
        
def dec_E(present):
    
    
    for i in range(30):
        if(present.lat[i]==90):
            if(present.lon[i]!=0):
                present.lon[i]=present.lon[i]-30
            else:
                present.lon[i]=330
    present.actions.append("dec_E")
                


def inc_E( present):
    
    
    for i in range(30):
        if(present.lat[i]==90):
            if(present.lon[i]!=330):
                present.lon[i]=present.lon[i]+30
            else:
                present.lon[i]=0
    present.actions.append("inc_E")
                
           
def inc_long_0(present):
    
    
    for i in range(30):
        if(present.lon[i]==0):
            present.lat[i]=present.lat[i]+30
            if(present.lat[i]==180):
                present.lon[i]=180
        elif(present.lon[i]==180):
            present.lat[i]=present.lat[i]-30
            if(present.lat[i]==0):
                present.lon[i]=0
    present.actions.append("inc_long_0")
 
def dec_long_0(present):
    
    
    for i in range(30):
        if(present.lon[i]==0):
            present.lat[i]=present.lat[i]-30
            if(present.lat[i]==-30):
                present.lon[i]=180
                present.lat[i]=30
        elif(present.lon[i]==180):
            present.lat[i]=present.lat[i]+30
            if(present.lat[i]==210):
                present.lon[i]=0
                present.lat[i]=150
    present.actions.append("dec_long_0")
 
def inc_long_90( present):
    
    
     for i in range(30):
        
        if(present.lon[i]==90):
            present.lat[i]=present.lat[i]+30
            if(present.lat[i]==180):
                present.lon[i]=180
        elif(present.lon[i]==270):
            present.lat[i]=present.lat[i]-30
            if(present.lat[i]==0):
                present.lon[i]=0
        elif(present.lon[i]==0 and present.lat[i]==0):
            present.lon[i]=90
            present.lat[i]=30
        elif(present.lon[i]==180 and present.lat[i]==180):
            present.lon[i]=270
            present.lat[i]=150
     present.actions.append("inc_long_90")
 
            
            
def dec_long_90(present):
    
     for i in range(30):
        if(present.lon[i]==90):
            present.lat[i]=present.lat[i]-30
            if(present.lat[i]==0):
                present.lon[i]=0
        elif(present.lon[i]==270):
            present.lat[i]=present.lat[i]+30
            if(present.lat[i]==180):
                present.lon[i]=180
        elif(present.lon[i]==180 and present.lat[i]==180):
            present.lon[i]=90
            present.lat[i]=150
        elif(present.lon[i]==0 and present.lat[i]==0):
            present.lon[i]=270
            present.lat[i]=30
     present.actions.append("dec_long_90")
 


def is_Goal(state_check,state_goal,flag):
    
    for i in range(30):
        if(state_check.lon[i]!=state_goal.lon[i] or state_check.lat[i]!=state_goal.lat[i] ):
            return False
    if(flag!=1):
        print(state_check.actions)
    return True


def stringify(state):
    result=""
    for i in range(30):
        result = result+str(state.lat[i])+"," + str(state.lon[i])+","
    return result

def unstringify(string_state):
    result =node()
    list_cord = string_state.split(",")
    for i in range(30):
        result.lat[i] = int(list_cord [2*i])
        result.lon[i] = int(list_cord [2*i + 1])
    return result





######## BREADTH FIRST SEARCH########################
def BFS(state_start,state_goal):
    frontier=queue.Queue()
    frontier.put(copy.deepcopy(state_start))
    nodes_expanded=0
    max_queue_size=1
    child_parent = {}
    child_parent[state_start] =1 
    
    
    while(not frontier.empty()):  
        
        if time.time() > Start + PERIOD_OF_TIME : 
            print("time limit of 1 hour exceeded")
            break
        
        nodes_expanded=nodes_expanded+1
        parent=frontier.get()
        
        org_parent=copy.deepcopy(parent)          # as parent gets modified inside dec_E need to do deep_copy of that
        dec_E(parent)
        if stringify(parent) not in child_parent.keys():
            child_parent[stringify(parent)]=stringify(org_parent)
            if(frontier.qsize()>max_queue_size):      
                max_queue_size=frontier.qsize()
            if is_Goal(parent,state_goal,0):
                break
            frontier.put(parent)
        
        parent=copy.deepcopy(org_parent)
        inc_E(parent)
        if stringify(parent) not in child_parent.keys():
            child_parent[stringify(parent)]=stringify(org_parent)
            if(frontier.qsize()>max_queue_size):
                max_queue_size=frontier.qsize()
            if is_Goal(parent,state_goal,0):
                break
            frontier.put(parent)
        
        parent=copy.deepcopy(org_parent)
        inc_long_0(parent) 
        if stringify(parent) not in child_parent.keys():
            child_parent[stringify(parent)]=stringify(org_parent)     
            if(frontier.qsize()>max_queue_size):
                max_queue_size=frontier.qsize()
            if is_Goal(parent,state_goal,0):
                break
            frontier.put(parent)
        
        parent=copy.deepcopy(org_parent)    
        dec_long_0(parent)
        if stringify(parent) not in child_parent.keys():
            child_parent[stringify(parent)]=stringify(org_parent)
            if(frontier.qsize()>max_queue_size):
                max_queue_size=frontier.qsize()
            if is_Goal(parent,state_goal,0):
                break
            frontier.put(parent)
        
        parent=copy.deepcopy(org_parent)
        inc_long_90(parent)
        if stringify(parent) not in child_parent.keys():
            child_parent[stringify(parent)]=stringify(org_parent)
            if(frontier.qsize()>max_queue_size):
                max_queue_size=frontier.qsize()
            if is_Goal(parent,state_goal,0):
                break
            frontier.put(parent)
        
        parent=copy.deepcopy(org_parent)
        dec_long_90(parent)
        if stringify(parent) not in child_parent.keys():
            child_parent[stringify(parent)]=stringify(org_parent)
            if(frontier.qsize()>max_queue_size):
                max_queue_size=frontier.qsize()
            if is_Goal(parent,state_goal,0):
                break
            frontier.put(parent)
        
        if(frontier.qsize()>max_queue_size):
            max_queue_size=frontier.qsize()
        
    print("nodes_expanded: "+str(nodes_expanded))    
    print("max_queue_size: "+ str(max_queue_size))
    
    depth=0
    path=[]
    path.append(parent)
    
    
    while(1):       ### path has sequence of nodes from state_start to goal state.
        
        if is_Goal(parent,state_start,1):
            break
        else:
            parent=unstringify(child_parent[stringify(parent)])
            path.append(parent)
     
    depth=len(path)-1       
    print("Path_length:"+ str(depth))
    

    
def heuristic_calc(current_state,state_goal):
    
    max_equ=0
    max_lon90=0
    max_lon0=0
    for i in range(30):
        
        if(state_goal.lat[i]==90):
            max_equ= max(max_equ,min(abs(state_goal.lon[i]-current_state.lon[i]),
                                     360-abs(state_goal.lon[i]-current_state.lon[i])))
        elif(state_goal.lon[i]==90 or state_goal.lon[i]==270):
            max_lon90= max(max_lon90,min(abs(state_goal.lat[i]-current_state.lat[i]),
                                     180-abs(state_goal.lat[i]-current_state.lat[i])))
        elif((state_goal.lon[i]==0 or state_goal.lon[i]==180) and state_goal.lat[i]!=0 ):
            max_lon0= max(max_lon0,min(abs(state_goal.lat[i]-current_state.lat[i]),
                                     180-abs(state_goal.lat[i]-current_state.lat[i])))
            
 
    return (max_equ+max_lon90+max_lon0)/30

    



###################################### A STAR ##########################################
 
def A_Star(state_start,state_goal):
    
    frontier=queue.PriorityQueue()
    unique = count()
    parent=copy.deepcopy(state_start)
    frontier.put((heuristic_calc(state_start,state_goal),next(unique),parent))
    parent.cost=0;
    max_queue_size=1
    
    child_parent = {}
    child_parent[stringify(state_start)]=1
    nodes_expanded=0
    gc_val=1
    
    while(not frontier.empty()):
        
        if time.time() > Start + PERIOD_OF_TIME :   #to exit after 1 hour
            print("time limit of 1 hour exceeded")
            break
        
        if(gc_val%100000==0):
           gc.collect()
        gc_val+=1
        x=frontier.get()
        nodes_expanded+=1
        parent=x[2]
       
        
        org_parent=copy.deepcopy(parent)
        dec_E(parent)
        if stringify(parent) not in child_parent.keys():
            child_parent[stringify(parent)]=stringify(org_parent)   
            if is_Goal(parent,state_goal,0):
                break
            parent.cost=org_parent.cost+1
            frontier.put((heuristic_calc(parent,state_goal)+parent.cost,next(unique),parent))
        if(frontier.qsize()>max_queue_size):
                max_queue_size=frontier.qsize()
        
        parent=copy.deepcopy(org_parent)
        inc_E(parent)
        if stringify(parent) not in child_parent.keys():
            child_parent[stringify(parent)]=stringify(org_parent)   
            if is_Goal(parent,state_goal,0):
                break
            parent.cost=org_parent.cost+1
            frontier.put((heuristic_calc(parent,state_goal)+parent.cost,next(unique),parent))
        if(frontier.qsize()>max_queue_size):
                max_queue_size=frontier.qsize()
                
        parent=copy.deepcopy(org_parent)
        inc_long_0(parent)
        if stringify(parent) not in child_parent.keys():
            child_parent[stringify(parent)]=stringify(org_parent)   
            if is_Goal(parent,state_goal,0):
                break
            parent.cost=org_parent.cost+1
            frontier.put((heuristic_calc(parent,state_goal)+parent.cost,next(unique),parent))
        if(frontier.qsize()>max_queue_size):
                max_queue_size=frontier.qsize()
        
        parent=copy.deepcopy(org_parent)
        dec_long_0(parent)
        if stringify(parent) not in child_parent.keys():
            child_parent[stringify(parent)]=stringify(org_parent)   
            if is_Goal(parent,state_goal,0):
                break
            parent.cost=org_parent.cost+1
            frontier.put((heuristic_calc(parent,state_goal)+parent.cost,next(unique),parent))   
        if(frontier.qsize()>max_queue_size):
                max_queue_size=frontier.qsize() 
        
        parent=copy.deepcopy(org_parent)
        inc_long_90(parent)
        if stringify(parent) not in child_parent.keys():
            child_parent[stringify(parent)]=stringify(org_parent)   
            if is_Goal(parent,state_goal,0):
                break
            parent.cost=org_parent.cost+1
            frontier.put((heuristic_calc(parent,state_goal)+parent.cost,next(unique),parent)) 
        if(frontier.qsize()>max_queue_size):
                max_queue_size=frontier.qsize()
                
        parent=copy.deepcopy(org_parent)
        dec_long_90(parent)
        if stringify(parent) not in child_parent.keys():
            child_parent[stringify(parent)]=stringify(org_parent)   
            if is_Goal(parent,state_goal,0):
                break
            parent.cost=org_parent.cost+1
            frontier.put((heuristic_calc(parent,state_goal)+parent.cost,next(unique),parent))    
        
        if(frontier.qsize()>max_queue_size):
                max_queue_size=frontier.qsize()
        
    print("nodes_expanded:" + str(nodes_expanded))
    print("max_queue_size:"+ str(max_queue_size))

    path=[]
    path.append(parent)
   
    
    while(1):
        
        if is_Goal(parent,state_start,1):
            break
        else:
            parent=unstringify(child_parent[stringify(parent)])
            path.append(parent)
     
    depth=len(path)-1       
    print("path_length: "+str(depth))
    
    

##################################    RBFS  ########################################

RBFS_nodes_expanded=0
max_queue_size=0
max_size=0
path2=[]
RBFS_depth=0
def RBFS(state_start,state_goal,f_limit):
    
    global max_queue_size
    global max_size
    global RBFS_nodes_expanded
    unique = count()
    
    if time.time() > Start + PERIOD_OF_TIME :    ## to exit after 1 hour
        print("nodes expanded:"+str(RBFS_nodes_expanded))
        print("Max_elements in queue RBFS:"+str(max_size))
        print("time limit of 1 hour exceeded")
        sys.exit()
    
    parent=copy.deepcopy(state_start)
    global path2
    path2.append(stringify(parent))
    
    if is_Goal(parent,state_goal,0):
        path=[]
        path.append(parent)
        return path,1
    
    
    RBFS_nodes_expanded+=1
    successors=[]
    
    max_queue_size+=5
    
    if(max_queue_size>max_size):
        max_size=max_queue_size
    org_parent=copy.deepcopy(parent)
    dec_E(parent)
    parent.cost=org_parent.cost+1
    
    parent.f=max(parent.cost+heuristic_calc(parent,state_goal),org_parent.f)
    heapq.heappush(successors,(parent.f,next(unique), parent))
    
    parent=copy.deepcopy(org_parent)
    inc_E(parent)
    parent.cost=org_parent.cost+1
    parent.f=max(parent.cost+heuristic_calc(parent,state_goal),org_parent.f)
    heapq.heappush(successors,(parent.f,next(unique), parent))
    
    parent=copy.deepcopy(org_parent)
    inc_long_0(parent) 
    parent.cost=org_parent.cost+1
    parent.f=max(parent.cost+heuristic_calc(parent,state_goal),org_parent.f)
    heapq.heappush(successors,(parent.f,next(unique), parent))
    
    parent=copy.deepcopy(org_parent)
    dec_long_0(parent)
    parent.f=max(parent.cost+heuristic_calc(parent,state_goal),org_parent.f)
    heapq.heappush(successors,(parent.f,next(unique), parent))
    
    parent=copy.deepcopy(org_parent)
    inc_long_90(parent)
    parent.cost=org_parent.cost+1
    parent.f=max(parent.cost+heuristic_calc(parent,state_goal),org_parent.f)
    heapq.heappush(successors,(parent.f,next(unique), parent))
    
    parent=copy.deepcopy(org_parent)
    dec_long_90(parent)
    parent.cost=org_parent.cost+1
    parent.f=max(parent.cost+heuristic_calc(parent,state_goal),org_parent.f)
    heapq.heappush(successors,(parent.f,next(unique), parent))
    
    heapq.heapify(successors)
    if len(successors)==0:
        return 0,float('inf')
    
    while(1):
        
        heapq.heapify(successors)
        x,x1,best= heapq.heappop(successors)
        
        if best.f> f_limit:
            return 0,best.f
        heapq.heapify(successors)
        alternative,x2,x3=successors[0]
        heapq.heapify(successors)
        heapq.heappush(successors,(x,x1,best))
        result,best.f=RBFS(best,state_goal,min(f_limit,alternative))
        
        max_queue_size-=5
        l1=list(successors[0])
        l1[2].f=best.f         ## successors are collection of tuples since tuples are immutable we convert it into list to update value
        l1[0]=best.f            
        successors[0]=tuple(l1)
        
        if  result!=0:
            result.append(org_parent)  ## result contains the sequence of nodes from start state to goal state along the path
            
            return result,1

    
    

    
########################### MAIN function ####################   

algo=sys.argv[1]
filename=sys.argv[2]         
file = open(filename, "r")

f1=file.readlines()
state_start=node()
state_goal=node()
k=0;

for i in f1:
    state = i.split("(")
    if(len(state) > 1):
        state_start.lat[k]=int(state[2].split(")")[0].split(",")[0])
        state_start.lon[k]=int(state[2].split(")")[0].split(",")[1])
        state_goal.lat[k]=int(state[3].split(")")[0].split(",")[0])
        state_goal.lon[k]=int(state[3].split(")")[0].split(",")[1])
        k=k+1

if(algo=="BFS"):     
   print("###Running BFS###")
   BFS(state_start,state_goal)
elif(algo=="AStar"):
    print("###Running A_Star###")
    A_Star(state_start,state_goal)
elif(algo=="RBFS"):
    print("###Running RBFS###")
    Path,x=RBFS(state_start,state_goal,float("inf"))
    print("nodes expanded:"+str(RBFS_nodes_expanded))
    print("Path_length:"+str(len(Path)-1))
    print("Max_elements in queue RBFS:"+str(max_size))
else:
    print("Enter either BFS or AStar or RBFS")
