import requests
import leetcode
import json
import sys

def create_issue(url, token):
    # 自定义body
    data = leetcode.gen_issue(url)
    data = json.dumps(data).encode('utf8')

    # 发起issue 请求

    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    repos = "https://api.github.com/repos/ljnpng/algorithm/issues"
    response = requests.post(url=repos, headers=headers, data=data)
    print(response.status_code)

if __name__ == '__main__':
    if(len(sys.argv) <= 1):
        print("Please input leetcode url, e.g. https://leetcode.cn/problems/merge-two-sorted-lists/")
        exit()
    url = str(sys.argv[1])
    token = ""
    create_issue(url, token)
