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



def maximum(surface, amap, top, bottom):
	for i in range(len(surface)-2):
		for j in range(len(surface)-2):
			if amap[i][j] == 0:
				if (surface[i+1,j] < surface[i,j])and\
					(surface[i,j+1] < surface[i,j])and\
					(surface[i-1,j] < surface[i,j])and\
					(surface[i,j-1] < surface[i,j]):
					top.append([i,j])
					amap[i+1,j] = 1; amap[i,j+1] = 1; amap[i-1,j] = 1; amap[i,j-1] = 1;
				if (surface[i+1,j] > surface[i,j])and\
					(surface[i,j+1] > surface[i,j])and\
					(surface[i-1,j] > surface[i,j])and\
					(surface[i,j-1] > surface[i,j]):
					bottom.append([i,j])
					amap[i+1,j] = 1; amap[i,j+1] = 1; amap[i-1,j] = 1; amap[i,j-1] = 1;	
	return 				 



def clear():
	global pos, end, dirs, top, bottom, summ
	summ = []
	pos = (1,1); 
	end = (5,5)
	dirs = [[-1,0],[1,0],[0,1],[0,-1]]
	top = []; bottom = []
	return 




def surface_solver(surface, amap, gather):
	# if start == end :
	# 	print (start)
	# 	return 
	for pos in gather:
		if amap[pos[0],pos[1]] == 0:
			# print pos, "aa"
			st = SStack()
			mark (amap, pos)
			summ.append(pos)
			st.push ((pos,0))
			while not st.is_empty():
				pos, nxt = st.pop()
				type(nxt)
				for i in range(nxt, 4):
					nextp = (pos[0] + dirs[i][0], pos[1] + dirs[i][1])
					if passable(surface, amap, nextp, pos):
						summ.append(nextp)
						st.push ((pos, i+1))
						mark (amap, nextp)
						st.push ((nextp, 0))
						 
	print ("No path found.")



def passable(surface, amap, nextp, pos):

	def in_range(nextp, surface):
		if 0 <= nextp[0] and len(surface)> nextp[0] and\
			0 <= nextp[1] and len(surface)> nextp[1]:
			return True
		else:
			return False

	if in_range(nextp, surface):
		# print nextp
		if (amap[nextp[0],nextp[1]] == 0):
			k = surface[nextp[0],nextp[1]]-surface[pos[0],pos[1]]
			if abs(k)<1e-4:
				return True
	return False



def mark(amap, pos):
	amap[pos[0],pos[1]] = 1;
	return 



import numpy as np
surface = np.loadtxt("surface.txt")
amap = np. zeros((512,512))
clear()
maximum(surface, amap, top, bottom)
amap = np. zeros((512,512))
surface_solver(surface, amap, top)
surface_solver(surface, amap, bottom)
print len(summ)
print len(top)+len(bottom)