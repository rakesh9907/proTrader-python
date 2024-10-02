def filterDeliveryData(data):
  current_data = data[0]
  rest_data = data[1:]
  final_data = rest_data[:5]

  if len(final_data) < 5:
    return "Data should be grether then 5"

  high_price = current_data['CH_TRADE_HIGH_PRICE']
  low_price = current_data['CH_TRADE_LOW_PRICE']
  open_price = current_data['CH_OPENING_PRICE']
  close_price = current_data['CH_CLOSING_PRICE']

  trades =  current_data['CH_TOTAL_TRADES']
  traded_qty = current_data['CH_TOT_TRADED_QTY']
  delivery_perc = current_data['COP_DELIV_PERC']
  delivery_qty = current_data['COP_DELIV_QTY']
  vwap = current_data['VWAP']
  date = current_data['CH_TIMESTAMP']

  high_price_52_week = current_data['CH_52WEEK_HIGH_PRICE']
  low_price_52_week = current_data['CH_52WEEK_LOW_PRICE']

  total_delivery_qty = sum(d['COP_DELIV_QTY'] for d in final_data) / 5
  total_volume_qty = sum(d['CH_TOT_TRADED_QTY'] for d in final_data) / 5

  delivery_time = current_data['COP_DELIV_QTY'] / total_delivery_qty
  volume_time = current_data['CH_TOT_TRADED_QTY'] / total_volume_qty

  result = {'open': open_price, 'close': close_price, 'high': high_price, 'low': low_price,
  'trades': trades, 'traded_qty': traded_qty, 'delivery_perc': delivery_perc,
  'delivery_qty': delivery_qty, 'vwap': vwap, 'date': date, 'week_52_high_price': high_price_52_week,
  'week_52_low_price': low_price_52_week, 'delivery_time': delivery_time, 'volume_time': volume_time }

  return result