from flask import Flask, request, jsonify
from naver_api import get_keyword_results

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

@app.route("/get/")
@app.route("/get/<int:item_id>", methods=["GET"])
def get(item_id=None):
    if item_id is None:  # case: /get, /get/
        return jsonify(message="default get json")
    # case: /get/<item_id>
    return jsonify(id=item_id, message="42")


@app.route("/get/naver/<string:keyword>", methods=["GET"])
def get_naver(keyword):
    results = get_keyword_results(keyword)
    return jsonify(status="OK", items=results)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9090, debug=True)
