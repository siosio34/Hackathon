import json
import requests
from pathlib import Path
from config import CLIENT_SECRET, CLIENT_ID


def get_json_data():
    results = {}
    my_file = Path("./naver_api_result_1.json")
    if my_file.is_file():
        print("Load existing json file")
        results = json.load(open("naver_api_result_1.json"))
    else:
        print("Request to naver open api")
        encText = requests.utils.quote("선릉 스타벅스")
        url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과

        headers = {
            "X-Naver-Client-Id": CLIENT_ID,
            "X-Naver-Client-Secret": CLIENT_SECRET
        }

        res = requests.get(url, headers=headers)
        rescode = res.status_code
        if rescode == 200:
            response_body = res.json()
            json.dump(response_body, open("naver_api_result_1.json", mode="w"))
            results = response_body
        else:
            print("Error Code:" + rescode)
    return results

results = get_json_data()
print(results["items"][0])
