class SQueue():
	def __init__(self, init_len=8):
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

def maze_solver_queue(maze, start, end):
	if start == end:
		print ("Path Found.")
		return 
	qu = SQueue()
	mark (maze, start)
	qu.enqueue (start)
	while not qu.is_empty():
		pos = qu.dequeue()
		for i in range(4):
			nextp = (pos[0] + dirs[i][0],\
					pos[1] + dirs[i][1])
			if passable(maze, nextp):
				dic[nextp] = pos
				if nextp == end:
					print ("path found.")
					return 
				mark(maze, nextp)
				qu.enqueue(nextp)
	print("No path.")

def mark(maze, pos):
	maze[pos[0]][pos[1]] = 2;
	return None 

def passable(maze, nextp):
	if maze[nextp[0]][nextp[1]] == 0:
		return True 
	else:
		return False

dic={}
maze = [[1,1,1,1,1,1,1],[1,0,0,0,0,0,1],[1,0,1,0,1,0,1],[1,0,0,1,1,0,1],[1,0,1,0,0,0,1],[1,0,0,1,1,0,1],[1,1,1,1,1,1,1]]
pos = (1,1)
end = (5,5)
dirs = [[-1,0],[1,0],[0,1],[0,-1]]
maze_solver_queue(maze, pos, end)
print dic