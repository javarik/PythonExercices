# coding=utf-8
import smtplib
import datetime

# Specifying the from and to addresses

fromaddr = 'checker iPad'
toaddrs  = 'toadress'

# Writing the message (this message will appear in the email)

msg = 'Une alerte puisard a été levé'

# Gmail Login

username = 'rasppuisard@gmail.com'
password = 'checker iPad'

# Sending the mail  

#server = smtplib.SMTP('smtp.gmail.com:587')
#server.starttls()
#server.login(username,password)
#server.sendmail(fromaddr, toaddrs, msg)
#server.quit()