from flask import Flask, request
from nse_scraper import fetch_delivery
from filter_data import filterDeliveryData
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/stock/<symbol>/delivery', methods=['GET'])
def stockDelivery(symbol):
  data = []
  end_date = request.args.get('date')
  start_date = (datetime.strptime(end_date.strip("'\" "), '%d-%m-%Y') - timedelta(days=10)).strftime('%d-%m-%Y')
  if start_date and end_date:
    data = filterDeliveryData(fetch_delivery(symbol, start_date, end_date)['data'][::-1])
  return {'data': data}    

@app.route('/')
def home():
  return "Hello, Flask!"


if __name__ == '__main__':
  app.run()
