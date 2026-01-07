print("*** Welcome to Indian Food Restaurant ***\n")

print("1. Coffee: Rs 60")
print("2. Sandvich: Rs 120")
print("3. Burger: Rs 40")
print("4. Pizza: Rs 50")
print("5. Pasta: Rs 30")

total_order=0

item1 = input("Enter the number of item you want to order = ")
if item1 == '1':
    item_name1 = 'Coffee'
    total_order = 60
elif item1 == '2':
    item_name1 = 'Sandvich'
    total_order = 120
elif item1 == '3':
    item_name1 = 'Burger'
    total_order = 40
elif item1 == '4':
    item_name1 = 'Pizza'
    total_order = 50
elif item1 == '5':
    item_name1 = 'Pasta'
    total_order = 30
else:
    item_name1 = None
    item_price1 = 0
    print("Ordered item is not available yet")
    
print("Your item", item_name1, "has been added to your order" )
another_order = input("\nDo you want to add another item? (Yes/No) ")
if another_order == "Yes" or "yes" or "Y" or "y":
    item2 = input("Enter the number of second item = ")
    if item2 == '1':
        item_name2 = 'Coffee'
        total_order += 60
    elif item2 == '2':
        item_name2 = 'Sandvich'
        total_order += 120
    elif item2 == '3':
        item_name2 = 'Burger'
        total_order += 40
    elif item2 == '4':
        item_name2 = 'Pizza'
        total_order += 50
    elif item2 == '5':
        item_name2 = 'Pasta'
        total_order += 30
    else:
        item_name2 = None
        item_price2 = 0
        print("Ordered item is not available yet")
        
    print("Your item", item_name2, "has been added to your order" )
print("The total amount of items to pay = Rs", total_order)