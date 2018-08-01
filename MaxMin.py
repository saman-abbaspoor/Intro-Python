Input=input('Please Enter Your Set of Numbers:')

if Input.find(',')!=-1:
    Numbers=Input.split(',')
else:
    Numbers=Input.split(' ')

Dataset=list()
for Number in Numbers:
    Number=int(Number)
    Dataset.append(Number)

Maximum=max(Dataset)
Minimum=min(Dataset)
