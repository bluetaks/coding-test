n = int(input())
files = {}

for i in range(n):
    name, ex = input().split('.')
    
    if ex in files:
        files[ex] += 1
    
    else: files[ex] = 1

result = sorted(files.items())
for i in result:
    print(i)