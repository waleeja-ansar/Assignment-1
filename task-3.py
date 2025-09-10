birthdays = {
    "Ali": "January 5",
    "Sara": "March 14",
    "Ahmed": "July 21",
    "Waleeja": "September 7"
}
name = input("Enter a name to find their birthday: ")

if name in birthdays:
    print(name, "'s birthday is on", birthdays[name])
else:
    print("Sorry, no birthday found for", name)
