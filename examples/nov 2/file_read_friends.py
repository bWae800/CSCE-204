def get_friends():
    friends = []
    
    
    with open("examples/nov 2/friends.txt") as file:
        for line in file:
            friends.append(line.strip())

    return friends

people = get_friends()

print("My friends: ")

for person in people:
    print(f" - {person}")