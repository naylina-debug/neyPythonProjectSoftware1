import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="flight_game"
)

cursor = connection.cursor()


icao = input("Enter ICAO code: ").upper()

sql = "SELECT name, municipality FROM airport WHERE ident = %s"

cursor.execute(sql, (icao,))
result = cursor.fetchone()


if result:
    print(f"Airport Name: {result[0]}")
    print(f"Location: {result[1]}")
else:
    print("No Airport found with this ICAO code.")


cursor.close()
connection.close()