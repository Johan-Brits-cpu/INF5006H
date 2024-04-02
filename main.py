
try:
    val = int(input("Please type provide and integer value:"))
except TypeError:
    print("You did not provide and integer value")
    val = int(input("Please retry. Type provide and integer value"))
finally:
    print("Executed! ")