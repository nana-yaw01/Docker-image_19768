from flask import Flask, request

app = Flask(__name__)

climates = {
    95126: "Sunny, 24°C",
    94303: "Cloudy, 25°C",
    94542: "Thunderstorm, 16°C",
    94552: "Heavy Rains, 20°C",
    94621: "Flood-Watch, 23°C"
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