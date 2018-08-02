#Written By Saman Abbaspoor, sabbaspoor.neusci@gmail.com

Input1=input("Please Enter Your First List:")
Input2=input("Please Enter Your Second List:")

FirstList=Input1.split(',')
SecondList=Input2.split(',')

N=len(FirstList)
if len(FirstList)>len(SecondList):
    N=len(SecondList)

FinalList=list()
for ii in range(N):
    if len(FirstList)<len(SecondList):
        if FirstList[ii] in SecondList:
            FinalList.append(FirstList[ii])
    else:
        if SecondList[ii] in FirstList:
            FinalList.append(SecondList[ii])

print(FirstList)
print(SecondList)
print(FinalList)
