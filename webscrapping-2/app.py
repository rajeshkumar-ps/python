import requests
from bs4 import BeautifulSoup
page = requests.get("https://books.toscrape.com/")
soup = BeautifulSoup(page.content, "html.parser") # Parse the HTML content
# print(soup.prettify()) # Print the parsed HTML in a pretty format
print(soup.find("h1").string)