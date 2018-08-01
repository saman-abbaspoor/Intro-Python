Score=input("Please Enter Your Score:")
S=float(Score)

if 0<S<1:
    if S>=0.9:
        print("A")
    elif S>=0.8:
        print("B")
    elif S>=0.7:
        print("C")
    elif S>=0.6:
        print("D")
    elif S<0.6:
        print("D")
else:
    print("Your score is out of range")
