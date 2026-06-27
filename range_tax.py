# Task 1: Check whether a number is in the range 1 to 100

num = int(input("Enter a number: "))

if num >= 1 and num <= 100:
    print("The number is within the range (1 to 100).")
else:
    print("The number is not within the range (1 to 100).")


# Task 2: Salary Tax Calculator

salary = float(input("\nEnter your salary: "))

if salary <= 250000:
    tax = 0

elif salary <= 500000:
    tax = (salary - 250000) * 0.05

elif salary <= 1000000:
    tax = (250000 * 0.05) + (salary - 500000) * 0.07

else:
    tax = (250000 * 0.05) + (500000 * 0.07) + (salary - 1000000) * 0.10

print("Tax to be paid =", tax)