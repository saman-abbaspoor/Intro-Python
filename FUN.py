def computepay(h,r):
    if h<40:
        payment=(h*r)
    elif h>40:
        payment=(40*r)+(h-40)*1.5*r
    return payment

hrs = input("Enter Hours:")
hrs=float(hrs)
Rate = input("Enter Rate:")
Rate=float(Rate)
p = computepay(hrs,Rate)
print("Your Payment is:", p)
