# import all related libraries
import sys # use for various function and variables
import pandas as pd # use to import pandas.io
from pandas.io import excel # import excel file
from PIL import Image # use for save and upload image
from prettytable import PrettyTable  # Create table for price list
from TZGTeam_mail import sendmail # import send email function from TZGTeam_mail file
from TZGTeam_train import chatbot, remarks # import chatbot and remarks function from TZGTeam_train file
from TZGTeam_datastore import food_list, beverage_list, food_order_list, beverage_order_list, food_price_list, beverage_price_list # import data storage list
from TZGTeam_datastore import detail_name, detail_address, detail_number, price # import user details and price
from TZGTeam_datastore import food_price_dict, beverage_price_dict, size_dict, food_dict, beverage_dict # import data storage dictionary

# import excel data with column B and C
menu = pd.read_excel(r'C:\Users\User\Desktop\Nott-A-Code Chatbot\TZGTeam_foodlist.xlsx', usecols='B:C')

# Define service function to ask customers' requirement
def service():
    #
    delivery_service = input('>> Dear users, do you require delivery or pick up ? \n[a] Delivery \n[b] Pick up (Can choose all delivery and pick up items)\n(Please type specify alphabet and press "Enter" when you are done)\n').lower()

    if delivery_service == 'a': # Choose [a] for delivery service
        customers_details()
        detail = input('\n>> Please confirm all your information are correct \n[a] Yes \n[b] No \n(Please type specify alphabet and press "Enter" when you are done)\n').lower()
        if detail == 'a':
            
            res = input('\n>> Do you want to order foods or beverage?  \n[a] Food \n[b] Beverage \n(Please type specify alphabet and press "Enter" when you are done)\n').lower()
        
        
            if res == 'a': # Choose [a] for order food
                return food_menu_delivery()
            elif res == 'b': # Choose [b] for order beverage
                return beverage_menu_delivery()
            else: # Choose others for wrong selection
                wrong_selection()
                service()
           
        else:
            error_message()
            service()
    
    elif delivery_service == 'b': # Choose [b] for pick up service
        res = input('\n>> Do you want to order foods or beverage? \n[a] Food \n[b] Beverage \n(Please type specify alphabet and press "Enter" when you are done)\n').lower()
        if res == 'a':
            return food_menu_pickup()
        elif res == 'b':
            return beverage_menu_pickup()
        else:
            wrong_selection()
            service()
    else: # Back to service function
        wrong_selection()
        service()


# define food menu pick up function 
def food_menu_pickup():
    # Provide option to choose food category
    print('\n>> Due to your selection, the list below shows delivery and pick up meals.')
    res = input('>> Please Pick a Food Category? \n[a] Malay (13 types) \n[b] Mamak (11 types) \n[c] Korean (15 types) \n[d] Japanese (25 types)\n(Please type specify alphabet and press "Enter" when you are done)\n').lower()

    # Accoding food category to run if-else condition
    if res == "a":
        im = Image.open(r"C:\Users\User\Desktop\Nott-A-Code Chatbot\TZGTeam_malay.jpg") # import image
        im.show() # Show image
        print(menu.iloc[0:13]) # Delivery food menu included in pick up food menu
        food_order_pickup() # Continue to food_order_pickup function

    elif res == "b":
        im = Image.open(r"C:\Users\User\Desktop\Nott-A-Code Chatbot\TZGTeam_mamak.jpg") 
        im.show() 
        print(menu.iloc[13:24])  # Delivery beverage included in pick up beverage menu 
        food_order_pickup()

    elif res == 'c' :
        im = Image.open(r"C:\Users\User\Desktop\Nott-A-Code Chatbot\TZGTeam_korean.jpg")
        im.show()
        print(menu.iloc[47:62]) # Korean food menu 
        food_order_pickup()

    elif res == 'd' :
        im = Image.open(r"C:\Users\User\Desktop\Nott-A-Code Chatbot\TZGTeam_japanese.jpg")
        im.show()
        print(menu.iloc[62:87]) # Japanese food menu   
        food_order_pickup()

    else: # Back to food_menu_pickup function
        wrong_selection()
        food_menu_pickup()

