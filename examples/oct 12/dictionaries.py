toys = {
    "doll":19.89,
    "car":1.99,
    "truck":7.85,
    "puzzle":14.95,
    "slinky":2

}

#print(toys("doll"))

toys["yo-yo"] = 4.5 # adding an item

#loop through and display toys
for key in toys:
    print(f"{key} - costs ${toys[key]}")

toy = input("Enter Toy: ").strip().lower()
print(f"{toy} costs ${toys[toy]}")