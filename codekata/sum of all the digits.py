    
abc=int(input())
s=0
while(abc>0):
  r=abc%10
  s=s+r
  abc=abc//10
print(s)
