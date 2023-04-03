import requests
from bs4 import BeautifulSoup
import json

url = "https://store.steampowered.com/dlc/620980/Beat_Saber/ajaxgetfilteredrecommendations/render/?query=&start=0&count=200&tagids=&sort=newreleases&app_types=&curations=&reset=true"
response = requests.get(url)

if response.status_code != 200:
    print("请求失败，状态码：", response.status_code)
else:
    json_data = json.loads(response.text)
    results_html = json_data["results_html"]
    soup = BeautifulSoup(results_html, 'html.parser')
    prettified_html = soup.prettify()
        # 将HTML内容保存到文件中
    with open('output.html', 'w', encoding='utf-8') as output_file:
        output_file.write(prettified_html)

    print("HTML内容已保存到 output.html 文件中")

