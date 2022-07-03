import requests
import re
# headers = {
#     'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37'
# }
# page_index = 1
#
# url = r"https://movie.douban.com/j/new_search_subjects?sort=S&range=0,10&tags=&start=" + str((page_index - 1) * 20)
#
# response = requests.get(url, headers=headers).text  # 发送请求，获取响应
# response = re.sub(r"\\", "", response)  # 对⽹址进⾏处理
# pat_title = r'"title":"(.*?)",'  # 匹配影视名
# pat_rate = r'"rate":"(.*?)",'  # 匹配影视评分
# pat_url = r'"url":"(.*?)",'  # 匹配具体⾖瓣影评的URL
# data_title_list = re.compile(pat_title).findall(response)  # 获取影视名列表
# data_rate_list = re.compile(pat_rate).findall(response)  # 获取影视评分列表
# data_url_list = re.compile(pat_url).findall(response)  # 获取具体⾖瓣影评的URL
# for i in range(0, len(data_title_list)):  # 循环遍历打印
#     print(data_title_list[i], "\t\t\t\t\t\t\t\t", data_rate_list[i], "\t\t\t\t\t\t\t\t", data_url_list[i])
#
# 爬取⾖瓣⾼评分影视
# 第1页：https://movie.douban.com/j/new_search_subjects?sort=S&range=0,10&tags=&start=0
# 第2页：https://movie.douban.com/j/new_search_subjects?sort=S&range=0,10&tags=&start=20
# 第3页：https://movie.douban.com/j/new_search_subjects?sort=S&range=0,10&tags=&start=40
# 第4页：https://movie.douban.com/j/new_search_subjects?sort=S&range=0,10&tags=&start=60
# 故可以得到URL公式：url="https://movie.douban.com/j/new_search_subjects?sort=S&range=0,10&tags=&start="+(page_index-1)*20
# 请求头
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36"
}
page_num = int(input("请输⼊您想知道的记录条数（记录条数是20的倍数）："))  # 获取记录总条数
page_index = int(page_num / 20)  # 获取页数
for i in range(1, page_index + 1):  # 循环遍历页数
    url = r"https://movie.douban.com/j/new_search_subjects?sort=S&range=0,10&tags=&start=" + str(
        (i - 1) * 20)  # 拼接URL
    response = requests.get(url, headers=header).text  # 发送请求，获取响应
    response = re.sub(r"\\", "", response)  # 对⽹址进⾏处理
    pat_title = r'"title":"(.*?)",'  # 匹配影视名
    pat_rate = r'"rate":"(.*?)",'  # 匹配影视评分
    pat_url = r'"url":"(.*?)",'  # 匹配具体⾖瓣影评的URL
    data_title_list = re.compile(pat_title).findall(response)  # 获取影视名列表
    data_rate_list = re.compile(pat_rate).findall(response)  # 获取影视评分列表
    data_url_list = re.compile(pat_url).findall(response)  # 获取具体⾖瓣影评的URL
    for i in range(0, len(data_title_list)):  # 循环遍历打印
        print(data_title_list[i], "\t\t\t\t\t\t\t\t", data_rate_list[i], "\t\t\t\t\t\t\t\t", data_url_list[i])
