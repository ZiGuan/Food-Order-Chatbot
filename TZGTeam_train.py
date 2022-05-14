import re  # Regular expression
import sys # Use to exit program
from nltk.chat.util import Chat, reflections # Natural Language Toolkit: Chatbot Utilities
from nltk.corpus import wordnet # Use to training chatbot answer frequenly asked question

# Building a list of Keywords
def chatbot():
    list_words=['hello','time','order', 'food', 'beverage','bill','receipt','fee','cancel','missing','discount','help','information','refund','location']
    list_syn={}
    for word in list_words:

        synonyms=[] # Create empty synonyms list
        for syn in wordnet.synsets(word):
            for lem in syn.lemmas():
                # Remove any special characters from synonym strings
                lem_name = re.sub('[^a-zA-Z0-9 \n\.]', ' ', lem.name())
                synonyms.append(lem_name) # Add lem_name into synonyms list

        list_syn[word]=set(synonyms)

    # Building dictionary of Intents & Keywords
    keywords={}
    keywords_dict={}

    # Defining a greet key in the keywords dictionary
    keywords['greet']=[]
    # Populating the values in the keywords dictionary with synonyms of keywords formatted with Regex metacharacters 
    for synonym in list(list_syn['hello']):
        keywords['greet'].append('.*\\b'+synonym+'\\b.*')

    # Defining a timings key in the keywords dictionary   
    keywords['time']=[]
    # Populating the values in the keywords dictionary with synonyms of keywords formatted with Regex metacharacters 
    for synonym in list(list_syn['time']):
        keywords['time'].append('.*\\b'+synonym+'\\b.*')

    keywords['order']=[]
    # Populating the values in the keywords dictionary with synonyms of keywords formatted with Regex metacharacters 
    for synonym in list(list_syn['order']):
        keywords['order'].append('.*\\b'+synonym+'\\b.*')

    # Defining a food key in the keywords dictionary
    keywords['food']=[]
    for synonym in list(list_syn['food']):
        keywords['food'].append('.*\\b'+synonym+'\\b.*')

    # Defining a beverage key in the keywords dictionary
    keywords['beverage']=[]
    for synonym in list(list_syn['beverage']):
        keywords['beverage'].append('.*\\b'+synonym+'\\b.*')
    
    # Defining a bill key in the keywords dictionary
    keywords['bill']=[]
    for synonym in list(list_syn['bill']):
        keywords['bill'].append('.*\\b'+synonym+'\\b.*')
    
    # Defining a receipt key in the keywords dictionary
    keywords['receipt']=[]
    for synonym in list(list_syn['receipt']):
        keywords['receipt'].append('.*\\b'+synonym+'\\b.*')
    
    # Defining a fee key in the keywords dictionary
    keywords['fee']=[]
    for synonym in list(list_syn['fee']):
        keywords['fee'].append('.*\\b'+synonym+'\\b.*')
    
    # Defining a cancel key in the keywords dictionary
    keywords['cancel']=[]
    for synonym in list(list_syn['cancel']):
        keywords['cancel'].append('.*\\b'+synonym+'\\b.*')
    
    # Defining a missing key in the keywords dictionary
    keywords['missing']=[]
    for synonym in list(list_syn['missing']):
        keywords['missing'].append('.*\\b'+synonym+'\\b.*')
    
    # Defining a discount key in the keywords dictionary
    keywords['discount']=[]
    for synonym in list(list_syn['discount']):
        keywords['discount'].append('.*\\b'+synonym+'\\b.*')

    # Defining a help key in the keywords dictionary
    keywords['help']=[]
    for synonym in list(list_syn['help']):
        keywords['help'].append('.*\\b'+synonym+'\\b.*')
    
    # Defining a information key in the keywords dictionary
    keywords['information']=[]
    for synonym in list(list_syn['information']):
        keywords['information'].append('.*\\b'+synonym+'\\b.*')
    
    # Defining a refund key in the keywords dictionary
    keywords['refund']=[]
    for synonym in list(list_syn['refund']):
        keywords['refund'].append('.*\\b'+synonym+'\\b.*')

    # Defining a location key in the keywords dictionary
    keywords['location']=[]
    for synonym in list(list_syn['location']):
        keywords['location'].append('.*\\b'+synonym+'\\b.*')

    for intent, keys in keywords.items():
         # Joining the values in the keywords dictionary with the OR (|) operator updating them in keywords_dict dictionary
        keywords_dict[intent]=re.compile('|'.join(keys))

