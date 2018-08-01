fhand=open('mbox-short.txt','r')

Dic=dict()

for Line in fhand:
    if Line.startswith('From '):
        Words=Line.split()
        Sender=Words[1]
        Dic[Sender]=Dic.get(Sender, 0)+1

BigSender=0
BigNumber=0

for Sender,NumEmails in Dic.items():
    if NumEmails > BigNumber:
        BigSender=Sender
        BigNumber=NumEmails

print(BigSender, BigNumber)
