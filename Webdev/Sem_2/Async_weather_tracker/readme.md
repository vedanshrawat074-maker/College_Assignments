Async Weather Tracker
Overview
Async Weather Tracker is a simple web application that allows users to search for the current weather of any city. The application fetches real-time weather data from the OpenWeatherMap API and displays important weather information such as temperature, humidity, wind speed, and weather condition.

Features
Search weather by city name

Displays:

City and Country
Temperature (°C)
Weather condition
Humidity
Wind speed
Search history section for previously searched cities

Clicking a city from history loads its weather again

Asynchronous API request using fetch and async/await

Clean UI using HTML, CSS, and JavaScript

Technologies Used
HTML5
CSS3
JavaScript (ES6)
OpenWeatherMap API
How It Works
The user enters a city name in the search box.
When the search button is clicked, the application sends a request to the OpenWeatherMap API.
The API returns the weather data in JSON format.
JavaScript processes the response and dynamically updates the weather information on the page.
The searched city is added to the search history for quick access later.
API Used
OpenWeatherMap API https://openweathermap.org/api

The API is used to retrieve real-time weather data using the following endpoint:

https://api.openweathermap.org/data/2.5/weather

Error Handling
Displays "City Not Found" if an invalid city name is entered.
Displays "Error fetching data" if the API request fails.
Project Structure
project-folder
│
├── index.html
└── README.md
Author
Vedu
