n=int(input("enter the number of term are need="))
a=int(input("enter the first initialize number="))
b=int(input("enter the second initialize number="))
if(n>0 and n!=1):
 print(a)
 print(b)
elif(n!=0):
 print(a)
while(n-2>=0):
 c=a+b
 a=b
 b=c
 print(c)
 n=n-1


 




 
