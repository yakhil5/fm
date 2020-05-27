e=float(input("Equity : "))
d=float(input("Debt : "))
tc=float(input("Tax Rate : "))
t=e+d

# Cost of Equity 
print("How do you want Equity Valued ?")
print("    1.Dividend Capitalization Model")
print("    2.Capital Asset Pricing Model(CAPM)")
opt=input()
if opt=="1" :
    do=float(input("Dividend per Share (DPS) : "))
    eo=float(input("Earnings per Share (EPS) : "))
    gd=float(input("Growth rate of Dividends : "))
    ke=(do/eo)+(gd/100)
else:
    rm=float(input("Market Risk Premium : "))
    rf=float(input("Risk free rate : "))
    beta=float(input("Beta : "))
    ke=(rf/100)+beta*((rm-rf)/100)
ke=ke
# Cost of Debt
if opt=="1":
    rf=float(input("Risk free rate : "))
cs=float(input("Credit Spread : "))
kd=((rf+cs)*(100-tc))/100

# Weighted Average Cost of Capital
wacc=(e/t)*ke+(d/t)*kd

# Output
print(" ")
print(" ")
print("     Weighted Average Cost of Capital")
print("     --------------------------------")
print(" ")
print("Cost of Equity : ",ke)
print("Cost of Debt : ",kd)
print("Weighted Average Cost of Capital : ",wacc)
