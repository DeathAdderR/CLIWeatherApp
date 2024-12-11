
import sqlite3

class WeatherTable:
    def __init__(self):
        self.connection = sqlite3.connect("weather_table.db")
        self.cursor = self.connection.cursor()
        self._initialize_database()

    def _initialize_database(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS weather_table (
                            entry_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            city_name TEXT,
                            region TEXT,
                            country TEXT,
                            localtime TEXT,
                            current_temperature REAL,
                            condition TEXT,
                            wind_speed REAL,
                            wind_degree REAL,
                            wind_direction TEXT,
                            humidity INTEGER)''')
        self.connection.commit()
    
    def close_db(self):
        self.connection.close()
        print("...connection to weather table terminated...")

    def execute_query(self, query, data=None):
        try:
            if query.strip().lower().startswith('insert'):
                # we need the optional data arg here
                if not data:
                    print(f"Incorrect data passed for INSERT query")
                    return
                self.cursor.execute(query, data)
                self.connection.commit()
                print("Entry successfully added to database")
                return
            # if not inserting we are fetching data
            self.cursor.execute(query)
            entries = self.cursor.fetchall()
            return entries
        except sqlite3.IntegrityError as e:
            print(f"SQL ERROR: {e}")