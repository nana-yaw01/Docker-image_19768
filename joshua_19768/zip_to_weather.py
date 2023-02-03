from flask import Flask, request

app = Flask(__name__)

climates = {
    94535: "Floods, 25°C",
    94395: "Earthquake, 25°C",
    94543: "Thunderstorm, 26°C",
    95126: "Heavy Rains, 22°C",
    94167: "T-sunami, 20°C"
}

@app.route("/climate", methods=["GET"])
def get_climate():
    zipcode = request.args.get("zipcode")
    if zipcode:
        zipcode = int(zipcode)
        climate = climates.get(zipcode)
        if climate:
            return "The climate in the zipcode {} is {}".format(zipcode, climate)
        else:
            return "Climate information for the zipcode {} not found".format(zipcode)
    else:
        return "Zipcode not provided"

if __name__ == '__main__':
    app.run()