# Define food_menu_delivery function
def food_menu_delivery():
    # Provide option to choose food category
    print('\n>> Due to your selection, the list below only shows delivery meals')
    res = input('>> Please Pick a Food Category? \n[a] Malay (11 types) \n[b] Mamak (3 types) \n[c] Korean (15 types) \n[d] Japanese (25 types)\n(Please type specify alphabet and press "Enter" when you are done)\n').lower()

    # Accoding food category to run if-else condition
    if res == "a":
        im = Image.open(r"C:\Users\User\Desktop\Nott-A-Code Chatbot\TZGTeam_malaydeliver.jpg") # import image
        im.show() # show image
        print(menu.iloc[0:11]) # Malay food menu for delivery
        food_order_delivery() # Continue to food_order_service

    elif res == "b":
        im = Image.open(r"C:\Users\User\Desktop\Nott-A-Code Chatbot\TZGTeam_mamakdeliver.jpg")
        im.show()
        print(menu.iloc[21:24])  # Mamak food menu for delivery
        food_order_delivery()

    elif res == 'c' :
        im = Image.open(r"C:\Users\User\Desktop\Nott-A-Code Chatbot\TZGTeam_korean.jpg")
        im.show()
        print(menu.iloc[47:62]) # Korean food menu 
        food_order_delivery()

    elif res == 'd' :
        im = Image.open(r"C:\Users\User\Desktop\Nott-A-Code Chatbot\TZGTeam_japanese.jpg")
        im.show()
        print(menu.iloc[62:87]) # Japanese food menu
        food_order_delivery()

    else: # Back to food_menu_delivery service
        wrong_selection()
        food_menu_delivery()

# define food_order_delivery function
def food_order_delivery():
    # Order food 
    food_order = input('\n>> Dear Customers, please follow name list to enter item name you want to order (Suggest copy and paste to avoid wrong typing) :\n(Press "Enter" when you are done.)\n')
    qty = input('\n>> Please enter item quantity: (Please enter quantity and press "Enter when you are done)\n')

    if food_order in food_list:
        food_order_list.append(food_order) # Record orders in food order list
        food_dict.update({food_order: qty})
        print('\n>> View your food order list: \n' + str(food_dict)) # Show customer's food orders
        res_1 = input('\n>> Do you want to add any food items to your order? \n[a] Yes \n[b] No \n(Please type specify alphabet and press "Enter" when you are done)\n').lower() # Additional order requirement

        if res_1 == 'a': # Back to food_menu_delivery function
            food_menu_delivery()

        elif res_1 == 'b':
            print('>> View your food order list: \n' + str(food_dict)) # Show the food order list
            beverage_menu_delivery()   # Continue to beverage_menu delivery function
        
        else: 
            wrong_selection()
            print('>> View your food order list: \n' + str(food_dict))
            beverage_menu_delivery() # Back to beverage_menu_delivery function 

    else: 
        error_message()
        food_menu_delivery() # Back to food_order_delivery function

# define food_order_pickup function
def food_order_pickup():
    # Order food
    food_order = input('\n>> Dear Customers, please follow name list to enter item name you want to order (Suggest copy and paste to avoid wrong typing):\n(Press "Enter" when you are done.)\n')
    qty = input('\n>> Please enter item quantity: (Please enter quantity and press "Enter when you are done)\n')
    

    if food_order in food_list:
        food_order_list.append(food_order) # Record orders in food order list
        food_dict.update({food_order: qty})
        print('\n>> View your food order list: \n' + str(food_dict)) # Show customer's food orders
        res_1 = input('\n>> Do you want to add any food items to your order \n[a] Yes \n[b] No \n(Please type specify alphabet and press "Enter" when you are done)\n').lower()# Additional order requirement

        if res_1 == 'a': 
            food_menu_pickup()  # Back to food_menu_pickup function

        elif res_1 == 'b': 
            print('>> View your food order list: \n' + str(food_dict))# Show the food order list
            beverage_menu_pickup() # Continue to beverage_menu delivery function
        
        else:
            wrong_selection()
            print('>> View your food order list: \n' + str(food_dict))
            beverage_menu_pickup()

    else:
        error_message()
        food_menu_pickup() # Back to food_order_pickup function


