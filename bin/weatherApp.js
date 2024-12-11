
const yargs = require("yargs");
const chalk = require("chalk");

const { spawn } = require('child_process')

const { default: axios } = require("axios");

const API_BASE_URL = "http://api.weatherapi.com/v1/current.json"; // make a free account to get API key and place in variable below. Bam, that's it!
const API_KEY = "YOUR_KEY_GOES_HERE";

var options = yargs(process.argv.slice(2))
.usage("Usage weatherapp <command> [options]")
.command(
    "fetchWeatherData [name]",
    "Fetch weather data by city",
    (yargs) => {
        yargs
          .positional("name", {
            describe: "City Name",
            type: "string",
          })
    },
    async (argv) => {
        if(!argv["name"]) {
            console.log(chalk.red("No city name provided"))
            return;
        }
        try {

            const response = await axios.get(API_BASE_URL, {
                params: {
                    key: API_KEY,
                    q: argv["name"],
                    aqi: "no"
                },
            })
            const data = response.data
            const weatherData = {
                city_name: data.location.name,
                region: data.location.region,
                country: data.location.country,
                localtime: data.location.localtime,
                current_temperature: data.current.temp_f,
                condition: data.current.condition.text,
                wind_speed: data.current.wind_kph,
                wind_degree: data.current.wind_degree,
                wind_direction: data.current.wind_dir,
                humidity: data.current.humidity,
            }
            console.log(response.data)
            callPython(weatherData)
        } catch (error) {
            console.error(chalk.red("Error fetching data:"), error);
        }
    }
)
.command(
    "viewWeatherData",
    "View all weather entries in the database",
    async (argv) => {
        try {
            const pythonProcess = spawn('python', ['backend/script.py', 'view_all']);
    
            pythonProcess.stdout.on('data', (data) => {
                console.log(`Python Output: ${data.toString()}`);
            });
    
            pythonProcess.stderr.on('data', (error) => {
                console.error(`Error: ${error}`);
            });
    
            pythonProcess.on('close', (code) => {
                console.log(`Python process closed with code ${code}`);
            })
            
        } catch (error) {
            console.error(chalk.red("Error Viewing data:"), error);
        }
    }
)
.demandCommand(1, chalk.red("You need at least one command before moving on"))
.strict()
.parse()

console.log(options)


// helper functions

const callPython = (weatherData) => {
    const pythonProcess = spawn('python', ['backend/script.py', JSON.stringify(weatherData)]);

    pythonProcess.stdout.on('data', (data) => {
        console.log(`Python Output: ${data}`);
    });

    pythonProcess.stderr.on('data', (error) => {
        console.error(`Error: ${error}`);
    });

    pythonProcess.on('close', (code) => {
        console.log(`Python process closed with code ${code}`);
    });
};

// callPython(weatherData)
