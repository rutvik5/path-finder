from p5 import *
import heapq
import random

# set the size of grid
n = 20

class Point:
	def __init__(self, row, col):
		self.f = float('inf')
		self.g = float('inf')
		self.h = 0
		self.row = row
		self.col = col
		self.val = 0
		# adds obstacles at random points with a certain prob
		# sets the value of every obstacle to -1
		if random.randint(1, 10) < 3:
			self.val = -1
	# colors the point with the given rgb values
	def show(self, r,g,b):
		fill(r,g,b)
		# if point is an obstacle, paint it black
		if self.val == -1:
			fill(0)
		stroke(0)
		rect((self.row * w, self.col * h), w, h, mode="CORNER")


def build_grid(n):
	# builds a n * n - grid matrix with the given dimension
	grid = [[Point(row, col) for col in range(n)] for row in range(n)]
	return grid

def set_heuristic_val(grid):
	# euclidean distance to find hval
	for row in range(len(grid)):
		for col in range(len(grid[0])):
			grid[row][col].h = (row - end.row)**2 + (col - end.col)**2

def init_std_points(start, end):
	# initializes g and f values for start
	start.g = 0
	start.f = start.h

	# overrides value for start and end to not be an obstacle
	start.val = 1
	end.val = 1

def dist(src, dest):
	# weight of the edge from source to dest
	# currently all weights are 1
	return 1

def create_path(end):
	# colors the path from end to start
	curr = end
	path.append(curr)
	while curr in came_from:
		path.append(curr)
		curr = came_from[curr]

# builds the grid and initializes it with Points
grid = build_grid(n)

# initializes start and end points
start = grid[0][0]
end = grid[-1][-1]

# sets heuristic values for all points on the grid
set_heuristic_val(grid)

# initializes start and end points
init_std_points(start, end)

# min-heap that includes all points to be processed
openset = []
# includes points that are finished to be processed
closedset = set()
# maintains the path from start to end
came_from = {start:None, }

#set of points on the path to be colored in the end
path = []

#add start point in the min_heap 
heapq.heappush(openset, (start.f, 0, 0))

def setup():
	print('Start')
	size(500, 500)
	global w 
	global h
	w = width / n
	h = height / n

def draw():
	background(0)
	# colors all the points based on its properties
	for row in range(n):
		for col in range(n):
			grid[row][col].show(255,255,255)

	for fval, row, col in openset:
		grid[row][col].show(0, 255, 0)

	for point in closedset:
		point.show(255, 0, 0)

	for point in path:
		point.show(0, 0, 255)


	if openset:
		# smallest f-val from all the points to be processed
		fval, row, col = heapq.heappop(openset)
		point = grid[row][col]
		# base-condition when point == end
		if point == end:
			create_path(end)
			no_loop()
			print('Done!')

		# add curr_point to closedSet
		closedset.add(point)
		# 8 directions
		neighbors = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

		# checks all neighbors to find lowest f-values
		for nei in neighbors:
			x = point.row + nei[0]
			y = point.col + nei[1]

			if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]) and grid[x][y].val != -1:
				tmp_g = point.g + dist(point, grid[x][y])
				# if the dist from start to nei via curr_point is less, update values
				if tmp_g < grid[x][y].g:
					came_from[grid[x][y]] = point
					grid[x][y].g = tmp_g
					grid[x][y].f = grid[x][y].g + grid[x][y].h

					if grid[x][y] not in closedset:
						heapq.heappush(openset, (grid[x][y].f, x,y))
	else:
		print('End cannot be reached')
		no_loop()

if __name__ == '__main__':
	run()


