fhand=open('romeo.txt', 'r')
Dic=dict()

for Line in fhand:
    Words=Line.split()
    for Word in Words:
        Dic[Word]=Dic.get(Word, 0)+1

print(Dic)
