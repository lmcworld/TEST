from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(),'html.parser')
a = ['a','b','c','d']
b = {'a':1,
     'b':2,
     'c':3,
     'd':[11,22,33],
     'e':{'111':'aaa','222':'bbb'},
     'f':(1111,2222)
     }
with open('name1.json','w') as f1:
    json.dump(b,f1)
with open('name1.json') as f2:
    a = json.load(f2)
print(a['a'])
print(a['b'])
print(a['c'])
print(a['d'])
print(a['e'])
print(a['f'])
