# crypto_app/tasks.py

from celery import shared_task
from .coinmarketcap import CoinMarketCap

@shared_task
def fetch_crypto_data(coins):
    cmc = CoinMarketCap()
    data = {}
    for coin in coins:
        data[coin] = cmc.scrape_coin_data(coin)
    cmc.close()
    return data
