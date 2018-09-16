import re

post_code_pattern = re.compile('\d{2}-\d{3}')

emaill_patern = re.compile('[\w\-\.]+@[\w\-\.]+\.\w+')
date_pattern = re.compile('\d{1,2} \w{3} \d{4}')


with open('input.txt') as f:
    tekst = f.read()
    kody = post_code_pattern.findall(tekst)
    maile = emaill_patern.findall(tekst)
    daty = date_pattern.findall(tekst)
    print(kody)
    print(maile)
    print(daty)