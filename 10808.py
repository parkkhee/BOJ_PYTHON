x=input()
cnt=[0]*26

for i in x:
    cnt[ord(i)-97]+=1

print(*cnt)
