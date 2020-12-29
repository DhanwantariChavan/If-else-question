present=int(input("Number of clsses held"))
absent=int(input("Nuber of classes attended"))
attended=(present/float(absent))*100
print("Attended is",attended)
if attended>=75:
    print("You are allowed to sit in exam ")
else:
    print("Sorry you are not allowed)
    