class Error(Exception):
    pass
class ValueInvalid (Error):
    pass


while True:
    unit1 = input("Choose conversion: ")
    unit2 = input("Choose conversion: ")
    if unit1 == "" or unit2 == "":
        print("Must enter units to continue program")

    value = float(input("Enter Conversion Number: "))


    if unit1 == "mm" and unit2 == "cm":
        print(value / 10) 
    elif unit1 == "mm" and unit2 == "m":
        print(value / 1000)
    elif unit1 == "mm" and unit2 == "km":
        print(value / 1000000)
    elif unit1 == "cm" and unit2 == "mm":
        print(value * 10)
    elif unit1 == "cm" and unit2 == "m":
        print(value / 100)
    elif unit1 == "cm" and unit2 == "km":
        print(value / 100000)
    elif unit1 == "m" and unit2 == "mm":
        print(value * 1000)
    elif unit1 == "m" and unit2 == "cm":
        print(value * 100)
    elif unit1 == "m" and unit2 == "km":
        print(value / 1000)
    elif unit1 == "km" and unit2 == "mm":
        print(value * 1000000)
    elif unit1 == "km" and unit2 == "cm":
        print(value / 100000)
    elif unit1 == "km" and unit2 == "m":
        print(value * 1000)
    else:
        print("Please enter valid information")