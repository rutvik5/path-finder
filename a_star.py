import heapq
import random

def main():
	n = 5
	p = FindPath(n)
	print('Start')
	p.print_grid()
	print()
	print('Output')
	p.a_star()

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

class FindPath:
	def __init__(self, n):
		# builds the grid and initializes it with Points
		self.grid = self.build_grid(n)

		# initializes start and end points
		self.start = self.grid[0][0]
		self.end = self.grid[-1][-1]
		
		# sets heuristic values for all points on the grid
		self.set_heuristic_val()
		# initializes start and end points
		self.init_std_points()
		# min-heap that includes all points to be processed
		self.openset = []
		# includes points that are finished to be processed
		self.closedset = set()
		# maintains the path from start to end
		self.came_from = {}
		#add start point in the min_heap 
		heapq.heappush(self.openset, (self.start.f, 0, 0))	

	def set_heuristic_val(self):
		# euclidean distance to find hval
		for row in range(len(self.grid)):
			for col in range(len(self.grid[0])):
				self.grid[row][col].h = (row - len(self.grid))**2 + (col - len(self.grid[0]))**2

	def init_std_points(self):
		# initializes g and f values for start
		self.start.g = 0
		self.start.f = self.start.h

		# overrides value for start and end to not be an obstacle
		self.start.val = 1
		self.end.val = 1

	def print_path(self):
		# prints final path from end to start
		curr = self.end
		while curr in self.came_from:
			curr.val = 1
			curr = self.came_from[curr]
		self.print_grid()
	
	def a_star(self):
		while self.openset:
			# smallest f-val from all the points to be processed
			fval, row, col = heapq.heappop(self.openset)
			point = self.grid[row][col]
			# base-condition when point == end
			if point == self.end:
				self.print_path()
				print()
				print('Done!')
				return

			# add curr_point to closedSet
			self.closedset.add(point)
			# 8 directions
			neighbors = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

			for nei in neighbors:
				x = point.row + nei[0]
				y = point.col + nei[1]

				if x >= 0 and x < len(self.grid) and y >= 0 and y < len(self.grid[0]) and self.grid[x][y].val != -1:
					tmp_g = point.g + self.dist(point, self.grid[x][y])
					# if the dist from start to nei via curr_point is less, update values
					if tmp_g < self.grid[x][y].g:
						self.came_from[self.grid[x][y]] = point
						self.grid[x][y].g = tmp_g
						self.grid[x][y].f = self.grid[x][y].g + self.grid[x][y].h

						if self.grid[x][y] not in self.closedset:
							heapq.heappush(self.openset, (self.grid[x][y].f, x,y))
		print('End cannot be reached')

	def dist(self, src, dest):
		# weight of the edge from source to dest
		# currently all weights are 1
		return 1

	def print_grid(self):
		for row in range(len(self.grid)):
			for col in range(len(self.grid)):
				print(self.grid[row][col].val, end = '\t')
			print()

	def build_grid(self,n):
		# builds a n * n - grid matrix with the given dimension
		grid = [[Point(row, col) for col in range(n)] for row in range(n)]
		return grid

if __name__ == '__main__':
	main()