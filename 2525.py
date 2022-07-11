h,m = map(int,input().split())
pt = int(input())
rm =m+pt

if(rm>=60):
  h=h+(int(rm/60))
  rm = rm%60
  if(h>=24):
    h=h-24

print(h, rm)
