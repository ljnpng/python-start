import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

def get_beat_saber_dlc_prices():
    url = "https://store.steampowered.com/dlc/620980/Beat_Saber/ajaxgetfilteredrecommendations/render/"
    params = {
        "query": "",
        "cc": "ar",
        "start": "0",
        "count": "200",
        "tagids": "",
        "sort": "newreleases",
        "app_types": "",
        "curations":"",
        "reset":"true"
    }
    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("请求失败，状态码：", response.status_code)
        return

    json_data = json.loads(response.text)
    results_html = json_data["results_html"]
    soup = BeautifulSoup(results_html, 'html.parser')
    dlcs = soup.find_all("div", class_="recommendation")

    dlc_data = []
    for dlc in dlcs:
        dlc_name = dlc.find("span", class_="color_created").text.strip()
        discount_info = dlc.find("div", class_="discount_final_price").text.strip()

        dlc_data.append({"DLC名称": dlc_name, "当前价格": discount_info})

    return dlc_data

def display_dlc_data(dlc_data):
    # 设置显示选项，以显示所有行和列
    pd.set_option("display.max_rows", None)  # 显示所有行
    pd.set_option("display.max_columns", None)  # 显示所有列
    pd.set_option("display.width", None)  # 根据内容自动调整列宽
    pd.set_option("display.max_colwidth", -1)  # 显示完整的列内容

    df = pd.DataFrame(dlc_data)
    print(df)

if __name__ == "__main__":
    dlc_data = get_beat_saber_dlc_prices()
    display_dlc_data(dlc_data)