# define beverage_menu_pickup function
def beverage_menu_pickup():
    res = input('\n>> Do you want to order beverages? \n[a] Yes \n[b] No \n(Please type specify alphabet and press "Enter" when you are done)\n').lower()
    if res == 'a':
        res = input('\n>> What type of beverage would you like? \n[a] Mamak Beverage (8 types) \n[b] Juice (6 types)\n[c] Coffee type (9 types) \n(Please type specify alphabet and press "Enter" when you are done)\n').lower()
        if res == "a" :
            im = Image.open(r"C:\Users\User\Desktop\Nott-A-Code Chatbot\TZGTeam_mamakbeverage.jpg") # import images
            im.show() # show images
            print(menu.iloc[24:32]) # Mamak beverage menu 
            beverage_order_pickup() # Continue to beverage_order_pickup function
        elif res == "b" :
            im = Image.open(r"C:\Users\User\Desktop\Nott-A-Code Chatbot\TZGTeam_juice.jpg")
            im.show()
            print(menu.iloc[32:38]) # Juice menu
            beverage_order_pickup()
        elif res == "c" :
            im = Image.open(r"C:\Users\User\Desktop\Nott-A-Code Chatbot\TZGTeam_coffee.jpg")
            im.show()
            print(menu.iloc[38:47]) # Coffee type menu
            beverage_order_pickup()
        else:
            wrong_selection()
            beverage_menu_pickup() # Back to beverage_menu_pickup function

    elif res == 'b':
        remarks()  # Continue to remarks function
    else:
        beverage_menu_pickup() # Back to beverage_menu_pickup function

# define beverage_menu_delivery function
def beverage_menu_delivery():
    res = input('\n>> Do you want to order beverages? \n[a] Yes \n[b] No \n(Please type specify alphabet and press "Enter" when you are done)\n').lower()
    if res == 'a':
        im = Image.open(r"C:\Users\User\Desktop\Nott-A-Code Chatbot\TZGTeam_coffee.jpg") # import image
        im.show() # show image
        print('\n>> Due to your selection, the list below only shows delivery meals')
        print(menu.iloc[38:47]) # Coffee type menu
        beverage_order_delivery() # Continue to beverage_order_delivery function
    elif res == 'b':
        remarks() # Continue to remarks function
    else:
        beverage_menu_delivery() # Back to beverage_menu_delivery function

# Define beverage size function
def beverage_size():

    res = input('\n>> What size drink can I get for you? \n[a] Small \n[b] Medium (+RM0.50) \n[c] Large (+RM1.00)\n(Please type specify alphabet and press "Enter" when you are done)\n').lower()

    if res == "a" :
        return 'Small'
    elif res == "b" :
        return 'Medium'
    elif res == "c" :
        return 'Large'
    else:
        wrong_selection()
        return beverage_size() # Back beverage_size function

