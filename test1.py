from urllib.error import HTTPError, URLError
from urllib.request import urlopen
from bs4 import BeautifulSoup
try:
    html = urlopen('https://github.com/lmcworld?tab=repositories')
except HTTPError as e:
    print(e)
except URLError as e:
    print("the server can't be find")
else:

    bs = BeautifulSoup(html,'html.parser')
    with open('web1.txt','w',encoding='utf-8') as f:
        f.write(str(bs))
    print(bs.h1)

