import sqlite3  # https://docs.python.org/3/library/sqlite3.html

"""
HOTEL database contains Room table as follows:

Room Table
roomNo floor type location rate
101 ground single non_sea_view 35
105 ground suite sea view 50
204 first single non_sea_view 30
206 first single non_sea_view 35
302 second double sea_view 45
403 third deluxe non_sea_view 60
507 fourth suite sea_view 75

"""

conn = sqlite3.connect("HOTEL.db")  # establishing the connection via connection object

c = conn.cursor()  # creating the cursor through which all transactions shall pass through

c.execute("SELECT * FROM Room;")

print(c.fetchall())  # prints full details of all records in Room table, as opposed to .fetchone() which would only return one
# and .fetchmany(size) which returns number of records of specifified paramater numbers
c.execute("""SELECT type, rate

             FROM Room;""")

print(c.fetchall())  # prints type and rate attributes's values per every record

# c.execute("""SELECT * FROM Room WHERE rate > 45;""")  # bad practice to hardcode in
# c.execute("SELECT * FROM Room WHERE symbol = '%s'" % symbol)  # insecure
# c.execute("SELECT * FROM Room WHERE rate > '{}';".format(45))  # bad practice cuz vulnerable to SQL injection attacks XO

# c.execute("SELECT * FROM Room WHERE rate > ?;", (45, ))  # good practice but less readable
c.execute("""SELECT *
            FROM Room
            WHERE rate > :rate_lb;""",
          {'rate_lb': 45})

print(c.fetchall())  #  What SQL commands would be needed to list full details of all rooms with a rate higher than £45?

c.execute("""SELECT *
            FROM Room
            WHERE type=:room_type1 OR type=:room_type2;""",
          {'room_type1': 'single', 'room_type2': 'deluxe'})

print(c.fetchall())  # What SQL commands would be needed to list full details of all rooms with single or deluxe type?

c.execute("""SELECT *
            FROM Room
            ORDER BY floor DESC, type ASC;""")

print(c.fetchall())  # What SQL commands would be needed to list full details of all rooms in descending order of ‘floor’ and ascending order of ‘type’?
# huh but it is text so... hmmm confusions

c.execute("""SELECT COUNT(roomNo) as totalOfRooms, SUM(rate) as totalOfRates
            FROM Room
            WHERE rate < 45""")

print(c.fetchall()) # What SQL commands would be needed to list total number of room with rate lower than £45 and the sum of their rates?

c.execute("""SELECT MIN(rate) as minRate, MAX(rate) as maxRate, AVG(rate) as avgRate
            FROM Room;""")
print(c.fetchall())  # What SQL commands would be needed to list the minimum, maximum, and average room rate?

c.execute("""SELECT floor, COUNT(roomNo) AS totalRoom, SUM(rate) as totalRate
            FROM Room
            GROUP BY floor;
            """)

print(c.fetchall())  # What SQL commands would be needed to find the number of rooms for each floor and the sum of their rate having grouped the floors?

c.execute("""SELECT floor, COUNT(roomNo) as totalRooms, SUM(rate) as ratesSum
            FROM Room
            GROUP BY floor
            HAVING COUNT(roomNo) > 1""")

print(c.fetchall())  # For each floor with more than 1 room find the number of rooms in each floor and sum their rates.


conn.commit()  # committing the changes otherwise they won't happen
print("Successful commit.")
conn.close()  # closes database connection -  after commiting else chchchanges will be lost
print("Successful database connection closure.")
