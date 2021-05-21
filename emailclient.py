import smtplib, ssl
import time

port = 587  # For starttls
smtp_server = "smtp.office365.com" #smtp.gmail.com #smtp.office365.com
sender_email = input("What is your email? ")
receiver_email = input("Who are you sending the email to? ")
password = input("Type your password and press enter:")
subject = input("Email Subject: ")
emailmessage = input("Message: ")
message = (f"""\
Subject: {subject}

{emailmessage}""")
emailtime = int(input("How many times do you wish to send the email? "))
newtime = emailtime
message_amount = 1
for i in range(emailtime):
  context = ssl.create_default_context()
  with smtplib.SMTP(smtp_server, port) as server:
    try:
      server.ehlo()  # Can be omitted
      server.starttls(context=context)
      server.ehlo()  # Can be omitted
      server.login(sender_email, password)
      server.sendmail(sender_email, receiver_email, message)
      print(f"Message number {message_amount} has been sent!")
      message_amount += 1
    except Exception as e:
      print("Something went wrong, please check you entered info correctly.")
      time.sleep(2)
      print(f"Quitting with error code {e}!")
      quit()
print("Completed operations.")
time.sleep(2)
