from prettytable import PrettyTable
try:
    print("Welcome To Happy Shoppinng")
    def shop():
        cart = {}
        add = 1
        remove = 1
        total_cost = 0
        total = 0
        try:
            print('These Are What We Offer ')
            print('-----------------------------------------------------------------------------------')
            # Code below are items in a table using prettytable
            x = PrettyTable()
            x.field_names = ['NO','ITEMS', 'PRICE']
            x.add_row([1,'Nike Blazer','$200.0'])
            x.add_row([2,'Skeleton Ripped Sweater', "$30.0"])
            x.add_row([3,'Beanie', "$5.0"])
            x.add_row([5, 'Tucker cap',"$12.0"])
            x.add_row([6,'Charles leman Watch', "$1500.0"])
            x.add_row([7,'Gucci Shades ', "$320.0"])
            x.add_row([8,'Laptop Bag', "$900"])
            print(x)
            # The code below creates a loop that gets and sums the item the user would like to purchase
            while add != 0:
                option = int(input('Enter The Item You Would Like To Add To The Cart:\n'))
                if option > 8:
                    nu = input("Item Not Found! Enter (1) to continue or (0) to cancle:")
                    if nu == '1':
                        shop()
                    elif nu == '0':
                        exit()
                    else:
                        print('Invalid')
                        exit()
                else:
                    if option == 1:
                        add_ons = int(input("Enter the quantity: "))
                        item_i_total = add_ons * 200.0
                        total = item_i_total
                        print("The price is: " + str(f'${total}'))
                    elif option == 2:
                        add_ons = int(input("Enter the quantity: "))
                        item_ii_total = add_ons * 30.0
                        total = item_ii_total
                        print("The price is: " + str(f'${total}'))
                    elif option == 3:
                        add_ons = int(input("Enter the quantity: "))
                        item_iii_total = add_ons * 5.0
                        total = item_iii_total
                        print("The price is: " + str(f'${total}'))
                    elif option == 4:
                        add_ons = int(input("Enter the quantity: "))
                        item_iv_total = add_ons * 12.0
                        total = item_iv_total
                        print("The price is: " + str(f'${total}'))
                    elif option == 5 :
                        add_ons = int(input("Enter the quantity: "))
                        item_v_total = add_ons * 1500.0
                        total = item_v_total
                        print("The price is: " + str(f'${total}'))
                    elif option == 6:
                        add_ons = int(input("Enter the quantity: "))
                        item_vi_total = add_ons * 320.0
                        total = item_vi_total
                        print("The price is: " + str(f'${total}'))
                    elif option == 7:
                        add_ons = int(input("Enter the quantity: "))
                        item_vii_total = add_ons * 900.0
                        total = item_vii_total
                        print("The price is: " + str(f'${total}'))
                    add = int(input("Would you like to add another item to your cart ? enter Yes (1) or No (0):"))
                    total_cost += total
                print("The total price of your Cart is: ", (f'${total_cost}'))

                # The code below deletes items from the users cart.
                remove_item = int(input("Would you like to remove an item? enter Yes(1) to remove item or No(0) to proceed with your payment:"))
                if remove_item == 1:
                    delete = int(input("Please Enter item Number To DELETE item:"))
                    if delete == 1:
                        delete = total_cost - item_i_total
                        total_cost = delete
                    elif delete == 2:
                        delete = total_cost - item_ii_total
                        total_cost = delete
                    elif delete == 3:
                        delete = total_cost - item_iii_total
                        total_cost = delete
                    elif delete == 4:
                        delete = total_cost - item_iv_total
                        total_cost = delete
                    elif delete == 5:
                        delete = total_cost - item_v_total
                        total_cost = delete
                    elif delete == 6:
                        delete = total_cost - item_vi_total
                        total_cost = delete
                    elif delete == 7:
                        delete = total_cost - item_vii_total
                        total_cost = delete
                    else:
                        print('Invalid input!')
                elif remove_item == 0:
                    print('CHECKOUT')
                    print('_________________________________________________________________________')
                    if total_cost > wallet:
                        print("Oops Insufficent Funds")
                        print(f'Available Balance: ${wallet}')
                    elif total_cost <= wallet:
                        print("Succesful Thank you for shopping at Happy !!!")
        except ValueError:
            act = input('Opps Invalid Input Enter (1) to continue or (0) to cancle:')
            if act == '1':
                shop()
            elif act == '0':
                exit()
            else:
                print('Invalid')
                exit()
    wallet = int(input("Please Enter An Amount You'ld Like To Deposit Into Your Wallet:"))
    shop()

except ValueError:
    act = input('Opps Invalid Input Enter (1) to continue or (0) to cancle:')
    if act == '1':
        shop()
    elif act == '0':
        exit()
    else:
        print('Invalid')
        exit()


