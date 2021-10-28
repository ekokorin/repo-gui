import requests
from datetime import datetime

"""Вывод валюты на указанную дату"""


def currency_rates(value):
    URL = 'http://www.cbr.ru/scripts/XML_daily.asp'
    dict_daily = {}
    response = requests.get(URL).text
    index = response.find('Date="')
    year = int(response[index + 12:index + 16])
    month = int(response[index + 9:index + 11])
    day = int(response[index + 6:index + 8])
    data = datetime(year, month, day)
    while response.find('<CharCode>') != -1:
        x = response.find('<CharCode>')
        char_code = f'{response[x + 10:x + 13]}'
        y = response.find('<Value>')
        val = f'{response[y + 7:y + 14]}'
        val = val.replace(',', '.')
        float(val)
        dict_daily[char_code] = val
        response = response[y + 14:]
    if value in dict_daily.keys():
        print(f'Курс валюты {value} на {data}')
        print(dict_daily[value])
    else:
        print(None)


currency_rates('USD')

currency_rates('EUR')

currency_rates('DGT')
