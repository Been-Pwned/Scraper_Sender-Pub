import requests
import re
from requests_html import HTMLSession
import csv
import smtplib

#Default Messages
error = "[ERROR] invalid option please use one of the options specified above"
done = "[DONE] Program finished running. All processes finished successfully"

#Scraping Function
def email_scraper():
	url = input("This only works for one url at a time. Input a url here: ")
	EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
	session = HTMLSession()
	r = session.get(url)	
	java = input("Does the website store emails in javascript? ")
	if java == "yes":
		r.html.render()
	elif java == "no":
		pass
	else:
		print(error)

	csv_file_name = input("What is the name of the csv file that you would like to save to? ")
	email_together = []
	with open(csv_file_name, 'w', newline = '') as new_file:
		csv_writer = csv.writer(new_file)
		for re_match in re.finditer(EMAIL_REGEX, r.html.raw_html.decode()):

			email = re_match.group()
			email_together.append(email)
		csv_writer.writerow(email_together)



#Email Function
def email_sender():
	file_name = input("What is the name of the file youw ould like to use?")
	subject = str(input("What do you want the subject of the email to be?  "))
	body = str(input("What do you want the body of the email to be?  "))
	app_code = str(input("Put in your appcode. You can get an appcode for your gmail account after enabling 2 factor auth: "))
	email_address = str(input("Input your the email address you would like to use: "))
	with open(file_name, 'r') as csv_file:
		csv_reader = csv.reader(csv_file)

		for line in csv_reader:
			with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
				smtp.ehlo()
				smtp.starttls()
				smtp.ehlo()

				smtp.login(email_address, app_code)

				subject = subject
				body = body

				msg = f'Subject: {subject}\n\n{body}'

				smtp.sendmail(email_address, line, msg)


#User_Options Config

options = input("Write premade to use premade .csv file or scrape to enter websites to scrape: ")

if options == "premade":
	print("You have selected the premade file option. Note that you can only send to 500 different email addresses with this tool(Unless you are going to use multiple accounts). \n	Starting Premade Option....	")
	email_sender()
	print(done)
elif options == "scrape":
	print("You have selected the scrape option. Note that this option will store a version of chromium.(for python) \n Starting... Scrape Option ")
	email_scraper()
	send_emails = input("Would you like to send emails from the new csv file?")
	if send_emails == "yes":
		email_sender()
		print(done)
	elif send_emails == "no":
		print(done)
	else:
		print(error)

else:
	print(error)