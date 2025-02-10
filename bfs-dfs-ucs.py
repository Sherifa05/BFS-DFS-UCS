#BFS
graph={
    's':['A','B','D'],
    'A':['C'],
    'B':['D'],
    'C':['D','G'],
    'D':['G'],
    'G':[] 
}
def bfs(graph,start,goal):
    visited=[] 
    queue=[[start]] 
    while queue:
        path=queue.pop(0)
        node=path[-1]
        if node in visited:
            continue
        visited.append(node)
        if node==goal:
            return path
        else:
            adjacent_nodes=graph.get(node,[])
            for node2 in adjacent_nodes:
                new_path=path.copy()
                new_path.append(node2)
                queue.append(new_path)
solution=bfs(graph,'s','G')        
print('bfs solution is ',solution)


#DFS
graph={
    's':['A','B','D'],
    'A':['C'],
    'B':['D'],
    'C':['D','G'],
    'D':['G'],
}
def dfs(graph,start,goal):
    visited=[] 
    stack=[[start]] 
    while stack:
        path=stack.pop() 
        node=path[-1]
        if node in visited:
            continue
        visited.append(node)
        if node==goal:
            return path
        else:
            adjacent_nodes=graph.get(node,[])
            for node2 in adjacent_nodes:
                new_path=path.copy()
                new_path.append(node2)
                stack.append(new_path)
solution=dfs(graph,'s','G')        
print('dfs solution is ',solution)

#UCS
graph={
    's':[('A',2),('B',3),('D',5)],
    'A':[('C',4)],
    'B':[('D',4)],
    'C':[('D',1),('G',2)],
    'D':[('G',5)],
}
def path_cost(path):
    total_cost = 0
    for node, cost in path:
        total_cost += cost
    return total_cost  

def ucs(graph,start,goal):
    visited=[] 
    queue=[[(start,0)]] 

    while queue:
        queue.sort(key=path_cost) 
        path=queue.pop(0)
        node=path[-1][0]

        if node in visited:
            continue

        visited.append(node)

        if node==goal:
            return path
        else:
            adjacent_nodes=graph.get(node,[])
            for (node2,cost) in adjacent_nodes:
                new_path=path.copy()
                new_path.append((node2,cost))
                queue.append(new_path) 
                
solution=ucs(graph,'S','G')   
print(' ucs Solution is= ',solution) 
print('cost of path is= ',path_cost(solution)[0])          
