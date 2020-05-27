def fv():
    x=input("Enter Present Value : ")
    r=input("Enter Discounting Rate : ")
    t=input("Enter time period : ")
    x=float(x)
    r=float(r)
    t=float(t)
    fv=x*((1+(r/100))**t)
    print("The future value of",x,"is",fv)

def pv():
    x=input("Enter Future Value : ")
    r=input("Enter Discounting Rate : ")
    t=input("Enter time period : ")
    x=float(x)
    r=float(r)
    t=float(t)
    pv=x/((1+(r/100))**t)
    print("The present value of",x,"is",pv)
    
print("This calculator can convert present values to future values vice vesa")
print("Choose option")
print("     1: Convert Present values into future values")
print("     2: Convert Future values into present values")
opt=input()
if opt == "1":
    fv()
elif opt == "2" :
    pv()
else:
    print("Invalid Option")

