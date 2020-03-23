# A* path finding algorithm

The repo contains a visualization of the A* algorithm using p5 library written in Python. The default problem includes a n*n grid where an agent has to travel from top-left to bottom right (This can be changed by updating the values for start, end). The contents of this repo are as follows:

- a_star.py : CLI version on A* algorithm. Contains n*n grid with following values
  - 0: available path
  - -1: obstacle
  - 1: path to be followed
  
- visualization.py : Implements visualization of the above program. The colors for each cell means as follows:
  - black: obstacles
  - green: potential path cells
  - red: path cells that should not be followed
  - blue: path cells to be followed

## Requirements
  
  - python (https://www.python.org/downloads/)
  - p5 for python (https://pypi.org/project/p5/)

## Output

<img src="https://github.com/rutvik5/path-finder/blob/master/output.PNG">

