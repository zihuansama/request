# import urllib.parse
# #
# # date = {
# #     'wd':'周杰伦',
# #     'sex':'男',
# # }
# # a = urllib.parse.urlencode(date)
# # print(a)
import urllib.request
import  urllib.parse
date ={
    'wd':'周杰伦',
    'sex':'男',
    'location':'中国台湾省'
}
base_url = 'https://www.baidu.com/s?'
new_date = urllib.parse.urlencode(date)
url = base_url + new_date

headers = {
    'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37'
}
request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
contant = response.read().decode('utf-8')
print(contant)