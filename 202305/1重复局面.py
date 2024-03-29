n = int(input())
chess = {}  #创建一个字典，其中的值都是唯一的
for i in range(n):
    temp = ''               #创建一个空的字符串
    for j in range(8):
        temp += input()     #字符串的+操作
    if temp not in chess:
        chess[temp] = 1
    else:
        chess[temp] += 1
    print(chess[temp])