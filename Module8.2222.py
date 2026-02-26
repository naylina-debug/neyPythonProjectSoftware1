import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="flight_game",
)

cursor = connection.cursor()

country_code = input("Enter country area code (e.g. FI): ").upper()


sql = """
SELECT type, COUNT(*)
FROM airport
WHERE iso_country = %s
GROUP BY type
ORDER BY type \
"""

cursor.execute(sql, (country_code,))
results = cursor.fetchall()

if results:
    print(f"\nAirports in {country_code}:")
    for row in results:
        print(f"{row[1]} {row[0]} airports")
else:
    print("No airports found for that country code.")

cursor.close()
connection.close()