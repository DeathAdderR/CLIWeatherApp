## CLI WEATHER COLLECTOR APP! ##

This is a project built to practice using yargs and tying it together with python and SQL!

[https://www.weatherapi.com/]
<-- You can go here and sign up to get a free API key!

Once you have that, go into the bin/weatherApp.js file and copy the API key into the variable that says 'API_KEY'

You can fetch data from the API like this:
node bin/weatherApp.js fetchWeatherData <cityName>
-this will store relevant data into the sql database

You can view the entries in the database like this:
node bin/weatherApp.js viewWeatherData
