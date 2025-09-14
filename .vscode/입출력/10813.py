n,m = map(int,input().split())
basket = [i for i in range(1,n+1)]
for _ in range(m):
    i,j = map(int,input().split())
    a = basket[i-1]
    b = basket[j-1]
    basket[j-1] = a
    basket[i-1] = b
for i in range(n):
    print(basket[i],end= " ")