# define beverage_order_pickup function
def beverage_order_pickup():

    print('>> Note: If you want to cancel order , you can press "Enter" to choose again')
    
    beverage_order = input('>> Dear Customers, please follow name list to enter item name you want to order (Suggest copy and paste to avoid wrong typing):\n(Press "Enter" when you are done.)\n')


    if beverage_order in beverage_list:
        beverage_order_list.append(beverage_order) # save order beverages in list
        size = beverage_size() # called the beverage_size function
        qty = input('\n>> Please enter item quantity: (Please enter quantity and press "Enter when you are done)\n')
        beverage_dict.update({beverage_order: qty})
        size_dict.update({beverage_order:size}) # record beverage and its size in size dictionary
        print(f'\n>> Beverage and size list {size_dict}') 

        res_1 = input('\n>> Do you want to add any beverage items to your order? \n[a] Yes \n[b] No \n(Please type specify alphabet and press "Enter" when you are done)\n').lower()
        if res_1 == 'a':
            beverage_menu_pickup() # Back to beverage_menu_pickup function

        elif res_1 == 'b':
            print('\n>> View your beverage order list: \n' + str(beverage_dict)) # View beverage order list
            remarks() # Continue to remarks function
        
        else:
            wrong_selection()
            print('\n>> View your beverage order list: \n' + str(beverage_dict)) # View beverage order list
            remarks()

    else:
        error_message() # Show error message to remind users
        beverage_menu_pickup()
   
#define beverage_order_delivery function
def beverage_order_delivery():

    print('>> Note: If you want to cancel order , you can press "Enter" to choose again')
    
    beverage_order = input('\n>> Dear Customers, please follow name list to enter item name you want to order (Suggest copy and paste to avoid wrong typing):\n(Press "Enter" when you are done.)\n')
    

    if beverage_order in beverage_list:
        beverage_order_list.append(beverage_order)  # save order beverages in list
        size = beverage_size() # called the beverage_size function
        qty = input('\n>> Please enter item quantity: (Please enter quantity and press "Enter when you are done)\n')
        beverage_dict.update({beverage_order: qty})
        size_dict.update({beverage_order:size}) # record beverage and its size in size dictionary
        print(f'>> Beverage and size list:\n {size_dict}')

        res_1 = input('\n>> Do you want to add any beverage items to your order? \n[a] Yes \n[b] No \n(Please type specify alphabet and press "Enter" when you are done)\n').lower()
        if res_1 == 'a':
            beverage_menu_delivery() #Back to beverage_menu_deliver function

        elif res_1 == 'b':
            print('\n>> View your beverage order list: \n' + str(beverage_dict)) # View beverage order list
            remarks()
        
        else:
            wrong_selection()
            print('\n>> View your beverage order list: \n' + str(beverage_dict)) # View beverage order list
            remarks()

    else:
        error_message() # Show error message to remind usersTZG
        beverage_menu_delivery()



# define customer_details function to get information

def customers_details():
    name = input('\n>> Dear customers, Please type your name. (Press "Enter" when you are done.)\n')
    detail_name.append(name)
    contact_number = input('\n>> Dear customers, Please type your contact number. (Press "Enter" when you are done.) \n+60')
    detail_number.append(contact_number)
    try: # Ensure contact number is valid
        val = int(contact_number)
        address = input('\n>> Dear customers, Please type your delivery address. (Press "Enter" when you are done.)\n')
        detail_address.append(address)
        print('\nName: ' + name +'\nContact Number: +60' + contact_number + '\nAddress: ' + address)
        
        
    except ValueError: # Run when contact number is error
        print('>> Please enter valid contact number e.g..+60123456789')
        customers_details() # Back to customer_details function

        
# Define calculate bills function

