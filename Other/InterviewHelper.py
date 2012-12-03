def rotate(x):
  print (x)
  y = []
  for i in range(0,len(x[0])):
    y.append([0]*len(x))
  print(x)
  for i in range(0 ,len(x[0])):
    for j in range(0 ,len(x)):
      y[i][j] = x[(len(x)-j)-1][i]
  print(y)

if __name__ == "__main__":
  x = [[1,2],[3,4],[5,6]]
  rotate(x)
  
  #[1,2]
  #[3,4]   =>  [5,3,1]
  #[5,6]	     [6,4,2]
  
  #[1,3,5]
  #[2,4,6]
