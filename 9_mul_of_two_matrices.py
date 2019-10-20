x=[[5,8,9,],[8,9,0],[7,8,9]]
y=[[5,6,7],[8,9,7],[8,9,7]]
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(y[0])):
     for k in range(len(y)):
        result[i][j] += x[i][k]*y[k][j]
        
for r in result:
        print(r)
