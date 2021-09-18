#Author Brenden Wade

endnum = int(input("Enter end number: "))
total = 0

for i in range(0,endnum+1):
    if(i % 2 == 0):
        print(i)
        total = total + i

print(f"Sum = {total}")