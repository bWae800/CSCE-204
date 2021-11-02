def get_phone_book():
    phonebook = {}


    with open("examples/nov 2/phones.txt") as file:
        for line in file:
            data = line.split(",")
            friend = data[0].strip().lower()
            phone = data[1].strip()
            phonebook[friend] = phone



    return phonebook

def display_phone_book(phonebook):
    for person in phonebook:
        print(f"{person}: {phonebook[person]}")

def getphonenumber(phonebook):
    personname = input("Enter Name: ").lower().strip()

    if personname in phonebook:
        print(f"{personname}'s phone number is {phonebook[personname]}")
    else:
        print(f"Sorry, {personname} is not in the phonebook.")


phonelist = get_phone_book()
display_phone_book(phonelist)
getphonenumber(phonelist)