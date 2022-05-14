import smtplib # import SMTP client session object that can be used to send mail
from TZGTeam_datastore import food_dict, beverage_dict, detail_name, detail_number, detail_address, price # import food list and beverage order list to display in receipt

# define sendmail function
def sendmail(): 

    gmail_user = 'chatbottzg@gmail.com' # TZG Chatbot email
    gmail_password = 'chatbot1117' # TZG Chatbot password

    sent_from = 'chatbottzg@gmail.com' # Who send this email
    to = [input('>> Please enter your email for order receipt: (Press "Enter" when you are done.)\n')] # Who receive this email
    subject = 'Payment Receipt' # Email title
   
    # Content in email
    body = 'Dear customers, \n\nYour order is successfully! Thank you for choosing TZG Chatbot.\n\nCustomer Details:\n \nName:'+ str(detail_name)[1:-1] + '\nContact number: +60' +  str(detail_number)[1:-1] + '\nAddress: ' + str(detail_address)[1:-1] + '\n\nFood and Beverage list:' '''
            ''' + '\nFood & Quantity: ' + str(food_dict) + '\nBeverage & Quantity: ' +  str(beverage_dict) +'\n\nTotal Price: RM' + str(price)[1:-1] + '''
            ''' + '\n\nTZG Chatbot \nCompany Address: Jln Broga, 43500 Semenyih, Selangor (UNM) \nTel: +6 (03) 8924 8000'

    email_text = """hello\
From: %s
To: %s
Subject: %s

%s
"""% (sent_from, ", ".join(to), subject, body)
  
    try:  # send succssfully
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465) # Gmail SMTP server name and Gmail SMTP Ports = 465
        smtp_server.ehlo() # identufy myself to an ESMTP server using EHLO
        smtp_server.login(gmail_user, gmail_password) 
        smtp_server.sendmail(sent_from, to, email_text)
        smtp_server.close() # Terminate SMTP session
        print ("\n>> Email sent successfully!")
    except Exception as ex: # send unsuccssfully
        print (">> Something went wrong….",ex)
