a1,a2=map(int,input().split())
xx=list(map(int,input().split()))
count=0
if(len(xx)==a1):
 for i in xx:
  if(i==a2):
   count+=1
 print(count) 
