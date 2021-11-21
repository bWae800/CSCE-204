from criminal import Criminal

def get_criminals():
    criminals = []

    with open("examples/nov 16/criminals.txt") as file:
        for line in file:
            data = line.split(',')
            first_name = data[0].strip()
            last_name = data[1].strip()
            gender = data[2].strip()
            crime_type = data[3].strip()
            in_jail_text = data[4].strip()
            in_jail = get_bool(in_jail_text)
            description = data[5].strip()
            criminal = Criminal(first_name, last_name, gender, crime_type, in_jail, description)
            criminals.append(criminal)
    return criminals
def get_bool(data):
    if data.lower() == "true":
        return True
    else:
        return False

criminals = get_criminals()

print("Welcome to our crime system")

while True:
    command = input("(V)iew, (S)earch, or (Q)uit: ").strip().lower()

    if command == "v":
        print("Full list of criminals")
        for criminal in criminals:
            criminal.display()
    elif command == "s":
        gender = input("Enter 'Male' or 'Female': ").lower().strip()
        crime_type = input("Enter 'Robbery', 'Assault', or 'Murder': ").lower().strip()
        print("Criminals that match your criteria...")
        for criminal in criminals:
            if criminal.is_match(gender,crime_type):
                criminal.display()
    elif command == "q":
        break
    else:
        print("Invalid command")