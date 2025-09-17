text = input()
result = ""
if "__" in text or text[0].isupper() or text[0] == "_" or text[-1] == "_":
    print("Error!")
elif '_' in text:
    if not text.replace("_", "").islower():
        print("Error!")
    else:
        text = text[0] + text.title()[1:]
        print(text.replace("_", ""))
else:
    a = list(text)
    for i in range(1, len(a)):
        if a[i].isupper():
            a[i] = "_" + a[i].lower()
    print("".join(a))