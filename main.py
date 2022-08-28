name = input("Please enter your name:")
age = int(input("How old are you, {0}?".format(name)))
print(age)

if age >= 18:
    print("Eligible for Voting")
else:
    print("Not eligible for voting")
    print("Please come back in {0} year/years.".format(18 - age))

