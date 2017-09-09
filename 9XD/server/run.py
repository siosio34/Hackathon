from flask import Flask, request, jsonify
from naver_api import get_keyword_results
from daum_api import get_place_id_results
from rank_api import get_ranking_results

app = Flask(__name__)

@app.route("/")
def index():
    return "It's work!"

@app.route("/post", methods=["POST"])
def post():
    data = request.json

    if data is None:
        return jsonify(status="OK", message="data is null"), 200

    message = data
    return jsonify(status="OK", message=message), 200

@app.route("/get/daum/<int:place_id>/", methods=["GET"])
@app.route("/get/daum/<int:place_id>/<string:key>", methods=["GET"])
def get_daum(place_id, key=None):
    results = get_place_id_results(place_id)
    if key is not None:
        results = results.get(key, results)

    return jsonify(results)

@app.route("/get/naver/<string:keyword>", methods=["GET"])
def get_naver(keyword):
    results = get_keyword_results(keyword)
    return jsonify(status="OK", items=results)

@app.route("/get/rank/", methods=["GET"])
@app.route("/get/rank/<string:place>", methods=["GET"])
def get_rank(place=""):
    results = get_ranking_results(place)
    return jsonify(results)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9090, debug=True)
