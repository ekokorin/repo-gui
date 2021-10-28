import utils

"""Вывод валюты на указонну дату"""


val = input('Введите валюту, по которой хотите узнать курс: ')
val = val.upper()
utils.currency_rates(val)
