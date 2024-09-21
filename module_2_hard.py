import random
def Unique(ListForClear):
    ClearList = []
    for i in ListForClear:
        if i not in ClearList:
            ClearList.append(i)
    return ClearList

def Extract(ListForExtract):
    ExtractedListStr = ''
    for i in ListForExtract:
        for j in i:
            ExtractedListStr = str(ExtractedListStr) + str(j)
    return ExtractedListStr

n = random.randint(3, 20)
Password = []
for i in range(1, n):
    for j in range(1, n):
        if i == j:
            continue
        elif n % (i + j) == 0:
            Password.append([i, j])
for i in range(len(Password)):
    Password[i].sort()
Password = Unique(Password)
Password = Extract(Password)
print(f'Ключом к цифре {n} будет {Password}')