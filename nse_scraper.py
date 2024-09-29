import requests
from datetime import datetime


# URL of the NSE website
nse_url = 'https://www.nseindia.com'

# Headers to mimic a real browser request
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
  'Accept-Encoding': 'gzip, deflate, br',
  'Accept-Language': 'en-US,en;q=0.5',
  'Connection': 'keep-alive',
  'Upgrade-Insecure-Requests': '1'
}

def fetch_nse_data():
  session = requests.Session()
  response = session.get(nse_url, headers=headers)

  if response.status_code == 200:
    print("Successfully retrieved response from NSE")
    return session
  else:
    print(f"Failed to retrieve response from NSE. Status code: {response.status_code}")

def fetch_delivery(symbol, start_date, end_date):
  session = fetch_nse_data()
  target_url = f'https://www.nseindia.com/api/historical/securityArchives?from={start_date.strip("'\" ")}&to={end_date.strip("'\" ")}&symbol={symbol}&dataType=priceVolumeDeliverable&series=ALL'
  response = session.get(target_url, headers=headers)
  data = response.json()
  return data
