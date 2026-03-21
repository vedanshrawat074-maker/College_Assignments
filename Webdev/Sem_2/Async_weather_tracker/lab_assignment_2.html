<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lab Assignment 2</title>
    <style>
         * {
            margin: 0;
            padding: 0;
        }

        body {
            background-color: rgb(65, 65, 176);
            font-family: Arial, sans-serif;
            color: white;
            min-height: 100vh;
            padding: 30px 20px;
        }

        h1 {
            text-align: center;
            font-size: 1.6rem;
            margin: 24px;
            color: white;
        }

        #search-main-container {
            display: flex;
            gap: 16px;
            margin-bottom: 16px;
            align-items: stretch;
        }
        #search-city-box {
            display: flex;
            flex-direction: column;
            gap: 16px;
            flex: 1;
            background-color: #fff;
            border-radius: 8px;
            padding: 16px;
        }

        #weather-info-container {
            flex: 1;
            background-color: #fff;
            color: #222;
            border-radius: 8px;
            padding: 16px;
            font-size: 0.88rem;;
        }

        #search-city-box,
        #search-history-box {
            color: #222;
        }

        #search-city-box h3,
        #search-history-box h3,
        #weather-info-container h3 {
            font-size: 0.85rem;
            margin-bottom: 10px;
            color: #333;
        }

        #search-city-box form {
            display: flex;
            gap: 8px;
        }

        #search-city-box input[type="text"] {
            flex: 1;
            padding: 6px 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 0.9rem;
            outline: none;
        }

        #search-city-box button {
            padding: 6px 16px;
            background-color: #e85d04;
            color: #fff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 0.85rem;
            font-weight: bold;
        }

        #search-city-box button:hover {
            background-color: #d44f00;
        }

        #search-cities-box {
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            margin-top: 4px;
        }

        #search-cities-box span {
            background-color: #e85d04;
            color: #fff;
            width: fit-content;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.78rem;
            cursor: pointer;
        }


        #City-Weather-box > div>div{
            display: flex;
            justify-content:space-between;
            background-color: #f3e0e0;
            padding: 6px;
            margin: 5px;
            border-left: 2px solid orangered;
        }
    </style>
</head>
<body>
    <h1> ⛅Async Weather Tracker</h1>

    <div id="search-main-container">
        <div id="search-city-box">
            <h3>Search City</h3>
            <form>
                <input type="text" name="city" id="city">
                <button type="submit">Search</button>
            </form>
            <div id="search-history-box">
                <h3>Search History</h3>
                <div id="search-cities-box"></div>
            </div>
        </div>    
        <div id="weather-info-container">
            <h3>Weather Info</h3>
            <div id="City-Weather-box"></div>

        </div>
    </div>
    <script>
        let API_KEY = "7b10ff2ce86832a4ac5dcf5334e89f06"

        async function getWeather(city){
            try{
            let response = await fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${API_KEY}&units=metric`)

            let data = await response.json()
            if(data.cod === 404){
                weather.innerHTML = `<span style="color:red;">City Not Found</span>`
                }
            let card = document.createElement('div')
            card.innerHTML = `<div>City :<span>${data.name},${data.sys.country}</div>
                              <div>Temp:<span> ${data.main.temp} °C</div>
                              <div>Weather :<span> ${data.weather[0].main}</div> 
                              <div>Humidity:<span>${data.main.humidity}</div> 
                              <div>Wind:<span>${data.wind.speed}</div>` 
            weather.innerHTML=""
            weather.append(card)  
            if (!searchHistory.includes(city)) {
                    searchHistory.push(city);
                    const tag = document.createElement("span");
                    tag.textContent = city;
                    tag.addEventListener("click", () => {
                        document.querySelector("#city").value = city;
                        getWeather(city);
                    });
                    searchedCitiesBox.appendChild(tag);
                }
            }catch(error){
                weather.innerHTML = `<span style="color:red;">Error fetching data</span>`
            }
        }
            


        let form = document.querySelector("form")
        let city = document.querySelector("#city")
        let weather= document.querySelector("#City-Weather-box")
        let searchHistory = []
        let searchedCitiesBox = document.querySelector("#search-cities-box")

        form.addEventListener("submit",(event)=>{
            event.preventDefault()
            getWeather(city.value)
        })  

    </script>
</body>
</html>
