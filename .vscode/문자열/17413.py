import sys
strInput = list(sys.stdin.readline().rstrip())
strInput.append(' ')
strInput2 = []
tagFlag = False
for i in strInput:
    if i == '<':
        while strInput2:
            print(strInput2.pop(), end='')
        tagFlag = True
        print('<', end='')
    elif i == '>':
        tagFlag = False
        print('>', end='')
    elif i == ' ':
        if tagFlag == True: 
            print(' ', end='')
        else:
            while strInput2:
                print(strInput2.pop(), end='')
            print(' ', end='')
    else:
        if tagFlag == True: 
            print(i, end='')
        else: strInput2.append(i)