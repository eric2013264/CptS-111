CR = float(input("What is the crank length: "))
RW = float(input("Enter the rear wheel radius: "))

crank_wheel_ratio = CR/RW

SP = float(input("Enter the number of teeth on the sproket: "))
CH = float(input("Enter the number of teeth on the chainring: "))

gear_ratio = SP/CH

final = crank_wheel_ratio * gear_ratio
print("The final ratio is: ",final)