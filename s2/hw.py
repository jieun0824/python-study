import requests
import pandas as pd
from bs4 import BeautifulSoup
import bs4
import json

key = 'a8e597633acca03091ad5fba598b58a7'
url = "http://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=" + key
parameter = {"directorNm": "봉준호"}
req = requests.get(url, parameter)
#공공데이터에 등록된 xml파일에 접
html= req.json()
html
DF = pd.DataFrame(html['movieListResult']["movieList"])
## 연도로 다시 정렬
DF = DF.sort_values("prdtYear")

## 컬럼 형식 바꾸기
DF['directors'] = DF['directors'].apply(lambda x : x[0]['peopleNm'])
DF['companys'] = DF['companys'].apply(lambda x : x[0]['companyNm'] if x else x)

DF

date = pd.date_range('20180101', '20181231')
date

Time = []
for time in date:    
    Time.append(date.strftime("%Y%m%d").tolist())
    
time_list=Time[0] ##12번 반복됨을 알아서 그중에서 하나만 사용

requestData2 = requests.get(url+str(time_list[k])+'')
data_2 = requestData2.json()
data = data_2['boxOfficeResult']['dailyBoxOfficeList']
df = pd.DataFrame.from_dict(data)
df_default = df_default.append(df)
df_default

data = []
key = 'a8e597633acca03091ad5fba598b58a7'
url = "http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=" + key + "&targetDt="
df_default = pd.DataFrame()
for k in range(len(time_list)):
    requestData2 = requests.get(url+str(time_list[k])+'')
    try: 
        data_2 = requestData2.json()
        data = data_2['boxOfficeResult']['dailyBoxOfficeList']
        df = pd.DataFrame.from_dict(data)
        df_default = df_default.append(df)
    except:
        pass

df_default.to_csv('data_result.csv',encoding='utf-8', index = False) ## 한글이 포함되어 있으므로, encoding에 utf-8을 넣는다.-> 파일을 저장한다.

## 출력을 통해서 확인
pd.read_csv('data_result.csv')