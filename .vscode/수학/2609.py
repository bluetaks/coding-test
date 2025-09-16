a,b = map(int,input().split())
if a > b:
    big_num = a
    small_num = b
else:
    big_num = b
    small_num = a
common_divisor = []
common_multiple = []
for i in range(1,small_num+1):
    if big_num % i == 0 and small_num % i ==0:
        common_divisor.append(i)
for i in range(big_num,(big_num*small_num)+1):
    if i % big_num == 0 and i % small_num ==0:
        common_multiple.append(i)
print(max(common_divisor))
print(min(common_multiple))
    