x=int(input())
y=list(map(int,input().split()))
y.sort()
for i in range(0,x):
  print(y[i],end="")
