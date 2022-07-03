import urllib.request
import urllib.parse
url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
headers = {
    ' 'Accept':' */*'
    ' Accept-Encoding: gzip, deflate, br
    ' Accept-Language: zh-CN,zh;q=0.9
    ' Acs-Token: 1656658807991_1656740371663_yFydIvmiaY1/Yp89fcVNWOWkox5NFMkN9UwHerOD7oRLu9UMs6vr8e60XifUdN6ZUPgEry8D2fxtfiiBUqsjUezqrE6lGCjpaQcyk/lbl/KbTcMDN0+HNxOEuOsmcXVchfyI4352/ce7tH2igxSypzeQvwW33H3U01h9MX/yYy27KhoVUJdW5HjeemkMLjSk7O9699lIpXV2SixyIY+i8+eAAEZjVvvdaaCtupe0/CVk/InBoQPO/2P9P/OE2HYldg9GKacyRfM2bVgNO+b+Tlxqu+hryHnEEIkBbNsVoFkDyjAEWyqpXnZkkKNEG4bW
    ' Connection: keep-alive
    ' Content-Length: 136
    ' Content-Type: application/x-www-form-urlencoded; charset=UTF-8
    ' Cookie: BIDUPSID=1125D323D6325DD13B553133DC5911CC; PSTM=1656502893; BAIDUID=1125D323D6325DD1740324CBC0FF6DE9:FG=1; BAIDUID_BFESS=1125D323D6325DD1740324CBC0FF6DE9:FG=1; ZFY=o6vfSHC8xYHt3daQYEqgToTZM74dH:BIiX1i5PFghDcY:C; H_PS_PSSID=36560_36463_36726_36455_31254_36691_36165_36695_36698_36569_36074_36772_36744_36762_36768_36764_26350_36686_36469_36714; BA_HECTOR=0l85ah2g00a4a1812g1hbvm1515; delPer=0; PSINO=3; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1656739883; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1656740184; ab_sr=1.0.1_YmZmYjRmZDUyZjNkOGFiZDA5MmFmMzA5YmU0MWM3ZWNjNWVmYzU0NDc3MTY0MzNhMGVmMzIxMDAyZWY3YzQxMDdjZTI5MGZlNTlhNTVhMGFkMmQ2MDlkY2NjZWM1NGZiOWYwMDI3ZWU2NmVhMmJmMjVmNzI1YTdmOTNjZjkwZjFkNTg3NTFkN2UwMDViZDQyMmUxM2I5ODU0N2Y4ZDVhZQ==
    ' Host: fanyi.baidu.com
    ' Origin: https://fanyi.baidu.com
' Referer: https://fanyi.baidu.com/
 sec-ch-ua: ".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"
    ' ' sec-ch-ua-mobile: ?0
    ' sec-ch-ua-platform: "Windows"
    ' Sec-Fetch-Dest: empty
    ' Sec-Fetch-Mode: cors
    ' Sec-Fetch-Site: same-origin
    ' User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36
    ' X-Requested-With: XMLHttpRequest
}
date = {
'from': 'en',
'to': 'zh',
'query'': 'love'',
'transtype': 'translang',
'simple_means_flag': '3',
'sign': '198772.518981',
'token': '54772215272de520e489e12a3198a30b',
'domain': 'common'',
}
