import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.co.uk/Samsung-Galaxy-Dual-SIM-Android-Smartphone-Prism-Black/dp/B07NWLZMGJ/ref=sr_1_3?keywords=samsung+s10&qid=1570265281&s=electronics&sr=1-3'
headers = {
		"user_Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}
def price_check():
	page = requests.get(URL,headers = headers)
	soup = BeautifulSoup(page.content,'html.parser')
	title = soup.find(id="productTitle").get_text()
	title = title.strip()	
	price = soup.find(id="priceblock_ourprice").get_text()
	price = price.replace('£','')
	price = float(price)
	meta = {price:price, title:title}
	if price:
		mailer(meta)

def mailer(price):
	# print (price)
	server =smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login('sameermasti00@gmail.com','htzunblrqwcaqfiv')
	subject = 'Price Upadated!!'
	Body = 'Check Amazon.uk https://www.amazon.co.uk/Samsung-Galaxy-Dual-SIM-Android-Smartphone-Prism-Black/dp/B07NWLZMGJ/ref=sr_1_3?keywords=samsung+s10&qid=1570265281&s=electronics&sr=1-3'
	msg =f"subject: {subject}\n\n{Body}"
	server.sendmail(
		'sameermasti00@gmail.com',
		'sreejithsathyan95@gmail.com',
		msg)
	print ('ddddddddddddddddddddddddd',server)
	print ('Email to Sreejith')
	server.quit()
while (True):
	price_check()
	time.sleep(60)