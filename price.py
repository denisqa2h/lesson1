def get_summ(one, two, delimiter='&'):
    return (one + ' ' + delimiter + ' ' + two)

print(get_summ('learn', 'python').upper())

def format_price(price:int):
    price = int(price)
    return f'Цена: {price} руб.'

result = format_price(56.24)
print(result)