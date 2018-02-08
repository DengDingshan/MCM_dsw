class SStack():
	def __init__(self):
		self._elems = []

	def is_empty(self):
		return self._elems == []

	def top(self):
		if self._elems == []:
			raise StackUnderflow("in SStack.top()")
		return self._elems[-1]

	def push (self, elem):
		self._elems.append(elem)

	def pop(self):
		if self._elems == []:
			raise StackUnderflow("in SStack.pop()")
		return self._elems.pop()

def maze_solver(maze, start, end):
	if start == end :
		print (start)
		return 
	st = SStack()
	mark (maze, start)
	st.push ((start, 0))
	while not st.is_empty():
		pos, nxt = st.pop()
		for i in range(nxt, 4):
			nextp = (pos[0] + dirs[i][0], pos[1] + dirs[i][1])
			if nextp == end:
				print_path (end, pos, st)
				return 
			if passable(maze, nextp):
				st.push ((pos, i+1))
				mark (maze, nextp)
				st.push ((nextp, 0))
				break 
	print ("No path found.")

def print_path (end, pos, st):
	print (st._elems, pos, end )

def mark(maze, pos):
	maze[pos[0]][pos[1]] = 2;
	return None 

def passable(maze, nextp):
	if maze[nextp[0]][nextp[1]] == 0:
		return True 
	else:
		return False

maze = [[1,1,1,1,1,1,1],[1,0,0,0,0,0,1],[1,0,1,0,1,0,1],[1,0,0,1,1,0,1],[1,0,1,0,0,0,1],[1,0,0,1,1,0,1],[1,1,1,1,1,1,1]]
pos = (1,1)
end = (5,5)
dirs = [[-1,0],[1,0],[0,1],[0,-1]]
maze_solver(maze, pos, end)