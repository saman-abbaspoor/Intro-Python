fhand=open('romeo.txt','r')
List=list()

for Line in fhand:
    Words=Line.split()
    for Word in Words:
        if Word not in List:
            List.append(Word)

List.sort()
print(List)
