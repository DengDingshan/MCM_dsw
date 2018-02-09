def find_path(maze , pos , end):
	mark(maze, pos)
	# print (pos, end)
	if pos == end :
		print (pos)
		return True 
	for i in range(4):
		nextp = pos[0]+dirs[i][0], pos[1]+dirs[i][1]
		if passable(maze, nextp):
			if find_path(maze, nextp, end):
				print (pos)
				return True
	return False

def mark(maze, pos):
	maze[pos[0]][pos[1]] = 2;
	return None 

def passable(maze, nextp):
	if maze[nextp[0]][nextp[1]] == 0:
		return True 
	else:
		return False

# maze = open ('maze.txt','r').read().split('\n')
maze = [[1,1,1,1,1,1,1],[1,0,0,0,0,0,1],[1,0,1,0,1,0,1],[1,0,0,1,1,0,1],[1,0,1,0,0,0,1],[1,0,0,1,1,0,1],[1,1,1,1,1,1,1]]
pos = (1,1)
end = (5,5)
dirs = [[-1,0],[1,0],[0,1],[0,-1]]
find_path(maze,pos,end);

# print (maze)