# urllib 库的简单请求
import urllib.request

response = urllib.request.urlopen("http://www.baidu.com") # 必须带上协议 http 等 https 会自动替换成http

print(response.type())
# print(response.read())