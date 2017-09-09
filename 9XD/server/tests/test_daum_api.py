# import requests
# url = "http://place.map.daum.net/main/v/653245473"
# res = requests.get(url)
# if res.status_code != 200:
#     print("error")
# data = res.json()

import json
data = json.load(open("daum_api_result_1.json", mode="r"))
json.dump(
    {
        "basicInfo": {**data["basicInfo"]},
        "photo": {**data["photo"]}
    },
    open("daum_api_result_2.json", mode="w")
)
print(data["basicInfo"].keys())
print(data["photo"].keys())
