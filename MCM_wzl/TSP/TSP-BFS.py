import copy

def get_down(c_s):
	summ = 0;
	for i in range(len(c_s)):
		c_s[i].sort()
		summ = c_s[i][0] + c_s[i][1] + summ 
	return summ / 2

def get_up(graph,used):
	summ = 0; pos = 0; temp = 0;
	for j in range(len(graph)-1):
		minlen = float('inf');
		used[pos] = False  
		temp = pos
		for i in range(len(graph[temp])):
			if (graph[temp][i] < minlen) and used[i] :
				minlen = graph[temp][i]
				pos = i
		print used,temp,pos,minlen
		summ += minlen
	return summ + graph[pos][0]

def solver(graph, used, pos, uplim, downlim):
	st = [0]
	for i in range(len(graph)-1) :
		st
	return s
	
def value(graph,st):
	val = 0
	for i in range(len(graph)):
	return 


graph = open ("TSP.txt","r").read().split('\n')

used = []
for i in range (len(graph)):
	graph[i]=graph[i].split(' ')
	for j in range (len(graph[i])):
		graph[i][j] = float(graph[i][j])
	used.append(True) 

c_s = copy.deepcopy(graph)
uplim = get_up(graph,used)
downlim = get_down(c_s)

print uplim,downlim
solver(graph, used, pos, uplim, downlim);