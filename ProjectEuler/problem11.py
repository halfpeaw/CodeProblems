import sys
sys.path.append("../SupportFunctions/")
import EulerSupport

#Grid is a 2d array of elements
def findLargest(grid):
  length = len(grid[0])
  height = len(grid)
  #Make sure all rows are equal in size
  for row in grid:
    if len(row) != length:
      print("Rows are not equal length")
      exit()
  #Cycle through each item, since random grid must brute force solution
  #Alg is 0(n^2)
  greatestProd = 0
  for y in range(0,height):
    for x in range(0,length):
      if (x <= length-4):
        greatestProd = max(grid[y][x] * grid[y][x+1] * grid[y][x+2] * grid[y][x+3],greatestProd)
      if (y <= height - 4):
        greatestProd =  max(grid[y][x] * grid[y+1][x] * grid[y+2][x] * grid[y+3][x],greatestProd)
      if (y <= height - 4 and x < length-4): 
        greatestProd = max(grid[y][x] * grid[y+1][x+1] * grid[y+2][x+2] * grid[y+3][x+3],greatestProd)
      if (y <= height - 4 and x >= 3):
        greatestProd = max(grid[y][x] * grid[y+1][x-1] * grid[y+2][x-2] * grid[y+3][x-3], greatestProd)
  print("Result: " + str(greatestProd))

if __name__ == "__main__":
	print("Problem 11")
	print("What is the greatest product of four adjacent numbers in any direction (up, down, left, right, or diagonally) in the 2020 grid?")
	filePath = "./InputFiles/gridP11.txt"
	grid = EulerSupport.parseUnicodeSepFile(filePath, True)
	findLargest(grid)