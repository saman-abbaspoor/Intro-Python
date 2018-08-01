fhand=open('mbox-short.txt', 'r')

for Line in fhand:
    if Line.startswith('From '):
        Pos1=Line.find('@')
        Pos2=Line.find(' ', Pos1)
        print(Line[Pos1+1: Pos2])
