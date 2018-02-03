import urllib2
from bs4 import BeautifulSoup

quote_page = 'https://www.bloomberg.com/quote/SSETRFI:AB'
page = urllib2.urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
name_box = soup.find('h1', attrs={'class': 'name'})
name = name_box.text.strip() # strip() is used to remove starting and trailing
print name
price_box = soup.find('div', attrs={'class':'price'})
price = price_box.text
print price







quote_page = 'https://www.bloomberg.com/quote/SCAASEQ:AB'
page = urllib2.urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
name_box = soup.find('h1', attrs={'class': 'name'})
name = name_box.text.strip() # strip() is used to remove starting and trailing
print name
price_box = soup.find('div', attrs={'class':'price'})
price = price_box.text
print price

