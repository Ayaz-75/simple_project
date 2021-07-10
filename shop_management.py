




# welcome to the shop management

shop_items=[]


def shop_menu():
    print("1- Add item in shop")
    print("2- update item in shop")
    print("3- delete item from shop")

    choice=int(input("enter your choice: "))



    if choice==1:
        add_item=input("enter the item to be added in shop: ")
        shop_items.append(add_item)
        print("items in shop are: ",shop_items)
        print()
        shop_menu()

    elif choice==2:
        check_item=input("Enter item name to be checked in shop: ")
        if check_item in shop_items:
            print(check_item," is present is shop")
            new_item=input("Enter new item to update previous one: ")
            chech_item_index=shop_items.index(check_item)
            shop_items.insert(chech_item_index,new_item)

            shop_items.remove(check_item)
            print(check_item," is updated to ",new_item)
            print()
        shop_menu()
    


    elif choice==3:
        check_itom=input("Enter the item to check in shop: ")
        if check_itom in shop_items:
            shop_items.remove(check_itom)
            print(check_itom," is now deleted from shop menu")
        shop_menu()



shop_menu()