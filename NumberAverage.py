Sum=0
Count=0
while True:
    Number=input("Number:")
    if Number=="Done":
        break
    try:
        Num=float(Number)
    except Exception:
        print("Sorry, Please Enter a Number.")

    Sum=Sum+Num
    Count=Count+1


print("Your Average is:", Sum/Count)
