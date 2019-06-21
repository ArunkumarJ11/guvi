    
str=input()
digits=0
alphabet=0
for i in str:
 if(i.isdigits()):
   digits=1
 if(i.isalphabet()):
   alphabet=1
if(digits and alphabet):
  print('Yes')
else:
  print('No')
