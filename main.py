print("Item 1    35/-")
print("Item 2    100/-")
print("Item 3    125/-")
print("Item 4    1055/-")
print("Item 5    800/-")
print("Item 6    350/-")
print("")
print("Offers:-")
print("'Item 1' and 'Item 2' = 25% off     Exclusive offer")
print("'Item 1' and 'Item 3' = 10% off")
print("'Item 2' and 'Item 4' = 5% off")

item_dict = {"Item 1" : 35,
             "Item 2" : 100,
             "Item 3" : 125,
             "Item 4" : 1055,
             "Item 5" : 800,
             "Item 6" : 350}

bill = 0
#%%
while True:
    choice1 = input("Enter the Item you want to buy: ")
    choice2 = input("Enter the Item you want to buy: ")
    
    if choice1 not in item_dict or choice2 not in item_dict: # to check if the product is there in the list
        if choice1 not in item_dict:
            print(f"We do not have {choice1}.")
            continue
        elif choice2 not in item_dict:
            print(f"We do not have {choice2}.")
            continue
        elif choice1 not in item_dict and choice2 not in item_dict:
            print("We do not have both the products.")
            continue
    elif choice1 == "Item 1" and choice2 == "Item 2":
        print("You will get 25% discount!")
        bill += (35 + 100) * (25/100)
    elif choice1 == "Item 1" and choice2 == "Item 3":
        print("You will get 10% discount!")
        bill += (35 + 125) * (10/100)
    elif choice1 == "Item 2" and choice2 == "Item 4":
        print("You wil get 5% discount!")
        bill += (100 + 1055) * (5/100)
    else:
        print("No discounts")
        bill += item_dict[choice1] + item_dict[choice2]
    
    choice = input("Do you want to buy anymore things?(y/n) ").lower()
    if choice == "n":
        break
    elif choice == "y":
        continue
#%%
print(f"Your bill is {bill}/- rupees.")
