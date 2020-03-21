import heapq
import collections

def main():
	n = 5
	p = FindPath(n)
	p.print_grid()
	p.a_star()

class Point:
	def __init__(self, row, col):
		self.f = float('inf')
		self.g = float('inf')
		self.h = 0
		self.row = row
		self.col = col
		self.val = 0

class FindPath:
	def __init__(self, n):
		self.grid = self.build_grid(n)
		self.start = self.grid[0][0]
		self.end = self.grid[-1][-1]
		self.set_heuristic_val()
		self.init_start()
		self.openset = []
		self.closedset = set()
		self.came_from = {}

		heapq.heappush(self.openset, (self.start.f, 0, 0))	

	def set_heuristic_val(self):
		# euclidean distance to find hval
		for row in range(len(self.grid)):
			for col in range(len(self.grid[0])):
				self.grid[row][col].h = (row - len(self.grid))**2 + (col - len(self.grid[0]))**2

	def init_start(self):
		self.start.val = 1
		self.start.g = 0
		self.start.f = self.start.h

	def print_path(self):
		curr = self.end
		while curr in self.came_from:
			curr.val = 1
			curr = self.came_from[curr]
		print()
		self.print_grid()
	
	def a_star(self):
		while self.openset:
			# smallest f-val from all the points to be processed
			fval, row, col = heapq.heappop(self.openset)
			point = self.grid[row][col]
			# base-condition when point == end
			if point == self.end:
				self.print_path()
				print('Done!')
				return

			# add curr_point to closedSet
			self.closedset.add(point)
			# 8 directions
			neighbors = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

			for nei in neighbors:
				x = point.row + nei[0]
				y = point.col + nei[1]

				if x >= 0 and x < len(self.grid) and y >= 0 and y < len(self.grid[0]):
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
		grid = [[Point(row, col) for col in range(n)] for row in range(n)]
		return grid

if __name__ == '__main__':
	main()