import csv
from bs4 import BeautifulSoup

# Read the "web_data.html" file
with open('data/raw_data/web_data.html', 'r', encoding='utf-8') as file:
    content = file.read()

# Parse the HTML content
soup = BeautifulSoup(content, 'html.parser')

# Extract data from the Market banner
market_cards_container = soup.find('div', class_='MarketsBanner-main')

# Create a list to store all the market_data
market_data = []

if market_cards_container:
    market_cards = market_cards_container.find_all('a', class_='MarketCard-container')
    for market_card in market_cards:
        marketCard_symbol = market_card.find('span', class_='MarketCard-symbol').text.strip()
        marketCard_stockPosition = market_card.find('span', class_='MarketCard-stockPosition').text.strip()
        marketCard_changePct = market_card.find('span', class_='MarketCard-changesPct').text.strip()
        market_data.append((marketCard_symbol, marketCard_stockPosition, marketCard_changePct))

    # Store the Market banner data in a CSV file
    if market_data:
        with open('data/processed_data/market_data.csv', 'w', newline='', encoding='utf-8') as market_csv:
            writer = csv.writer(market_csv)
            writer.writerow(['Market Symbol', 'Stock Position', 'Change Percentage'])
            writer.writerows(market_data)
        print("Market data stored in market_data.csv")
else:
    print("Market banner container not found.")

# Extract data from the Latest News section
latest_news_section = soup.find('div', class_='LatestNews-isHomePage LatestNews-isIntlHomepage')

# Create a list to store all the news data
news_data = []



if latest_news_section:
     news_entries = latest_news_section.find_all('li')
     for entry in news_entries:
          timestamp = entry.find('time', class_='LatestNews-timestamp').text.strip()
          title = entry.find('a', class_='LatestNews-headline')['title'].strip()
          link = entry.find('a', class_='LatestNews-headline')['href'].strip()
          news_data.append([timestamp, title, link])
else:
     print("Latest News data not found.")


# Store the News data in a CSV file
if news_data:
	with open('data/processed_data/news_data.csv', 'w', newline='', encoding='utf-8') as news_csv:
		writer = csv.writer(news_csv)
		writer.writerow(['Timestamp', 'Title', 'Link'])
		writer.writerows(news_data)
	print("News data stored in news_data.csv")
