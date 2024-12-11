
import sys
import json
from table import WeatherTable

db = WeatherTable()



def validate_weather_data(data):
    # ensure all columns have been assigned values

    required_keys = ["city_name", "region", "country", "localtime", "current_temperature", "condition", "wind_speed", "wind_degree", "wind_direction", "humidity"]

    # make sure the data contains all the required keys
    for key in required_keys:
        if key not in data:
            print(f"Missing required column-data: {key}")
            return False
        return True
        


def save_weather_data(data):
    # add data to database table

    is_valid_data = validate_weather_data(data)
    if not is_valid_data:
        # Error is printed from validate_weather_data
        db.close_db()
        return
    db.execute_query('''INSERT INTO weather_table (city_name, region, country, localtime, current_temperature, condition, wind_speed, wind_degree, wind_direction, humidity) VALUES (?,?,?,?,?,?,?,?,?,?)''', (data["city_name"], data["region"], data["country"], data["localtime"], data["current_temperature"], data["condition"], data["wind_speed"], data["wind_degree"], data["wind_direction"], data["humidity"]))
    # successfull entry submission log printed from table class


def view_all_weather_data():
    # view all weather data collected in database
    print('attempting to view entries')
    entries = db.execute_query('''SELECT * FROM weather_table''')
    if entries:
       print(json.dumps(entries)) # return entries as JSON
    else:
        print("No data found in the database") # return empty list if no data


if len(sys.argv) > 1:
    if sys.argv[1] == "view_all":
        view_all_weather_data()
    else:
        weather_data = json.loads(sys.argv[1])
        save_weather_data(weather_data)
        db.connection.close()
else:
    print("No data received from JavaScript")
    db.connection.close()


db.connection.close()
