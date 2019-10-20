r=int(input("enter upper limt="))
m=int(input("enter lower limt="))      
for n in range(m,r+1):
    if n>1:
       for i in range(2,n):
            if(n%i)==0:
              break
       else:
        print(n)
            
