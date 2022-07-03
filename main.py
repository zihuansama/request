import urllib.request
url = 'http://www.baidu.com/'
#定义URL
response = urllib.request.urlopen(url)
#response响应

content = response.read().decode('utf-8')
print(content)