# To build an interest calculator for XYZ bank. It calculates interest for both your investment and house loans.
import math


print("Welcome to XYZ Bank's interest calculator. Refer the options below to continue"
      +"\n"+"Investment- to calculate the amount of interest you will earn for your investment"
      +"\n"+"Bond- to calculate the amount you will have to pay on a home loan"
      +"\n"+"Choose one of the above two options to start calculating")
calc=input("Your option:")
calc= calc.lower()
print("Fill in the details below to continue")    # calculations continue based on the users choice 

if (calc== "investment"):
    P=int(input("Enter your deposit amount in GBP:"))
    r=int(input("Enter the interest rate given:"))/100       # Since the interest rate is in percentage, we divide it by 100 for the calculations.
    t=(int(input("Enter your investment period in years:")))
    interest=input("Choose and enter 'simple' or 'Compound' interest to continue:")
    interest=interest.lower()
    print("Lets calculate the"+" "+interest+" "+"interest")
    if (interest== "simple"):
      A=P*(1+r*t)
      print(interest+"interest ="+" "+str(A))       # Calculating the simple interest.
    else:
      A=P*math.pow((1+r),t)
      print(interest+"interest ="+" "+str(A))       # Calculating the Compound interest.

elif calc== "bond":
    P=int(input("Enter the present value of house:"))
    i=int(input("Enter the interest rate given:"))
    n=int(input("Enter the repayment tenure:"))
    repayment= (i*P)/(1-(1+i)**(-n))
    print("Repayment amount="+" "+str(repayment))
else: 
    print("error: result not found")               # inputs other than bond or investment will result in this output.






