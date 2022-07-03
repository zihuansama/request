import urllib.request

url = 'https://www.baidu.com'
response = urllib.request.urlopen(url)
# print(type(response))
#response 是HTTPResponse类型

content = response.readline() #读取字节
print(content)
# content = response.readline()
# content = response.readlines()读取一行
#
# print(response.getcode())#返回状态码
# print(response.geturl())
# print(response.getheaders())#获取状态信息
# HTTPResponse的六个方法 read readline readlines getcode geturl getheaders
# print(response.getheaders())