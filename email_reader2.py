#modules
import imaplib
import email

#credentials
username ="rajumm1996@gmail.com"

#generated app password
app_password= "noaqixzdfefxjfod"

# https://www.systoolsgroup.com/imap/
gmail_host= 'imap.gmail.com'


from message_classifier_main import classify_text_msg

def mess_read():

                #set connection
                mail = imaplib.IMAP4_SSL(gmail_host)

                #login
                mail.login(username, app_password)

                #select inbox
                mail.select("INBOX")

                messages_recieved_by_sequence_spam=[]
                messages_recieved_by_sequence_ham=[]
                mess_sub=[]
                mess_to=[]
                mess_from=[]
                mess_date=[]


                #select specific mails
                _, selected_mails = mail.search(None, '(FROM "no-reply-smsforwarder@cofp.ru")')

                #total number of mails from specific user
                print("Total Messages from no-reply-smsforwarder@cofp.ru :" , len(selected_mails[0].split()))

                for num in selected_mails[0].split():
                    _, data = mail.fetch(num , '(RFC822)')
                    _, bytes_data = data[0]

                    #convert the byte data to message
                    email_message = email.message_from_bytes(bytes_data)
                    print("\n===========================================")

                    #access data
                    print("Subject: ",email_message["subject"])
                    print("To:", email_message["to"])
                    print("From: ",email_message["from"])
                    print("Date: ",email_message["date"])
                    for part in email_message.walk():
                        if part.get_content_type()=="text/plain" or part.get_content_type()=="text/html":
                            message = part.get_payload(decode=True)
                            print("Message: \n", message.decode())


                            type_of_message=classify_text_msg(message.decode())[0]

                            if  type_of_message=="spam":


                                          messages_recieved_by_sequence_spam.append(message.decode())

                            else:

                                          messages_recieved_by_sequence_ham.append(message.decode())



                            print("==========================================\n")
                            break

                    mess_sub.append(email_message["subject"])
                    mess_to.append(email_message["to"])
                    mess_from.append(email_message["from"])
                    mess_date.append(email_message["date"])
                         #   print(messages_recieved_by_sequence)

                           # test_string =messages_recieved_by_sequence



                return mess_sub,mess_to,mess_from,mess_date,messages_recieved_by_sequence_ham,messages_recieved_by_sequence_spam
# initializing split word
           # spl_word = 'text:'
  
# printing original string 
#print("The original string : " + str(test_string))
  
# printing split string 
#print("The split string : " + str(spl_word))
  
# using split()
# Get String after substring occurrence
            #res = test_string.partition(spl_word)[2]
  
# print result
            #print(res)

