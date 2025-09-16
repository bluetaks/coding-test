n = int(input())
for i in range(n):
    text = input()
    text = text.replace(" ","")
    
    text1 = set(text)
    text2 = list(text1)
    text2_count = []
    
    for j in range(len(text2)):
        text2_count.append(text.count(text2[j]))
        m = max(text2_count)
    if text2_count.count(m)>1:
        print("?")
    else:
        m2 = text2_count.index(m)
        print(text2[m2])