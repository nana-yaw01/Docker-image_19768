# Docker-image_19768
This web application finds the weather of a given city. 
This repository contains code for a web application that allows users to find the weather forecast for a given city. 

A zip code-to-weather microservice
Key Instructions/Commands
Clone the repository:

git clone https://github.com/<YOUR_USERNAME>/weather-app.git

Build the Docker images:

docker build -t city-to-zip:v1 -f city_to_zip/Dockerfile city_to_zip/
docker build -t zip-to-weather:v1 -f zip_to_weather/Dockerfile zip_to_weather/

Create and start the containers:

docker run -d -p 5000:5000 --name city-to-zip city-to-zip:v1
docker run -d -p 5001:5000 --name zip-to-weather zip-to-weather:v1

Test the application:

curl http://localhost:5000/zip_code?city=San Francisco
curl http://localhost:5001/weather?zip=94103
