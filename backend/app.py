# orbitviewer/backend/app.py

from flask import Flask, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
# Allow CORS for all domains on all routes.
# For production, this should be restricted to the frontend's domain.
CORS(app)

def query_db():
    conn = sqlite3.connect('flights.db')
    conn.row_factory = sqlite3.Row # This allows accessing columns by name
    c = conn.cursor()
    c.execute("SELECT * FROM flight_states ORDER BY time_position DESC LIMIT 100")
    rows = c.fetchall()
    conn.close()
    
    # Convert row objects to dictionaries
    return [dict(row) for row in rows]

@app.route('/api/flights')
def get_flights():
    """
    API endpoint to get the most recent flight data.
    """
    try:
        flights = query_db()
        return jsonify(flights)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Note: This is a development server. For production, use a proper WSGI server like Gunicorn.
    app.run(debug=True, port=5001)
