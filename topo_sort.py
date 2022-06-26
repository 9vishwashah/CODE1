from collections import defaultdict
class Graph:
	def __init__(s,v):
		s.graph = defaultdict(list) 
		s.V = v 
	def addEdge(s,u,v):
		s.graph[u].append(v)
	def topologicalSortUtil(s,v,vis,st):
		vis[v] = True
		for i in s.graph[v]:
			if vis[i] == False:
				s.topologicalSortUtil(i,vis,st)
		st.insert(0,v)
	def topologicalSort(s):
		vis = [False]*s.V
		st =[]
		for i in range(s.V):
			if vis[i] == False:
				s.topologicalSortUtil(i,vis,st)
		print (st)
g= Graph(6)
g.addEdge(5, 2);
g.addEdge(5, 0);
g.addEdge(4, 0);
g.addEdge(4, 1);
g.addEdge(2, 3);
g.addEdge(3, 1);
print ("Following is a Topological Sort of the given graph")
g.topologicalSort()
