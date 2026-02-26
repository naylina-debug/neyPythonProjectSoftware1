import mysql.connector
from geopy.distance import geodesic

connection = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="flight_game"
)

cursor = connection.cursor()


icao1 = input("Enter first ICAO code: ").upper()
icao2 = input("Enter second ICAO code: ").upper()

sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"

cursor.execute(sql, (icao1,))
result1 = cursor.fetchone()

cursor.execute(sql, (icao2,))
result2 = cursor.fetchone()

if result1 and result2:
    coords1 = (result1[0], result1[1])
    coords2 = (result2[0], result2[1])


    distance = geodesic(coords1, coords2).kilometers

    print(f"\nDistance between {icao1} and {icao2}:")
    print(f"{distance:.2f} kilometers")
else:
    print("One or both ICAO codes were not found.")


cursor.close()
connection.close()