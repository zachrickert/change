# change.py
# A program to calculate the value of some change.

def main():
    print("Change Counter")
    print

    print("Enter the count of each of each coin count.")
    quarters = input("Quaters: ") * 0.25
    dimes = input("Dimes: ") * 0.10
    nickles = input ("Nickles: ") * 0.05
    pennies = input ("Pennies: ") * 0.01

    total = quarters + dimes + nickles + pennies

    print
    print("The total value of your change is $" + str(total))

main()
