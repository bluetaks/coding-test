# a,b = map(int,input().split())
# big_num = max(a,b)
# small_num = min(a,b)
# common_divisor = []
# common_multiple = []
# for i in range(1,small_num+1):
#     if big_num % i == 0 and small_num % i ==0:
#         common_divisor.append(i)
# for i in range(big_num,(big_num*small_num)+1):
#     if i % big_num == 0 and i % small_num ==0:
#         common_multiple.append(i)
# print(max(common_divisor))        
# print(min(common_multiple))
# 시간초과 나의 버젼

# 유클리드 호제법을 사용한 풀이
a, b = map(int, input().split())
# 'x, y의 최대 공약수는 y, r의 최대 공약수와 같다'는 원리를 이용 이때 r = x % y
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
# x와 y의 최소공배수는 x*y // gcd(x,y)
def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))