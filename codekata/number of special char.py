x=input()
num=0
for i in range(len(x)):
  if(x[i].isdigit() or x[i].isalpha() or x[i]==' '):
    continue
  else:
    num=num+1
print(num)
