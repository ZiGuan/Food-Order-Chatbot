# Store food list
food_list = ['Nasi lemak','Nasi goreng kampung','Nasi goreng tomyam','Nasi goreng ikan masin','Nasi goreng paprik','Nasi goreng USA',
             'Nasi goreng pattaya','Nasi goreng biasa','Ikan goreng','Ayam goreng','Satay','Kuih talam','Kuih koci','Roti canai','Roti telur',
             'Roti cheese','Roti boom','Roti planta','Roti susu','Roti tisu','Tosai','Mee goreng','Maggi goreng','Maggi soup','Tteok' ,'Kimchi',
             'Gimbap','Tteokbokki','Hobakjuk','Ramyun','Kimchi Fried Rice','Bulgogi','Jjajangmyeon','Kongguksu','Japchae','Bulgogi with rice',
             'Naengmyeon','Bibimbap','Sundubu Jjigae','Miso Soup','Chawanmushi','Gyoza','Tempura','Tamagoyaki (Egg Roll)','Teriyaki Chicken Bento',
             'Teriyaki Vegetable Bento','Seafood Bento','Chicken Katsu Don','Tempura Soba','Chicken Yaki Soba','Vegetable Yaki Soba','Zaru Soba',
             'Zaru Soba + Tempura','Tempura Udon','Chicken Yaki Udon','Vegetable Yaki Udon','Zaru Udon','Zaru Udon + Tempura','Chicken Teriyaki Lunch Set (Miso Soup)',
             'Tempura Lunch Set (Miso Soup)','Vegetarian Lunch Set (Miso Soup)','Chicken Teriyaki Dinner Set (Chawanmushi)','Tempura Dinner Set (Chawanmushi)',
             'Vegetarian Dinner Set (Chawanmushi)',]

# Store beverage list
beverage_list = ['Teh tarik ais','The tarik panas','Milo ais','Milo panas','Cincau','Limau ais','Limau panas','Bandung ais',
                 'Apple juice','Orange juice','Watermelon juice','Cucumber juice','Pineapple juice','Carrot juice','Espresso',
                 'Hot Americano','Iced Americano','Hot Latte','Iced Latte','Hot Cappuccino','Ice Cappuccino','Hot Mocha','Iced Mocha',]

# Store food price list
food_price_list = [2,6,6.5,6.5,7,7,7,5,3.5,3,1.2,0.7,0.4,1.2,2.3,2.5,2.2,2.2,2.2,3.2,1.2,5,5,4,2,4,4.5,5,
                   6,6.5,7,7,7,7.5,8,8,8.5,9,10,1.5,1.5,5,5,1.5,8,6.5,9,8,7,7,6,6,7,7,7,6,6,7,10,9,8,10,9,8,]

# Store beverage price list
beverage_price_list = [2.2,1.8,2.5,2.2,2.5,1.8,1.5,2,5,5,5,5,5,5,6,7,8,9,10,9,10,9,10]

# Combine food list and food price list to dictionary for calculate bills
food_price_dict = {key:value for key,value in zip(food_list,food_price_list)}
# Combine beverage list and beverage price list to dictionary for calculate bills
beverage_price_dict = {key:value for key,value in zip(beverage_list,beverage_price_list)}

# Empty detail list to record customer details
detail_name = []
detail_number = []
detail_address = []
# Empty price list to record total price
price = []
# Empty food order list to record customer orders
food_order_list = []
# Empty food dict to record food quantity
food_dict = {}
# Empty beverage order list to record customer orders
beverage_order_list = []
# Empty food dict to record beverage quantity
beverage_dict = {}
# Empty beverage size list to record customer beverage sizes
size_dict = {}