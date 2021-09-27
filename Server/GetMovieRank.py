# import requests
# from bs4 import BeautifulSoup
#
# # 요청을 막아둔 사이트들이 많음. 브라우저에서 엔터친것처럼 효과를 내줌
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)
#
# # beautiful soup 형태로 만들기
# soup = BeautifulSoup(data.text, 'html.parser')
# trs = soup.select('#old_content > table > tbody > tr')
#
# for tr in trs:
#
#     a_tag = tr.select_one('td.title > div > a')
#     if a_tag is not None:
#         title = a_tag.text
#         star = tr.select_one('td.point').text
#         rank = tr.select_one('td:nth-child(1) > img')['alt']
#
#         print(rank, title, star)


# from pymongo import MongoClient
# client = MongoClient('localhost', 27017)
# db = client.dbhwanE
#
#
#
# result = db.movies.find()
#
# for r in result:
#     print(r["title"])



# import requests
# from bs4 import BeautifulSoup
# from pymongo import MongoClient
# client = MongoClient('localhost', 27017)
# db = client.dbhwanE

# url = "https://finance.naver.com/sise/sise_market_sum.nhn?page=1"
#
# res = requests.get(url)
# soup = BeautifulSoup(res.text, 'lxml')
#
# stock_list = soup.find("table", attrs={"class": "type_2"}).find("tbody").find_all("tr")
#
# for stock in stock_list:
#      if len(stock) > 1 :
#           tmp = stock.get_text().split()
#           put_data = {
#               'KOSPI': tmp[0],
#               'title': tmp[1],
#               'capitalization': tmp[6],
#               'comparison' : tmp[4],
#               'nowmoney' : tmp[2]
#           }
#           db.kospinews.insert_one(put_data)

# import requests
# from bs4 import BeautifulSoup
# from pymongo import MongoClient
# client = MongoClient('localhost', 27017)
# db = client.dbhwanE
#
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)
#
# soup = BeautifulSoup(data.text, 'html.parser')
#
# movies = soup.select("#old_content > table > tbody > tr")
#
#
# for movie in movies:
#     movie_name = movie.select_one("td.title > div > a")
#     if movie_name is not None:
#         movie_ranking = movie.select_one("td:nth-child(1) > img")["alt"]
#         movie_title = movie_name.text
#         movie_point = movie.select_one("td.point").text
#
#         put_data = {
#             'ranking': movie_ranking,
#             'title': movie_title,
#             'point': movie_point
#         }
#
#         print(put_data)




import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbhwanE

data = requests.get('https://music.bugs.co.kr/chart')
soup = BeautifulSoup(data.text, 'html.parser')
rank_lists = soup.select('.list > tbody > tr')

for rank_list in rank_lists:
    ranking = rank_list.select_one('td > div.ranking > strong').text
    m_title = rank_list.select_one('th > .title > a').text
    m_artist = rank_list.select_one('td.left > .artist > a').text

    put_data = {
        'ranking': ranking,
        'title': m_title,
        'artist': m_artist
    }
    db.music.insert_one(put_data)