#Author Brenden Wade

companies = ["Google","Facebook", "Instagram", "AVX", "3D Systems","Human Technologies", "Palmetto", "O'Neal", "NBA", "MLB"]
wishlist = []


while True:
    command = input("(V)iew, (A)dd company to wish list, (R)emove company from wish list, (Q)uit: ").strip().lower()

    if command == "v":
        ans = input("View (A)ll companies or your (W)ish list? ").lower().strip()
        if ans == "a":
            for company in companies:
                print(f"- {companies}")
        elif command == "w":
            for wish in wishlist:
                print(f"- {wishlist} ")
        else:
            print("Invalid command.")
    elif command == "a":
        company1 = input("Enter company name: ")
        wishlist.append(company1)
    elif command == "r":
        company = input("Enter company name: ")
        wishlist.remove(company)
    elif command == 'q':
        break
    else:
        print("Invalid command")

print("Goodbye.")