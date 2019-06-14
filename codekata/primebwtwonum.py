c,d=map(int,input().split())
for k in range(c+1,d):
  if k>1:
    for l in range(2,k):
      if(k%l==0):
        break
    else:
      print(k,end=' ')
