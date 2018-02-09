def find_path(maze, pos, end, br):
	mark(maze, pos, br)
	# print (pos, end, br)
	if pos == end :
		print (pos)
		return True 
	for i in range(5):
		nextp = nextposition(pos, br, i)
		if passable(maze, nextp, br):
			if br :
				br = False
			else :
				br = True
			# print maze
			if find_path(maze, nextp, end, br):
				print (pos)
				return True
	return False


def nextposition(pos, br, i):
	if not br :
		return (pos[0]+dirs[i][0], pos[1]+dirs[i][1])
	if br :
		return (pos[0]-dirs[i][0], pos[1]-dirs[i][1])


def mark(maze, pos, br):
	if br and maze[pos[0]][pos[1]] == 0 :
		maze[pos[0]][pos[1]] = 1;
		return None

	if not br and maze[pos[0]][pos[1]] == 0:
		maze[pos[0]][pos[1]] = 2;
		return None

	if maze[pos[0]][pos[1]] != 0:
		maze[pos[0]][pos[1]] = 3
		return None 


def passable(maze, nextp, br ):
	if nextp[0]<4 and nextp[0]>-1 and \
		nextp[1]<4 and nextp[1]>-1:
		if maze[nextp[0]][nextp[1]] == 0 or \
			(maze[nextp[0]][nextp[1]] == 2 and not br) or \
			(maze[nextp[0]][nextp[1]] == 1 and br) :
			return True 
		else:
			return False


maze = [[0,3,3,0],[0,0,3,0],[0,3,0,0],[0,3,3,0]]
pos = (3,3)
end = (0,0)
dirs = [[2,0],[1,1],[0,2],[1,0],[0,1]]
br = True
find_path(maze, pos, end, br)