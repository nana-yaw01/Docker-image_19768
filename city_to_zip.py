from flask import Flask, jsonify

app = Flask(__name__)

def get_zip_code(city):
    zip_codes = {
        "san jose": 95126,
        "palo alto": 94303,
        "hayward": 94542,
        "castro valley": 94552,
        "oakland": 94621
    }
    return zip_codes.get(city.lower(), None)

@app.route("/zipcode/<city>", methods=["GET"])
def zip_code(city):
    zip_code = get_zip_code(city)
    if zip_code:
        return jsonify({"zip_code": zip_code})
    else:
        return jsonify({"error": "City not found"}), 404

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port =5001)
