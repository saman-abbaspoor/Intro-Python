FileName=input('Please Enter Your Filename:')
try:
    fhand=open(FileName)
except:
    print('Your File Does Not Exist.')
    quit()

Count=0
Total=0
for line in fhand:
    if line.find('X-DSPAM-Confidence')!=-1:
        Position=line.find(':')
        Range=line[Position+1:]
        Range=float(Range)
        Total=Total+Range
        Count+=1

print('Average spam confidence:', Total/Count) 
