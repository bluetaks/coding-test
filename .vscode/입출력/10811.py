n,m = map(int,input().split())
numbers = [k for k in range(1,n+1)]
temp = 0
for _ in range(m):
    i,j = map(int,input().split())
    temp = numbers[i-1:j]
    temp.reverse()
    numbers[i-1:j] = temp
for x in range(n):
  print(numbers[x],end=" ")