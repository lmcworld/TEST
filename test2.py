from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(),'html.parser')
nameList = bs.find_all('span',{'class':'green'})

for name in nameList:
    print(name.get_text())
h_list = bs.find_all(['h1','h2','h3','h4','h5'])
print(h_list)

class_list = bs.find_all('span',{'class':{'green','red'}})
for class1 in class_list:
    print(class1.get_text())

nameList2 = bs.find_all(text='Anna')
print(nameList2)
