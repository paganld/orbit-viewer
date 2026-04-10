# orbitviewer/backend/database.py

import sqlite3
import json
import time

def create_connection(db_file="flights.db"):
    """ Create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Successfully connected to SQLite database: {db_file}")
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    """ Create the flights table """
    try:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS flight_states (
                icao24 TEXT,
                callsign TEXT,
                origin_country TEXT,
                time_position INTEGER,
                last_contact INTEGER,
                longitude REAL,
                latitude REAL,
                baro_altitude REAL,
                on_ground BOOLEAN,
                velocity REAL,
                true_track REAL,
                vertical_rate REAL,
                sensors TEXT,
                geo_altitude REAL,
                squawk TEXT,
                spi BOOLEAN,
                position_source INTEGER,
                fetch_time INTEGER,
                PRIMARY KEY (icao24, fetch_time)
            )
        ''')
        print("Table 'flight_states' created or already exists.")
    except sqlite3.Error as e:
        print(e)

def insert_flight_data(conn, data, fetch_time):
    """ Insert flight data into the flight_states table """
    if not data or 'states' not in data or not data['states']:
        return

    c = conn.cursor()
    
    # The state vectors from OpenSky are in a specific order.
    # See: https://opensky-network.org/apidoc/rest.html#all-state-vectors
    sql = ''' INSERT OR REPLACE INTO flight_states(
                icao24, callsign, origin_country, time_position, last_contact,
                longitude, latitude, baro_altitude, on_ground, velocity,
                true_track, vertical_rate, sensors, geo_altitude, squawk,
                spi, position_source, fetch_time
              ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''
    
    states_to_insert = []
    for state in data['states']:
        # Pad the state vector with None if it's shorter than expected
        state.extend([None] * (17 - len(state)))
        # Add our own fetch_time to the record
        state.append(fetch_time)
        states_to_insert.append(tuple(state))

    try:
        c.executemany(sql, states_to_insert)
        conn.commit()
        print(f"Successfully inserted or replaced {len(states_to_insert)} flight state records.")
    except sqlite3.Error as e:
        print(e)


def cleanup_old_data(conn):
    """ Deletes records older than 24 hours """
    try:
        c = conn.cursor()
        # Get the current time in Unix timestamp format
        current_time = int(time.time())
        # Calculate the timestamp for 24 hours ago
        time_threshold = current_time - (24 * 60 * 60)
        
        c.execute("DELETE FROM flight_states WHERE fetch_time < ?", (time_threshold,))
        conn.commit()
        
        deleted_rows = c.rowcount
        print(f"Successfully cleaned up {deleted_rows} old records.")
    except sqlite3.Error as e:
        print(f"Error during data cleanup: {e}")


if __name__ == '__main__':
    db_path = "backend/flights.db"
    conn = create_connection(db_path)
    
    if conn is not None:
        # Create table
        create_table(conn)
        
        # Clean up old data before inserting new data
        cleanup_old_data(conn)
        
        # Load the sample data and insert it
        try:
            with open("backend/flight_data_sample.json", 'r') as f:
                sample_data = json.load(f)
            
            fetch_timestamp = int(sample_data.get('time', time.time()))
            insert_flight_data(conn, sample_data, fetch_timestamp)
            
        except FileNotFoundError:
            print("flight_data_sample.json not found. Run opensky_fetcher.py first.")
        except json.JSONDecodeError:
            print("Error decoding flight_data_sample.json.")

        # Close the connection
        conn.close()
        print("Database connection closed.")
    else:
        print("Error! cannot create the database connection.")
