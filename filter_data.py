def filterDeliveryData(data):
  filter_data = []
  for d in data:
    high_price = d['CH_TRADE_HIGH_PRICE']
    low_price = d['CH_TRADE_LOW_PRICE']
    open_price = d['CH_OPENING_PRICE']
    close_price = d['CH_CLOSING_PRICE']

    trades =  d['CH_TOTAL_TRADES']
    traded_qty = d['CH_TOT_TRADED_QTY']
    delivery_perc = d['COP_DELIV_PERC']
    delivery_qty = d['COP_DELIV_QTY']
    vwap = d['VWAP']
    date = d['CH_TIMESTAMP']

    high_price_52_week = d['CH_52WEEK_HIGH_PRICE']
    low_price_52_week = d['CH_52WEEK_LOW_PRICE']

    filter_data.append({'open': open_price, 'close': close_price, 'high': high_price, 'low': low_price,
    'trades': trades, 'traded_qty': traded_qty, 'delivery_perc': delivery_perc,
    'delivery_qty': delivery_qty, 'vwap': vwap, 'date': date, 'week_52_high_price': high_price_52_week,
    'week_52_low_price': low_price_52_week })
  return filter_data