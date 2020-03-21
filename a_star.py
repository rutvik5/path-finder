def main():
	n = 5
	start = (0,0)
	end = (n-1,n-1)
	p = FindPath(n,start, end)
	p.print_grid()

class Point:
	def __init__(self, row, col):
		self.f = 0
		self.g = 0
		self.h = 0
		self.row = row
		self.col = col
		self.val = 0

class FindPath:
	def __init__(self, n, start, end):
		self.grid = self.build_grid(n, start, end)

	def print_grid(self):
		for row in range(len(self.grid)):
			for col in range(len(self.grid)):
				print(self.grid[row][col].val, end = '\t')
			print()

	def build_grid(self, n, start, end):
		grid = [[Point(row, col) for col in range(n)] for row in range(n)]
		grid[start[0]][start[1]].val = 1
		grid[end[0]][end[1]].val = 1
		return grid

if __name__ == '__main__':
	main()