import pandas as pd

def find_best_prices(items, data):
    output = []
    for item in items:
        subset = data[data['item'].str.lower() == item]
        if not subset.empty:
            best = subset.loc[subset['price'].idxmin()]
            output.append({
                'item': item,
                'store': best['store'],
                'price': float(best['price']),
                'link': best['link']
            })
        else:
            output.append({
                'item': item,
                'store': 'Not Found',
                'price': '-',
                'link': '#'
            })
    return output