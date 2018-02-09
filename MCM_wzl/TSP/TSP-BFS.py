import copy
class SQueue():
	def __init__(self, init_len=16):
		self._len = init_len 
		self._elems = [0]*init_len
		self._head = 0
		self._num = 0

	def is_empty(self):
		return self._num == 0

	def peek(self):
		if self._num == 0 :
			raise QueueUnderflow 
		return self._elems[self._head]

	def dequeue(self):
		if self._num == 0 :
			raise QueueUnderflow 
		e = self._elems[self._head]
		self._head = (self._head + 1 ) % self._len 
		self._num -= 1
		return e 

	def enqueue(self, e):
		if self._num == self._len :
			self._extend()
		self._elems[(self._head+self._num) % self._len] = e
		self._num += 1 

	def __extend(self):
		old_len = self._len
		self._len *= 2
		new_elems = [0]*self._len
		for i in range(old_len):
			new_elems[i] = self._elems[(self._head + i)% old_len]
		self. elems, self._head = new_elems, 0


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
		# print used,temp,pos,minlen
		summ += minlen
	return summ + graph[pos][0]

def solver(graph, pos, uplim, downlim):
	val = 0; nextp = [0]
	qu = SQueue()
	qu.enqueue([0])
	while not qu.is_empty():
		pos = qu.dequeue()
		# print pos
		for i in range(len(graph)):
			if not i in pos:
				nextp = pos + [i]
				val = value(graph,nextp)
				# print nextp,val
			if len(nextp) == len(graph) :
				print 'binggo', nextp, val
				return
			if val<=uplim and val>=downlim :
				qu.enqueue(nextp)
				# print 'a sign'
	print("No path.")
	return 
	
def value(graph,np):
	val = 0
	temp = float('inf')
	anti_np = []
	for i in range(len(graph)):
		if not i in np:
			anti_np.append(i)
	for i in range(len(np)-1):
		val += graph[np[i]][np[i+1]]*2.

	for i in anti_np:
		if temp>graph[np[0]][i]:
			temp = graph[np[0]][i]
	val += temp; temp = float('inf');

	for i in anti_np:
		if temp>graph[np[-1]][i]:
			temp = graph[np[-1]][i]
	val += temp

	for i in anti_np:
		temp = [];
		for j in range(len(graph)):
			temp.append(graph[i][j])
		temp.sort()
		val += temp[0] + temp[1] 
	return val/2.


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

# for i in range(len(graph)):
# 	used(i) = True 

print uplim,downlim

solver(graph, 1, uplim, downlim);