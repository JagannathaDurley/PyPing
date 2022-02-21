#IMPORATING
import time
import os
import datetime
import smtplib
import admin

if not admin.isUserAdmin():
    admin.runAsAdmin()
#SETUP
print("Welcome to Jag's advanced Python Ping script.")
print("Specify the IP / DOMAIN you want to ping")
hostname = input()
print("Please specify how often you would like to ping this website! For example 1 minute would be 60. Or 5 minutes would be 300.")
howoftenping = int(input())
print("Now for the automatic emailing... Please type in the email address you would like to send the message from. Please use a GMAIL account.")
emailaddress = input()
print("Now enter your password.")
emailpassword = input()
print("Finally, enter the email address you would like the emails to be sent to.")
sendemail = input()

#IMPORTANT VARIABLES
onoff = "off"
dateon = datetime.datetime.now()
time.sleep(5)
dateoff = datetime.datetime.now()


 

#MAIN CODE
while (True):
    response = os.system("ping -c 1 " + hostname)

    if response == 0:
        print (hostname, 'is online!')
        if onoff == "off":
            onoff = "on"
            dateon = datetime.datetime.now()
            offtime = dateon - dateoff
            print(f"{hostname} was offline for: {offtime}")
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()

                smtp.login(emailaddress, emailpassword)

                subject = 'Uptime Alert On!'
                body = f'{hostname} is now online! The current time is {dateon}. {hostname} was offline for {offtime}.'
                msg = f'Subject: {subject}\n\n{body}'

                smtp.sendmail(emailaddress, f'{sendemail}', msg)
    else:
        print (hostname, 'is offline!')
        if onoff == "on":
            onoff = "off"
            #send email saying offline
            dateoff = datetime.datetime.now()
            offtime = dateon - dateoff
            #SMTP
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()

                smtp.login(emailaddress, emailpassword)

                subject = 'Uptime Alert Off!'
                body = f'{hostname} is now offline! The current time is {dateoff}. You will recieve another email when {hostname} is back online.'
                msg = f'Subject: {subject}\n\n{body}'

                smtp.sendmail(emailaddress, f'{sendemail}', msg)
    time.sleep(howoftenping)

