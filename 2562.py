num=[]

for _ in range(9):
    num.append(int(input()))
    
maxN=num[0]
index=0
for i in range(1,9):
    if(maxN<num[i]):
        maxN=num[i]
        index = i
        
print(maxN)
print(index+1)
