import urllib.request
#strat (page-1)*20
# 下载豆瓣电影前十部
# 1 请求对象的定制
# 2 获取相应的数据
# 3 下载数据
import urllib.parse

from ast import literal_eval



def new_request(page):
     base_url = 'https://movie.douban.com/j/new_search_subjects?sort=S&range=0,10&tags=%E7%94%B5%E5%BD%B1&'
     date = {
          'start':(page-1)*20,
          'limit':20
     }
     date = urllib.parse.urlencode(date)
     url = base_url+date
     print(url)
     headers = {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37'
     }
     request = urllib.request.Request(url=url,headers=headers)
     return request

def get_content(request):
     response = urllib.request.urlopen(request)
     content = response.read().decode('utf-8')
     return content
def down_load(page,content):
     with open('douban_'+str(page)+'.josn','w',encoding='utf-8')as fp:
          fp.write(content)


if __name__ == '__main__':
     start_page = int(input('起始的页码'))
     end_page = int(input('结束的页码'))

     for page in range (start_page,end_page+1):
          request = new_request(page)
          content = get_content(request)
          down_load(page,content)
          literal_eval(content)

