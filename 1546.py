a= int(input())
b= list(map(int, input().split()))

sum=0

for i in range(a):
  sum = sum + b[i]/max(b)*100.0
print(sum/a)
