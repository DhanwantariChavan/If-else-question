salary=int(input("How much salary do you have?"))
years=int(input("How many years of service you have done?"))
salary1=str(salary)
if years<5:
    print("You get salary₹"+salary1)
elif years>=5:
   salary2=int(salary1)
   salary3=5/100*salary
   salary4=salary+salary3
   salary5=str(salary4)
   print("You get salary of ₹"+salary5)
   print("You got 5%Bonus")