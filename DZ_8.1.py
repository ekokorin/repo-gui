import re


def email_parse(email_address):
    msg = f'wrong e-mail: {email_address}'
    s = {'username': '',
         'domain': ''}
    t = re.match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$', email_address)
    if t is None:
        raise ValueError(msg)
    result = re.split(r'@', email_address)
    s['username'] = result[0]
    s['domain'] = result[1]
    print(s)


a = input('input e-mail: ')
email_parse(a)
