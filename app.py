from flask import Flask, request
from nse_scraper import fetch_delivery
from filter_data import filterDeliveryData

app = Flask(__name__)

@app.route('/stock/<symbol>/delivery', methods=['GET'])
def stockDelivery(symbol):
  print("calll data stock delivery")
  start_date = request.args.get('start_date')
  end_date = request.args.get('end_date')
  if start_date and end_date:
    data = filterDeliveryData(fetch_delivery(symbol, start_date, end_date)['data'][::-1])
  return {'data': data}
    

@app.route('/')
def home():
    return "Hello, Flask!"


if __name__ == '__main__':
    app.run(port=5001, debug=True)