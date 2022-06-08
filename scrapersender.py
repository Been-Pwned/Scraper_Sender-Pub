import requests
import yagmail


# find websites to scrape emails from
website_list = [""]

#Configure User Options
online = input("Do you want to scrape websites or use a premade .csv file?(enter scrape to scrape or premade for premade file.)  ")

if online == "scrape":
	print("[SCRAPING]")
elif online == "premade":
	print("input file name")

else:
	print("[ERROR:] Invalid option please input one of the options specified in initial question.")



# Send emails from the csv file

yagmail.register('thisemailisdefinetlynotanad@gmail.com', 'IloveAsuseventhoughitsucks')

reciever = "astoshanstuerm1@gmail.com"
body = "Hello there from yagmail"


yag = yagmail.SMTP("thisemailisdefinetlynotanad@gmail.com")
yag.send(
	to=reciever,
	subject="Yagmail test with attachement",
	contents=body
)








