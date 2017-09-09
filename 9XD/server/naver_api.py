import requests
from tests.config import CLIENT_SECRET, CLIENT_ID


def get_keyword_results(keyword):
    results = {}
    encText = requests.utils.quote(keyword)
    url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과

    headers = {
        "X-Naver-Client-Id": CLIENT_ID,
        "X-Naver-Client-Secret": CLIENT_SECRET
    }

    res = requests.get(url, headers=headers)
    rescode = res.status_code
    if rescode == 200:
        response_body = res.json()
        results = response_body
    return results["items"]
