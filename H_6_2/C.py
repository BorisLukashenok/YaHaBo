import pandas as pd


def cheque(lst: pd.Series, **arg):

    df = pd.DataFrame({'product': sorted(arg.keys())})
    df['price'] = lst[df['product'].values].values
    df['number'] = [arg[i] for i in sorted(arg.keys())]
    df['cost'] = df.price * df.number
    return df


products = ['bread', 'milk', 'soda', 'cream']
prices = [37, 58, 99, 72]
price_list = pd.Series(prices, products)
result = cheque(price_list, soda=3, milk=2, cream=1)
print(result)
