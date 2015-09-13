# change.py
# A program to calculate the value of some change.

def main():
    print("Change Counter")
    print

    print("Enter the count of each of each coin count.")
    quarters = float(input("Quaters: ")) * 0.25
    dimes = float(input("Dimes: ")) * 0.10
    nickles = float(input ("Nickles: ")) * 0.05
    pennies = float(input ("Pennies: ")) * 0.01

    total = quarters + dimes + nickles + pennies

    print
    print("The total value of your change is $" + str(total))

main()
