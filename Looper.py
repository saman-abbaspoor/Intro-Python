fhand=open('mbox-short.txt', 'r')

Count=0
for Line in fhand:
    if Line.startswith('From '):
        Words=Line.split()
        Count+=1
        print(Words[1])


print('There were', Count, 'lines in the file with From as the first word')
