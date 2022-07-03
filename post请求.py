import urllib.request
import urllib.parse


url = 'https://fanyi.baidu.com/sug'

headers = {
    'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37'
}
date = {
    'kw':'spider',
}

date = urllib.parse.urlencode(date).encode('utf-8')
request = urllib.request.Request(url=url,date=date,headers=headers)
response = urllib.request.urlopen(request)
contant = urllib.response.read().encode('utf-8')
print(contant)