friends = ["amy" , "brad" ,"carl", "dave"]

with open("examples/nov 9/friends.txt", "w") as file:
    #Loop through friends and write them to a file
    for x in friends:
        file.write(f"{x}\n")