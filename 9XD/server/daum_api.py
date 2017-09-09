import requests


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
        "photo": {**data["photo"],
        "status": "OK"}
    }
    return result
