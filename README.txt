Contents:
1)Structure:
2)Brief description of each algorithm.
3) The logic of each function implemented and the purpose of each function.
 
Note: The termination time of the algorithm is currently set as 1 hour (PERIOD_OF_TIME = 3600), this can be increased if needed.
First, we need to run the file search.py by passing the arguments algo (BFS or A_Star or RBFS ) and filename. 
The contents of the file are read, and the values of longitude and latitude of the initial state are extracted. Based on the algo value entered that algorithm will be executed on that latitude and longitude values.

Functions:
1) Node Class:
The node class has five elements:
 i)First element is a list of 30 integers Which has the 30 latitudes of the the given state.(.lat)
ii) Has list of 30 integers which has 30 longitudes of given state(.lon)
iii) cost: Is the g(n) to reach that state.
iv) f:  Is used to calculate the f value
v) actions: has all the sequence of actions which has led to the current state from the starting state

2) Dec_E: When an action is performed on equator such that the values of the longitudes are reduced by 30. It also appends the action Dec_E to  node.actions . So we have track of what actions led to the current state.

3) Inc_E: When an action is performed on equator such that the values of the longitudes are increased by 30. It also appends the action Inc_E to  node.actions . So we have track of what actions led to the current state.
4) Inc_long_0: When an action is performed on 0-180 longitude such that the values of the latitudes are increased by 30. It also appends the action Inc_long_0 to  node.actions . So we have track of what actions led to the current state.
5) dec_long_0: When an action is performed on 0-180 longitude such that the values of the latitudes are decrease by 30. It also appends the action dec_long_0 to  node.actions . So we have track of what actions led to the current state.
6) dec_long_90: When an action is performed on 90-270 longitude such that the values of the latitudes are decrease by 30. It also appends the action dec_long_90 to  node.actions . So we have track of what actions led to the current state.
7) inc_long_90: When an action is performed on 90-270 longitude such that the values of the latitudes are increase by 30. It also appends the action inc_long_90 to  node.actions . So we have track of what actions led to the current state.

8) is_Goal : takes the current state and the goal state and compares all the latitudes and longitudes  of the two states if they are equal then goal is found and based on flag value the path is printed. Flag value is used so that path is not printed multiple times.

9) Stringify: converts the current state latitude and longitude values from two lists into a single string.
10) Unstringify: Converts back the single string to two lists separating longitude and latitude values of a node.

11) Heuristic_calc: Calculates the heuristic value of h(n) for a current state and returns the h(n) value.

BFS:
i) Creating a queue named frontier to keep track of the frontier nodes and added the state_start node to frontier.
ii) Child_parent is a dictionary containing the stringify(child_node) as key and stringify(parent-node) as its value.
iii) We run a loop which exits when it either reaches goal state or the frontier is empty.
iv) In that we perform all six actions on parent and check whether the resultant child is the goal state. If it is not the goal state then we add it to frontier queue and we mark it as visited by adding it into the dictionary. If it is goal state  then we print the sequence of actions that led to goal state (in the is_Goal function by sending the flag as 0) and we exit the loop.
v) Every time we add a new node to the frontier we check the value of max_queue_size is less than the present queue size and we update the max_queue_size.
vi) So each time the first node in the queue is getting popped and all the six actions are being performed on the node and we repeat this.
vii) We keep track of the nodes_expanded by counting the number of times the loop runs.
viii) Path variable of type list has all the nodes of the path that leads to the goal state from starting state. We get this  by referring to the dictionary.
ix) And the depth is nothing but the number of nodes in the path list-1. 

Prints path_length ,number of nodes expanded, sequence of steps that led to the current state and size of the queue.

A_Star
i) We store the frontier of A* in a priority queue and insert start_state into the queue.
ii) We create a dictionary with Stringify(child) as key and Stringify(parent) as value to keep track of visited nodes.
iii) We then execute a loop which exits when priority queue is empty or the goal state is reached. All the 6 actions are performed and we check whether it is already visited(by checking in the keys of dictionary) if it is not visited then we check whether it is the goal, if it is not goal then it is added to frontier.
iv) The priority queue uses g(n)+h(n) function as the priority function.
v) We update the max_queue_size with queue.size if max_queue_size is less. And If the goal state is reached we print the sequences of actions.
vi) Nodes expanded will be the number of times the loop is being executed.
vii) And the path contains all the nodes from start to goal state which are on that path.

RBFS:
       
i) First, we call the RBFS function on the start_state with f_value as g(n)+h(n) and f_limit as inf.
ii) Then we store all the successors in  a heap  which are obtained by doing all the six actions.
iii) Then we update the f_value  of all the successors whose f_value is less than f_value of parent with parent f_value.
iv) If there are no successors, we return the value of f_limit as infinity else we heapify the heap
v) Now we run a loop which breaks when the goal state is found or the smallest value of f_value is greater than f_limit.
vi) We take the node with minimum f_value and compare it with f_limit . If f_value is greater then we return 0 and best.f .(which is used to update the f_value of the parent ).Else, we find the second best  and store it as alternative.
vii) We call the RBFS function with node as best_node(node with min f_value ) and f_limit value as  minimum of f_limit of its parent and alternative f_value.
viii) We update the f_value of the best node once the recursive function returns value.
ix) Result has the sequence of nodes from start state to goal state which are on that path.
x) Here queue size is the available nodes for expansion at a given instance so if we are at a depth d then the available nodes for expansion will be 5 for every node in that path so it will be 5*n.
xi) Nodes expanded at a given instance will be the number of recursive calls happened before this recursive call execution has started.






