import requests
import json

def get_place_id_results(place_id):
    url = "http://place.map.daum.net/main/v/{}".format(place_id)
    res = requests.get(url)
    if res.status_code != 200:
        return {"status": "Error"}
    data = res.json()
    if not "basicInfo" in data.keys():
        return {"status": "basic info is not contained"}
    if not "photo" in data.keys():
        return {"status": "photo is not contained"}
    result = {
        "basicInfo": {**data["basicInfo"]},
        "photo": {**data["photo"]},
        "blogReview": {**data["blogReview"]},
        "status": "OK",
    }
    result = replace_list_word(result)
    return result

def replace_list_word(result_dict):
    dump_dict = json.dumps(result_dict)
    replace_dict = dump_dict.replace("list", "resultList")
    return json.loads(replace_dict)
