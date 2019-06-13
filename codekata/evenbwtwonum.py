x,y=map(int,input().split())
if(x<y):
  for j in range(x+1,y,1):
    if(j%2==0):
     print(j,end='')
