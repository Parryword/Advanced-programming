import mysql.connector

database = mysql.connector.connect (
    host = "localhost",
    user = "root",
    passwd = "0000"
)

cursorObject = database.cursor()

cursorObject.execute("""CREATE DATABASE myDataBase""")

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    database="myDataBase",
    passwd="0000"
)
if connection.is_connected():
    db_Info = connection.get_server_info()
    print("Connected to MySQL Server Version", db_Info)
    cursor = connection.cursor()
    cursor.execute("""SELECT DATABASE();""")
    record = cursor.fetchone()
    print("You are connected to database: ", record)

cursor.execute("""CREATE TABLE Marvel (
    ID INT AUTO_INCREMENT,
    Movie VARCHAR(40),
    Date VARCHAR(20),
    PCUPhase VARCHAR(20),
    PRIMARY KEY (ID)
);""")

cursor.execute("""INSERT INTO Marvel (ID, Movie, Date, PCUPhase) VALUES
    (1, "IronMan", "May2,2008", "Phase1"),
    (2, "TheIncredibleHulk", "June13,2008", "Phase1"),
    (3, "IronMan2","May7,2010","Phase1"),
    (4, "Thor","May6,2011","Phase1"),
    (5, "CaptainAmerica:TheFirstAvenger","July22,2011","Phase1"),
    (6, "Marvel'sTheAvengers","May4,2012", "Phase1"),
    (7, "IronMan3","May3,2013","Phase2"),
    (8, "Thor:TheDarkWorld","November8,2013","Phase2"),
    (9, "CaptainAmerica:TheWinterSoldier","April4,2014","Phase2"),
    (10, "GuardiansoftheGalaxy","August1,2014","Phase2"),
    (11, "Avengers:AgeofUltron","May1,2015","Phase2"),
    (12, "Ant-Man","July17,2015","Phase2"),
    (13, "CaptainAmerica:CivilWar","May6,2016","Phase3"),
    (14, "DoctorStrange","November4,2016","Phase3"),
    (15, "GuardiansoftheGalaxyVol.2","May5,2017","Phase3"),
    (16, "Spider-Man:Homecoming","July7,2017","Phase3"),
    (17, "Thor:Ragnarok",	"November3,2019","Phase3"),
    (18, "BlackPanther",	"February16,2018", "Phase3"),
    (19, "Avengers:Infinity War", "April27,2018", "Phase3"),
    (20, "Ant-ManandtheWasp", "July6,2018",	"Phase3"),
    (21, "CaptainMarvel", "March8,2019",	"Phase3"),
    (22, "Avengers:Endgame","April26,2019",	"Phase3"),
    (23, "Spider-Man:FarFromHome",	"July2,2019", "Phase3")
""")

connection.commit()

cursor.execute("""SELECT * FROM Marvel""")
records = cursor.fetchall()
for row in records:
    print("ID:", row[0])
    print("Title:", row[1])
    print("Date:", row[2])
    print("PCUPhase:", row[3])

cursor.execute("""DELETE FROM Marvel WHERE Movie = "TheIncredibleHulk" """)
connection.commit()
print("----------------------")

cursor.execute("""SELECT * FROM Marvel""")
records = cursor.fetchall()
for row in records:
    print("ID:", row[0])
    print("Title:", row[1])
    print("Date:", row[2])
    print("PCUPhase:", row[3])
print("----------------------")

cursor.execute("""SELECT * FROM Marvel WHERE PCUPhase = "Phase2" """)
records = cursor.fetchall()
for row in records:
    print("ID:", row[0])
    print("Title:", row[1])
    print("Date:", row[2])
    print("PCUPhase:", row[3])
print("----------------------")

cursor.execute("""UPDATE Marvel SET Date = "November3,2017" WHERE Movie = "Thor:Ragnarok" """)
connection.commit()

cursor.execute("""SELECT * FROM Marvel""")
records = cursor.fetchall()
for row in records:
    print("ID:", row[0])
    print("Title:", row[1])
    print("Date:", row[2])
    print("PCUPhase:", row[3])
print("----------------------")
