from product import Product


shopping_list = [
    Product("Converse Shoes" , "Tan and Black walking shoes", 29.99),
    Product("Baby doll" , "Walking and talking fun doll", 19.99),
    Product("Gym bag" , "Green duffel bag", 45.99)
]
total = 0
print("Your Shopping list")
for item in shopping_list:
    item.display()
    total += item.get_total_price()


print(f"Total: ${round(total,2)}")