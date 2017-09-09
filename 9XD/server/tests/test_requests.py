import requests


place_id = 653245473
url = "http://place.map.daum.net/{}".format(place_id)
res = requests.get(url)
print(res.status_code)
print(res.headers)
