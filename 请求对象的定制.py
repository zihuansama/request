import urllib.request
import urllib.parse

url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=%E5%91%A8%E6%9D%B0%E4%BC%A6'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37'
           }
name = urllib.parse.quote('周杰伦')
url = url+name
request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)

content =response.read().decode('utf-8')
print(content)