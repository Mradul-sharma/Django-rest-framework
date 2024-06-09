# crypto_app/coinmarketcap.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

class CoinMarketCap:
    def __init__(self):
        options = Options()
        options.headless = True
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def scrape_coin_data(self, coin):
        url = f"https://coinmarketcap.com/currencies/{coin}/"
        self.driver.get(url)
        time.sleep(2)  # Wait for the page to load completely
        
        data = {}
        try:
            data['price'] = float(self.driver.find_element_by_css_selector('.priceValue span').text.strip('$').replace(',', ''))
            data['price_change'] = float(self.driver.find_element_by_css_selector('.sc-15yy2pl-0.kAXKAX').text.strip('%').replace(',', ''))
            data['market_cap'] = int(self.driver.find_element_by_css_selector('div.statsValue span').text.strip('$').replace(',', ''))
            data['volume'] = int(self.driver.find_element_by_xpath("//div[span='Volume 24h']//span[@class='statsValue']").text.strip('$').replace(',', ''))
            # Add more fields as needed
        except Exception as e:
            data['error'] = str(e)
        
        return data

    def close(self):
        self.driver.quit()
