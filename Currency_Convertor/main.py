import requests
URL = 'http://data.fixer.io/api/latest?access_key=1409832e403af7ca3a9897f49c63dd44'


def currency_conversion():
    from_currency = input('From Currency :')
    to_currency = input('To Currency   :')
    amount = int(input('Amount        :'))
    response = requests.get(URL)
    rate = response.json()['rates'][from_currency]
    amount_in_EUR = amount / rate
    amount = amount_in_EUR * (response.json()['rates'][to_currency])
    amount = round(amount, 2)
    print(amount)
    again = input('Again ?(yes):')
    if again == 'yes':
        currency_conversion()


currency_conversion()