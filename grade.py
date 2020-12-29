marks=int(input("Enter your marks"))
if marks>=80:
    print("a grade")
else:
    if marks<80 and marks>=60:
        print("B grade")
    elif marks>=50 and marks<60:
        print("C grade")
    elif marks>=45 and marks<50:
        print("D grade")
    elif marks>=25 and marks<45:
        print("E grade")
    elif marks<25:
        print(F grade)

