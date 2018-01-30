#!/usr/bin/python

import sys
import os
import smtplib
import getpass

email_origin = raw_input('E-mail: ')
password = getpass.getpass('Password: ')
email_destination = raw_input('\nTo: ')

message = raw_input('Message: ')
total = input('Number of send: ')

server = 'smtp.gmail.com'
port = 25

try: 
	gmail = smtplib.SMTP(server, port)
   	gmail.ehlo()
   	gmail.starttls()
   	gmail.login(email_origin, password)
   
   	for i in range(1, total + 1):
		subject = os.urandom(9)
		msg = 'From: ' + email_origin + '\nSubject: ' + subject + '\n' + message
		gmail.sendmail(email_origin, email_destination, msg)
		print "\re-mails sent: %i" % i
		sys.stdout.flush()
	gmail.quit()
	print '\n Done !!'
except KeyboardInterrupt:
	print 'Canceled'
	sys.exit()
except smtplib.SMTPAuthenticationError: 
	print('\n Error: E-mail or Password incorrect.')
	sys.exit()
