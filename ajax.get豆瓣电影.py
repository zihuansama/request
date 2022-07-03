import urllib.request

url = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start=0&genres=%E5%8A%A8%E4%BD%9C'
headers = {
    'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37'
}
request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
#下载数据到本地

# fp = open('douban.josn','w',encoding='utf-8')
# fp.write(content)
with open('douban1.josn','w',encoding='utf-8')as fp:
    fp.write(content)
fp = open('douban.josn','w',encoding='utf-8')
fp.write(content)
