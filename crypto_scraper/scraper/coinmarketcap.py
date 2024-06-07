import requests
from bs4 import BeautifulSoup
import json

class CoinMarketCap:
    def __init__(self):
        self.base_url = "https://coinmarketcap.com/currencies/"

    def get_coin_data(self, coin_name):
        url = f"{self.base_url}{coin_name}/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        data = {}
        data["price"] = self.extract_price(soup)
        data["price_change"] = self.extract_price_change(soup)
        data["market_cap"] = self.extract_market_cap(soup)
        data["market_cap_rank"] = self.extract_market_cap_rank(soup)
        data["volume"] = self.extract_volume(soup)
        data["volume_rank"] = self.extract_volume_rank(soup)
        data["volume_change"] = self.extract_volume_change(soup)
        data["circulating_supply"] = self.extract_circulating_supply(soup)
        data["total_supply"] = self.extract_total_supply(soup)
        data["diluted_market_cap"] = self.extract_diluted_market_cap(soup)
        data["contracts"] = self.extract_contracts(soup)
        data["official_links"] = self.extract_official_links(soup)
        data["socials"] = self.extract_socials(soup)

        return data

    def process_data(self, data):
        return data

    def send_json_response(self, data):
        return json.dumps(data)

    def extract_price(self, soup):
        price_element = soup.find("div", {"class": "priceValue___11gHJ"})
        return float(price_element.text.strip().replace("$", ""))

    def extract_price_change(self, soup):
        price_change_element = soup.find("span", {"class": "change___24pjr"})
        return float(price_change_element.text.strip().replace("%", ""))

    def extract_market_cap(self, soup):
        market_cap_element = soup.find("div", {"class": "marketCap___3xwPV"})
        return int(market_cap_element.text.strip().replace("$", "").replace(",", ""))

    def extract_market_cap_rank(self, soup):
        market_cap_rank_element = soup.find("div", {"class": "marketCapRank___2tQZS"})
        return int(market_cap_rank_element.text.strip().replace("#", ""))

    def extract_volume(self, soup):
        volume_element = soup.find("div", {"class": "volume___3xwPV"})
        return int(volume_element.text.strip().replace("$", "").replace(",", ""))

    def extract_volume_rank(self, soup):
        volume_rank_element = soup.find("div", {"class": "volumeRank___2tQZS"})
        return int(volume_rank_element.text.strip().replace("#", ""))

    def extract_volume_change(self, soup):
        volume_change_element = soup.find("span", {"class": "change___24pjr"})
        return float(volume_change_element.text.strip().replace("%", ""))

    def extract_circulating_supply(self, soup):
        circulating_supply_element = soup.find("div", {"class": "circulatingSupply___3xwPV"})
        return int(circulating_supply_element.text.strip().replace(",", ""))

    def extract_total_supply(self, soup):
        total_supply_element = soup.find("div", {"class": "totalSupply___3xwPV"})
        return int(total_supply_element.text.strip().replace(",", ""))

    def extract_diluted_market_cap(self, soup):
        diluted_market_cap_element = soup.find("div", {"class": "dilutedMarketCap___3xwPV"})
        return int(diluted_market_cap_element.text.strip().replace("$", "").replace(",", ""))

    def extract_contracts(self, soup):
        contracts_elements = soup.find_all("div", {"class": "contract___3xwPV"})
        contracts = []
        for contract_element in contracts_elements:
            contract = {}
            contract["name"] = contract_element.find("span", {"class": "contractName___2tQZS"}).text.strip()
            contract["address"] = contract_element.find("span", {"class": "contractAddress___2tQZS"}).text.strip()
            contracts.append(contract)
        return contracts

    def extract_official_links(self, soup):
        official_links_elements = soup.find_all("div", {"class": "officialLink___3xwPV"})
        official_links = []
        for official_link_element in official_links_elements:
            official_link = {}
            official_link["type"] = official_link_element.find("span", {"class": "officialLinkType___2tQZS"}).text.strip()
            official_link["url"] = official_link_element.find("a").get("href")
            official_links.append(official_link)
        return official_links

    def extract_socials(self, soup):
        socials_elements = soup.find_all("div", {"class": "social___3xwPV"})
        socials = []
        for social_element in socials_elements:
            social = {}
            social["type"] = social_element.find("span", {"class": "socialType___2tQZS"}).text.strip()
            social["url"] = social_element.find("a").get("href")
            socials.append(social)
        return socials