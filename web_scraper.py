import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.service import Service
import time

# URL of the website 
url = "https://www.cnbc.com/world/?region=world"

# Option
options = Options()

# service
gecko_service = Service("/usr/local/bin/geckodriver")

# profile
profile = FirefoxProfile("/home/ysun9487/.mozilla/firefox/l9wjraf1.default-release")
options.profile = profile

# setup web-driver
driver = webdriver.Firefox(service = gecko_service, options=options)

driver.get(url)
time.sleep(10)

# Send a GET request
response = requests.get(url)

# Parse the html content
soup_news = BeautifulSoup(response.text, "html.parser")
soup_market = BeautifulSoup(driver.page_source, "html.parser")

# Find market banner
market_banner = soup_market.find("div", class_="MarketsBanner-main")

# Find latest news
latest_news = soup_news.find("div", class_="LatestNews-isHomePage LatestNews-isIntlHomepage")

# write the collected data to raw_data folder as web_data.html
with open("data/raw_data/web_data.html", "w", encoding = "utf-8") as file:
	file.write(str(market_banner))
	file.write(str(latest_news))