def calculate_bills():
    
    print('\n>> Dear user, please kindly check your bill statement below：')
    
    # Food price calculation method
    single_price = 0 # Set single price equal 0 first
    total_food_price = 0 # Set total food price equal 0 first
    for element in food_order_list: # Calculate food price in food list
        if element in food_price_dict: # Check element in food price dictionary
            single_price = food_price_dict.get(element) # Get dictionary value (price)
            total_food_price += single_price * int(food_dict.get(element))  # Calculate total price
    # Show final food price with 2 decimal number    
    food_table = PrettyTable(["Food Item", "Total Price (RM)"]) # Create the table title
    food_table.add_row([food_order_list, total_food_price])# import food order list and price list inside table
    print(food_table) # print table     

    
    # Beverage price calculation method
    single_price = 0
    total_beverage_price = 0
    for element in beverage_order_list:  # Calculate beverage price in food list
        if element in beverage_price_dict: # Check element in beverage price dictionary
            if element in size_dict: # Check beverage size in size dictionary
                if size_dict.get(element) == 'Medium':
                    single_price = beverage_price_dict.get(element) + float(0.5) # Medium size add more RM0.50
                elif size_dict.get(element) == 'Large':
                    single_price = beverage_price_dict.get(element) + int(1) # Large size add more RM1.00
                else:
                    single_price = beverage_price_dict.get(element) # Origin price
            total_beverage_price += single_price*int(beverage_dict.get(element)) # Calculate total price
    bevarage_table = PrettyTable(["Beverage Item", "Total Price (RM) "]) # Create the table title
    bevarage_table.add_row([beverage_order_list, total_beverage_price]) # import beverage order list and price list inside table
    print(bevarage_table) # print table

    # Sum total food price and total beverage price
    total_price = total_food_price + total_beverage_price
    
    # If consume over RM 50 can get discount
    if total_price > 50:
        print('''
    >> Congratulation dear customers !!! TZG chatbot company organize promotions from 08/11/2021 - 17/11/2021. 
    All of the items didn't charge delivery fee and total bill can get 20 percent discount for who are consume over RM 50 in TZG chatbot
        ''')
        total_price =total_price - 0.2*total_price # Show final price after discount
        total_price_1 ="{:.2f}".format(total_price) # Show final price with 2 decimal number
        price.append(total_price_1)
        myTable = PrettyTable(["Food Price (RM)", "Beverage Price (RM)", "Total Price (RM)"])
        myTable.add_row([0.8*int(total_food_price), 0.8*int(total_beverage_price), total_price])
        print(myTable)
        payment_method() # Continue to payment_method function
    else:
        total_price_1 ="{:.2f}".format(total_price) # Show final price with 2 decimal number
        price.append(total_price_1)
        myTable = PrettyTable(["Food Price (RM)", "Beverage Price (RM)", "Total Price (RM)"])
        myTable.add_row([total_food_price, total_beverage_price, total_price])
        print(myTable)
        payment_method() # Continue to payment_method function

    
# Create payment method function
def payment_method():
    res = input('\n>> Please choose your payment method: \n[a] Cash \n[b] TNG eWallet  \n[c] Master/ Visa Card \n(Please type specify alphabet and press "Enter" when you are done)\n').lower() # User choose payment method
    if res == 'a' or res == 'b' or res == 'c':

        print('>> Awesome, your order is booked, you will get a confirmation message from email in just a moment.\n')
        # Show company information
        print('''>> For more information or any inquiry, you can contact TZG Company from information below: 
    
        TZG Contact Number:  +6 (03) 8924 8000
        TZG Company Address: Jln Broga, 43500 Semenyih, Selangor
        TZG Company Email:   chatbottzg@gmail.com
              ''')

        sendmail() # Called sendmail function
        
        print('>> Dear customers, we appreciate your support for our order chatbot. See you next time.')
        sys.exit()

    else:
        print('>> Sorry, your payment is unsuccessful.')
        transaction = input('>> Do you want to continue your transaction? \n[a] Yes \n[b] No \n(Please type specify alphabet and press "Enter" when you are done)\n').lower()
        if transaction == 'a':
            payment_method() # Back to payment_method 
            
        else:
            print('>> Dear customers, your order has been cancelled. See you next time')
            sys.exit()       

# Use lambda define error message function (Used in wrong type foods and beverages name)
error_message = lambda: print("\n>> Dear customers, we don't know understand your order. Please complete your order again.\n")

# Use lambda define Wrong selection function (Used in MCQ)
wrong_selection = lambda: print("\n>> I'm sorry, I didn't understand your selection. Please enter the corresponding letter for your response.\n")

#define TZGchatbot
def TZGchatbot():
    chatbot() 
    service() 
    calculate_bills() 
    
# Called TZG function run the program
TZGchatbot()

