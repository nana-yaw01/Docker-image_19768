from flask import Flask, request

app = Flask(__name__)

climates = {
    95126: "24°C",
    94303: "25°C",
    94542: "16°C",
    94552: "20°C",
    94621: "23°C"
}

@app.route("/weather", methods=["GET"])
def get_climate():
    zipcode = request.args.get("zipcode")
    if zipcode:
        zipcode = int(zipcode)
        climate = climates.get(zipcode)
        if climate:
            return "The weather in the zipcode area ({}) is {}".format(zipcode, climate)
        else:
            return "weather information for the zipcode area {} not found".format(zipcode)
    else:
        return "Zipcode not provided"

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port =5000)