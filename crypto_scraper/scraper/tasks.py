from celery import shared_task
from .models import ScrapingTask
from .coinmarketcap import CoinMarketCap

coin_market_cap = CoinMarketCap()

@shared_task
def scrape_coin_data(job_id):
    scraping_task = ScrapingTask.objects.get(id=job_id)
    coin_name = scraping_task.coin
    try:
        coin_data = coin_market_cap.get_coin_data(coin_name)
        processed_data = coin_market_cap.process_data(coin_data)
        json_response = coin_market_cap.send_json_response(processed_data)
        scraping_task.output = json_response
        scraping_task.completed = True
        scraping_task.save()
    except Exception as e:
        scraping_task.error = str(e)
        scraping_task.completed = True
        scraping_task.save()
