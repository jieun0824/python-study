import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "http://www.daum.net/"
response = requests.get(url)

rank = 1
soup = BeautifulSoup(response.text, 'html.parser')

# file = open("daum.html","w")
# file.write(response.text)
# file.close()


# print(soup.title)
# print(soup.title.string)


# print(soup.span)
# print(soup.findAll('span'))

results = soup.findAll("a","link_favorsch")

print(response.text)

search_rank_file = open("rankresult.txt","w")

print(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))

for result in results:
    search_rank_file.write(str(rank)+"위:"+result.get_text()+"\n")
    print(rank,"위 : ",result.get_text(),"\n")
    rank += 1
