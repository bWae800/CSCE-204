#Author Brenden Wade


def encode(message):
    encoded = ""
    for letter in message:
        encoded = encoded + chr(ord(letter)+1)
    return encoded

def decode(message):
    decoded = ""
    for letter in message:
        decoded = decoded + chr(ord(letter)-1)
    return decoded

print("Secret Messages")

while True:
    command = input("(E)ncode, (D)ecode, or (Q)uit: ").lower().strip()
    if command == "e":
        userinput = input("Enter a secret message: ")
        print(f"Your encoded message is {encode(userinput)}")
    elif command == "d":
        userinput2 = input("Enter a secret message: ")
        print(f"Your decoded message is {decode(userinput2)}")
    elif command == "q":
        break
    else:
        print("Invalid command")
print("Goodbye.")

