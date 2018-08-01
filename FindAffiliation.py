fhand=open('mbox-short.txt')

for Line in fhand:
    if Line.startswith('From '):
        Array=Line.split()
        Array2=Array[1].split('@')
        print(Array2[1])

print('\nWell Done')

fhand=open('mbox-short.txt')

for Line in fhand:
    if Line.startswith('From '):
        Pos1=Line.find('@')
        Pos2=Line.find(' ', Pos1)
        print(Line[Pos1+1:Pos2])
