import utils


val = input('Введите валюту, по которой хотите узнать курс: ')
val = val.upper()
utils.currency_rates(val)
