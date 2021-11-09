numbers = [8,13,29,6,7,10]

with open("examples/nov 9/numbers.txt", "w") as file:
    #Loop through and write a comma separated list of numbers
    for i in range(len(numbers)):
        file.write(f"{numbers[i]}")
        if i < len(numbers) - 1:
            file.write(", ")