# Building a dictionary of responses
    responses={
    
    'greet':'>> Hello! How can I help you? (Type "help" command and press "Enter" to get help)\n',
    'time':'>> We will prepare and deliver your food within 30 minutes (Type "help" command and press "Enter" to get help)\n',
    'food':'>> We serve Malay, Mamak, Korean and Japanese types food. (Type "help" command and press "Enter" to get help)\n',
    'beverage': '>> We serve Mamak beverage, Juice and various of coffee types. (Type "help" command and press "Enter" to get help)\n',
    'bill': '>> We accept cash ,TNG eWallet, Master/Visa Card these three payment method. (Type "help" command and press "Enter" to get help)\n',
    'fee':'>> From 08/11/2021 until 17/11/2021, TZG  chatbot did not charge any delivery fee. (Type "help" command and press "Enter" to get help)\n',
    'cancel' : '>> If you want to cancel your order, please contact us through TZG Contact number: +6 (03) 8924 8000 (Type "help" command and press "Enter" to get help)\n',
    'missing': '>> If you want to cancel your order, please contact us through TZG Contact number: +6 (03) 8924 8000 to get the refund. (Type "help" command and press "Enter" to get help)\n',
    'discount': '>> Customers can get 20 percent discount if they consume over RM50 in TZG Chatbot from 08/11/2021 until 17/11/2021. (Type "help" command and press "Enter" to get help)\n',
    'fallback': '>> I dont quite understand. Could you repeat that? (Type "help" command and press "Enter" to get help)\n',
    'information': (''' >> TZG Contact Number:  +6 (03) 8924 8000
    TZG Company Address: Jln Broga, 43500 Semenyih, Selangor
    TZG Company Email:   chatbottzg@gmail.com
    (Type "help" command and press "Enter" to get help)\n '''),
    'refund': ('Please contact TZG Company through email(chatbottzg@gmail.com) to get refund (Type "help" command and press "Enter" to get help)\n'),
    'location' : ('Jln Broga, 43500 Semenyih, Selangor (Type "help" command and press "Enter" to get help)\n'),
    'receipt' : ('>> Customers will receive their receipt through email (Type "help" command and press "Enter" to get help)\n'),
    'help':('''>> Refer the commands below if you are doubt: (Please type specify command and press "Enter")\n
    
           |    Command          |         Function
        ---|---------------------|----------------------------------------------
        1  |    order            |  Start the order session 
        2  |    time             |  Check deliver time 
        3  |    food             |  Check the foods categories 
        4  |    beverage         |  Check the beverages categories
        5  |    payment          |  Check different payment method
        6  |    fee              |  Check any additional fee.
        7  |    cancel           |  Check how to cancel order
        8  |    missing          |  Check how to contact company if order missing.
        9  |    discount         |  Check how to get promotion
        10 |    help             |  Check all of the commands in chatbot
        11 |    information      |  Check chatbot and company information
        12 |    refund           |  Check how to get refund
        13 |    location         |  Check TZG Company location
        14 |    receipt          |  Check how to get receipt
            ''')

}
    # Greeting with users
    print ("\n>> Hello, Welcome to TZG Chatbot.")
    res = input('>> How may I help you? \n[a] Yes, I need help. \n[b] No, just browsing \n(Please type specify alphabet and press "Enter" when you are done)\n').lower()
    
    if res == 'a':
        print('\n>> Please type "help" and press "Enter"')
        
    else:
        print('See you next time.')
        sys.exit()
    
    while (True):  
        # Takes the user input and converts all characters to lowercase
        user_input = input().lower()
    # Defining the Chatbot's exit condition

        if user_input == 'order': 
            print(">> You can start to take order.\n")
            break 

        matched_intent = None 

        for intent,pattern in keywords_dict.items():
        # Using the regular expression search function to look for keywords in user input
            if re.search(pattern, user_input): 
            # if a keyword matches, select the corresponding intent from the keywords_dict dictionary
                matched_intent=intent  


        # The fallback intent is selected by default
        key='fallback' 
        if matched_intent in responses:
        # If a keyword matches, the fallback intent is replaced by the matched intent as the key for the responses dictionary
            key = matched_intent 
        # The chatbot prints the response that matches the selected intent
        print (responses[key]) 
# While loop to run the chatbot indefinetely

# Training chatbot auto reply
reflections = {"i am":"you are","i was":"you were","i" :"you","i'm":"you are","i'd": "you would",
  "i've": "you have","i'll": "you will","your": "my","yours" : "mine","you": "me","me": "you","my": "your",
  "you are" : "I am","you were" : "I was","you've" : "I have","you'll": "I will",}

# Use for chatbot reply in remarks
remarks_pairs = [
                ["(.*)deliver|How long|time(.*)", ['We will deliver food to your destination within 30 minutes\n']],
                ["(.*)hot(.*)",["We will take care that the food delivered is hot\n"]],
                ["(.*)more spicy(.*)",["We will notice restaurant to add more spicy for you\n"]],
                ["(.*)less spicy(.*)",["We will notice restaurant to prepare less spicy for you\n"]],
                ["(.*)no spicy(.*)",["We will inform restaurant don't add spicy for you\n"]],
                ["(.*)less ice(.*)",["We will prepare less ice for your beverage. \n"]],
                ["(.*)more ice(.*)",["We will prepare more ice for your beverage. \n"]],
                [("(.*)quit(.*)"),["It was nice talking to you. See you soon :)\n"]],
                ]

def remarks():
    # default message at the start
    print(("\n>> Dear Users, if you have any additional requirement can type in here!!! (Please type 'quit' to leave when done remarks)"))
    # Called function with remarks_pairs and reflection
    remark = Chat(remarks_pairs, reflections)
    remark.converse()

    

        