text = input().upper()
text_list = list(set(text))
text_count = []
for i in text_list:
    text_count.append(text.count(i))
if text_count.count(max(text_count)) > 1:
    print("?")
else:
    print(text_list[(text_count.index(max(text_count)))])