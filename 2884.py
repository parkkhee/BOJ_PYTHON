H, M= map(int,input().split())
m=M-45
if(m<0):
    if(H==0):
        H=23
        M=60+m
    else:
        H=H-1
        M=60+m
else:
    M=m
    
print (H,M)
