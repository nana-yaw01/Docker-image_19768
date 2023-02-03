# Docker-image_19768
This web application finds the weather of a given city. 
This repository contains code for a web application that allows users to find the weather forecast for a given city. 

A zip code-to-weather microservice
Key Instructions/Commands
Clone the repository:

git clone https://github.com/<YOUR_USERNAME>/weather-app.git

Build the Docker images:

docker build -t image1 :v1 -f image1/Dockerfile city_to_zip/
docker build -t image2 :v1 -f image2/Dockerfile zip_to_weather/

Create and start the containers:

docker run --name image1-container1 -p image1:v1
docker run --name image2-container2 -p image2:v1

Test the application:

http://192.168.1.93:5000/weather?zipcode=94621
