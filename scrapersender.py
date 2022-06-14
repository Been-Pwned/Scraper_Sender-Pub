
# # find websites to scrape emails from
# website_list = [""]

# #Configure User Options
# online = input("Do you want to scrape websites or use a premade .csv file?(enter scrape to scrape or premade for premade file.)  ")
# # app_code = input("input your application code provided by your google account: ")
# # email_address = input("input the email you would like to use(note: This email sender is autoconfigured for gmail if you need to use a different server change the piece of code bellow): ")

# if online == "scrape":
# 	print("[SCRAPING]")
# elif online == "premade":
# 	file_name = input("What is the name of the file youw ould like to use?")
# 	with open(file_name, 'r') as csv_file:
# 		csv_reader = csv.reader(csv_file)
# else:
# 	print("[ERROR:] Invalid option please input one of the options specified in initial question.")



# # Send emails from the csv file
# import smtplib

app_code = "youdon'tgetmycode"#This is only for testing purposes the commented input is what you will use above
email_address = "thisemailisdefinetlynotanad@gmail.com"

# with open("base.csv", 'r') as csv_file:
# 	csv_reader = csv.reader(csv_file)

# for line in csv_reader:
# 	with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
# 		smtp.ehlo()
# 		smtp.starttls()
# 		smtp.ehlo()

# 		smtp.login(email_address, app_code)

# 		subject = str(input("What do you want the subject of the email to be?  "))
# 		body = str(input("What do you want the body of the email to be?  "))

# 		msg = f'Subject: {subject}\n\n{body}'

# 		smtp.sendmail(email_address, "astoshanstuerm1@gmail.com", msg)


import requests
import csv



#Scraping Function


#Email Function
import smtplib
def email_sender():
	file_name = input("What is the name of the file youw ould like to use?")
	subject = str(input("What do you want the subject of the email to be?  "))
	body = str(input("What do you want the body of the email to be?  "))
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

				smtp.sendmail(email_address, "astoshanstuerm1@gmail.com", msg)




#User_Options Config

email_sender()

