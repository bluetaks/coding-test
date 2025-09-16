n = int(input())
start , end = input().split("*")
for _ in range(n):
    text = input()
    if len(start)+len(end) > len(text):
        print("NE")
    elif text.startswith(start) and text.endswith(end):
        print("DA")
    else:
        print("NE")