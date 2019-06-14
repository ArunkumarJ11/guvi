    
x,y=map(int,input().split())
for n in range(x+1,y):
  temp=n
  sum=0
  while(temp!=0):
    x=temp%10
    sum=sum+x**3
    temp=temp//10
  if(n==sum):
    print(n,end=' ')
