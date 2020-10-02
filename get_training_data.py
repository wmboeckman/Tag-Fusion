# import libraries
import urllib3
from bs4 import BeautifulSoup

# specify the url
quote_page = 'https://onezero.medium.com/this-is-how-much-youtube-paid-me-for-my-1-000-000-viewed-video-1453cad73847'
# query the website and return the html to the variable ‘page’
page = urllib3.urlopen(quote_page)
# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')
# Take out the <div> of name and get its value
name_box = soup.find('h1', attrs={'class': 'name'})
name = name_box.text.strip()  # strip() is used to remove starting and trailing
print(name)
# get the index price
price_box = soup.find('div', attrs={'class':'price'})
price = price_box.text
print(price)