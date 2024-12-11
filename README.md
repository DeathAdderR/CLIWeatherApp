## CLI WEATHER COLLECTOR APP! ##

This is a project built to practice using yargs and tying it together with python and SQL!

[https://www.weatherapi.com/]
<-- You can go here and sign up to get a free API key!

Once you have that, go into the bin/weatherApp.js file and copy the API key into the variable that says 'API_KEY'

You can fetch data from the API like this while in the CLI:
***node bin/weatherApp.js fetchWeatherData "city name"***
-this will store relevant data into the sql database

You can view the entries in the database like this while in the CLI:
***node bin/weatherApp.js viewWeatherData***



#### The scope of this project is to gain familiarity using API's, making API requests and storing data from the requests.
#### The scope also includes applying concepts used in real world development. I intend on writing test cases that must be passed



# This project was inspired by: [https://github.com/mdwiltfong/FlightTrackerCLI]

yargs are a TON of fun to write!




# FEEL FREE TO CONTRIBUTE!

At the moment the project is bare bones. You can make the API call to the city of your choice. I have cherry picked what properties to fetch and store into the database.
If you would like to add more properties go ahead. ***THERE ARE NO TEST CASES IN PLACE YET***

***If you decide to contribute and want to fetch more properties from the API request you MUST reflect the changes in the TABLE.PY, SCRIPT.PY file AND weatherApp.js file!***
--
--
***You would need to MANUALLY add the NEW properties AT THE END OF THE CURRENT COLUMNS IN THE SQL QUERY, THE SQL TABLE AND THE PROPERTIES BEING PULLED FROM THE REQUEST IN THE API CALL IN weatherApp.js*** =]

<3

