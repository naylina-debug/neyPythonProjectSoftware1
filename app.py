import sqlite3

def create_database():
    conn = sqlite3.connect('airports.db')
    cursor = conn.cursor()

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS airports (
                                                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                           icao TEXT UNIQUE NOT NULL,
                                                           name TEXT NOT NULL,
                                                           location TEXT NOT NULL
                   )
                   ''')

    airports_data = [
        ('EFHK', 'Helsinki-Vantaa Airport', 'Helsinki'),
        ('EFTU', 'Turku Airport', 'Turku'),
        ('EFOU', 'Oulu Airport', 'Oulu'),
        ('EFTP', 'Tampere-Pirkkala Airport', 'Tampere'),
        ('EFRO', 'Rovaniemi Airport', 'Rovaniemi'),
        ('EFIV', 'Ivalo Airport', 'Ivalo'),
        ('EFKU', 'Kuopio Airport', 'Kuopio'),
        ('EFJY', 'Jyvaskyla Airport', 'Jyvaskyla'),
        ('EFKT', 'Kittila Airport', 'Kittila'),
        ('EFJO', 'Joensuu Airport', 'Joensuu')
    ]

    cursor.executemany('''
                       INSERT OR IGNORE INTO airports (icao, name, location)
        VALUES (?, ?, ?)
                       ''', airports_data)

    conn.commit()
    conn.close()
    print("Database created successfully!")

if __name__ == '__main__':
    create_database()

from flask import Flask, jsonify, request
import sqlite3
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_db_connection():
    """Create a database connection"""
    conn = sqlite3.connect('airports.db')
    conn.row_factory = sqlite3.Row  # This enables column access by name
    return conn

@app.route('/airport/<icao_code>', methods=['GET'])
def get_airport(icao_code):
    """
    Get airport information by ICAO code

    Args:
        icao_code (str): ICAO code of the airport (e.g., EFHK)

    Returns:
        JSON: Airport information or error message
    """
    icao_code = icao_code.upper()

    if not icao_code or len(icao_code) != 4 or not icao_code.isalpha():
        return jsonify({
            "error": "Invalid ICAO code format. ICAO code must be 4 letters."
        }), 400

    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT icao, name, location FROM airports WHERE icao = ?",
            (icao_code,)
        )
        airport = cursor.fetchone()

        if airport:
            response = {
                "ICAO": airport["icao"],
                "Name": airport["name"],
                "Location": airport["location"]
            }
            logger.info(f"Airport found: {icao_code}")
            return jsonify(response), 200
        else:
            logger.warning(f"Airport not found: {icao_code}")
            return jsonify({
                "error": f"Airport with ICAO code {icao_code} not found"
            }), 404

    except sqlite3.Error as e:
        logger.error(f"Database error: {str(e)}")
        return jsonify({
            "error": "Internal server error"
        }), 500
    finally:
        conn.close()

@app.route('/airports', methods=['GET'])
def get_all_airports():
    """Get all airports (optional endpoint for testing)"""
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT icao, name, location FROM airports ORDER BY icao")
        airports = cursor.fetchall()

        result = []
        for airport in airports:
            result.append({
                "ICAO": airport["icao"],
                "Name": airport["name"],
                "Location": airport["location"]
            })

        return jsonify(result), 200
    except sqlite3.Error as e:
        logger.error(f"Database error: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500
    finally:
        conn.close()

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='127.0.0.1', port=5000, debug=True)