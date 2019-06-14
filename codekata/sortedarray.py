a=int(input())
c=list(map(int,input().split()))
c.sort()
for i in range(0,a):
  print(c[i],end="")
