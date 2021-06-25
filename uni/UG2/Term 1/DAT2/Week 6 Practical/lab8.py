import sqlite3


def gettingHeaders(tup):
    returning = [tu[0] for tu in tup]
    return tuple(returning)


def formattingPrintings(table=None):
    # if table is not None:
    #     #c.execute("SELECT * FROM ?", (table, ))
    #     c.execute("SELECT * FROM :tableeq;", {'tableeq': table})  # doesn't work: OperationalError T.T awes pushing boundaries of programming going a bit tooo far for my novice level at times XOS
    print(gettingHeaders(c.description))
    for record in c.fetchall():
        print(record)
    return


file = "Property_Business_CHANGED.db"
conn = sqlite3.connect(file)
c = conn.cursor()


# c.execute("""ALTER TABLE Rental   RENAME COLUMN propertyID TO propertyNo""")
# c.execute("""DROP TABLE Property_Old;""")
# c.execute("""DROP TABLE Rental_Old;""")  # sigh what kerfuffles

# """
# QUESTION 1:
# Assume we have the left table - Tenant, and the right table - Rental. Create an INNER JOIN between
# these two tables, showing the attributes of : tenantID and tenantFName from the Tenant table;
# propertyNo and rentStart from the Rental table in your result. Display your result.
# You need to clearly show us the commands that have helped you to reach your answer.
# """
c.execute("""SELECT Tenant.tenantID, Tenant.tenantFName, Rental.propertyNo, Rental.rentStart
            FROM Tenant
            Inner JOIN Rental
            ON Tenant.tenantID=Rental.tenantID;""")
# inner join gives the intersection of the records in both tables - in Tenant AND Rental
# formattingPrintings()

# """
# QUESTION 2:
# Assume we have the left table - Property, and the right table - Rental. Create a LEFT JOIN between
# these two tables, showing the attributes of: tenantID and propertyNo from Rental table;
# propertyAddress and rentFee from Property table in your result. Display your result.
# You need to clearly show us the commands that have helped you to reach your answer.
# """
c.execute("""SELECT Rental.tenantID, Rental.propertyNo, Property.propertyAddress, Property.rentFee 
            FROM Property
            LEFT JOIN Rental
            ON Property.propertyNo=Rental.propertyNo;""")
# left outer join returns all records in the left table including the ones in the intersection of both tables - so includes NULL values most likely
# formattingPrintings()

# """
# QUESTION 3:
# Join the three tables: Tenant, Rental and Property. In your result, the following attributes should be
# shown: tenantID, propertyNo, and propertyAddress.
# You need to clearly show us the commands that have helped you to reach your answer.
# """
c.execute("""SELECT Tenant.tenantID, Property.propertyNo, Property.propertyAddress
            FROM Tenant
            INNER JOIN Rental
            ON Rental.tenantID=Tenant.tenantID
            INNER JOIN Property
            ON Rental.propertyNo=Property.propertyNo;""")
# getting intersections, yuppies
# formattingPrintings()

# """
# QUESTION 4:
# Owner John Kent has changed his id to ow400. Write a statement to make this change in the
# database. You need to clearly show us the commands that have helped you to reach your answer.
# """
# # need to make a new table
# c.execute("""BEGIN TRANSACTION;""")
# c.execute("""ALTER TABLE Property RENAME TO Property_Old;""")
# c.execute("""
#             CREATE TABLE Property
#             (
#                 propertyNo TEXT PRIMARY KEY NOT NULL,
#                 propertyAddress TEXT,
#                 rentFee INTEGER,
#                 ownerID TEXT,
#                 FOREIGN KEY(ownerID) REFERENCES Owner(ownerID) ON UPDATE CASCADE
#             );
# """)
# c.execute("""
#             INSERT INTO Property (propertyNo, propertyAddress, rentFee, ownerID)
#             SELECT propertyNo, propertyAddress, rentFee, ownerID
#             FROM Property_Old;""")
# c.execute("""
#             COMMIT;
# """)
# c.execute("""
#             BEGIN TRANSACTION;
# """)
# c.execute("""            ALTER TABLE Rental RENAME TO Rental_Old;
# """)
# c.execute("""CREATE TABLE Rental (
#                 tenantID TEXT NOT NULL,
#                 propertyNo TEXT NOT NULL,
#                 rentStart TEXT,
#                 rentFinish TEXT,
#                 PRIMARY KEY (tenantID, propertyNo),
#                 FOREIGN KEY (tenantID) REFERENCES Tenant(tenantID),
#                 FOREIGN KEY (propertyNo) REFERENCES Property(propertyNo) ON UPDATE CASCADE
#             );""")
# c.execute("""
#             INSERT INTO Rental (tenantID, propertyNo, rentStart, rentFinish)
#             SELECT tenantID, propertyNo, rentStart, rentFinish FROM Rental_Old;""")
# c.execute("""
#             COMMIT;""")
# c.execute("""
#             DROP Table Rental_Old;""")
# c.execute("""
#             DROP TABLE Property_Old;
#             """)
# # i dont actually know why this whole recreating tables kerfuffle was needed, hmmmmmm
# # actually maybe to rename the foreign key as well and keep consistency cuz we don't know if it was kept? hmmmm
# # update cascade ensures that foreign keys are changed in and deleted from both tables ~ are kept synchronous
# # and finally
c.execute("""UPDATE Owner
            SET ownerID = 'ow400'
            WHERE ownerName='John Kent';""")
c.execute("COMMIT;")  # to end transaction
c.execute("SELECT * FROM Owner")
# formattingPrintings()

# """
# QUESTION 5:
# In the Tenant table drop the column tenantFName, and rename tenantLName to tenantName. You
# need to clearly show us the commands that have helped you to reach your code.
# """
c.execute("""
BEGIN TRANSACTION;""")
c.execute("""
ALTER TABLE Tenant RENAME TO Tenant_Old;""")
c.execute("""
CREATE TABLE Tenant (
    tenantID TEXT PRIMARY KEY NOT NULL,
    tenantName VARCHAR
);""")
c.execute("""
INSERT INTO Tenant (tenantID, tenantName)
SELECT tenantID, tenantLName FROM Tenant_Old""")
c.execute("""
COMMIT;
""")  # need to seperate different statements out by ; and execute methodsss
# need to alter Rental table as well due to foreign key of tenant I presume
c.execute("""
BEGIN TRANSACTION;""")
c.execute("""
ALTER TABLE Rental RENAME TO Rental_Old;""")
c.execute("""
CREATE TABLE Rental (
    tenantID TEXT NOT NULL,
    propertyNo TEXT NOT NULL,
    rentStart TEXT,
    rentFinish TEXT,
    PRIMARY KEY (tenantID, propertyNo),
    FOREIGN KEY (tenantID) REFERENCES Tenant(tenantID),
    FOREIGN KEY (propertyNo) REFERENCES Property(propertyNo) ON UPDATE CASCADE
)
""")
c.execute("""
INSERT INTO Rental (tenantID, propertyNo, rentStart, rentFinish)
SELECT tenantID, propertyNo, rentStart, rentFinish FROM Rental_Old;
""")
c.execute("COMMIT")
c.execute("DROP TABLE Rental_Old;")
c.execute("DROP TABLE Tenant_Old;")
c.execute("SELECT * FROM Tenant")
formattingPrintings()
c.execute("SELECT * FROM Rental")
# formattingPrintings()

# QUESTION 6
# Add a column to Property table: telNum. You need to clearly show us the commands that have
# helped you to reach your code.
c.execute("ALTER TABLE Property ADD telNum INTEGER;")
c.execute("SELECT * FROM Property")
# formattingPrintings()
# Now, add the telephone number for P104: 345 671 8853 | P107: 3457874545 | P36: 3456761234 |
# P200: 3456713344. You need to clearly show us the commands that have helped you to reach your
# code.
c.execute("""UPDATE Property
SET telNum = 3456718853
WHERE propertyNo='P104'""")
c.execute("""UPDATE Property
SET telNum = 3457874545
WHERE propertyNo='P107'""")
c.execute("""UPDATE Property
SET telNum = 3456761234
WHERE propertyNo='P36'""")
c.execute("""UPDATE Property
SET telNum = 3456713344
WHERE propertyNo='P200'""")
c.execute("SELECT * FROM Property")
# formattingPrintings()


# QUESTION 7:
# Write a query to check whether we have a rent that starts ’31-Jan-96’ in the Rental table or not. If
# we do not have any of this date, then all other dates should be displayed. You need to clearly show
# us the commands that have helped you to reach your code.
c.execute("""
SELECT * FROM Rental
WHERE NOT EXISTS (SELECT rentStart FROM Rental
WHERE rentStart = '31-Jan-96');
""")  # remember exists works as boolean
# formattingPrintings()  # doesn't exist so returns all other records due to NOT EXISTS (huh kinda like for all is the inverse of there exists, hmmm)

# QUESTION 8:
# For each property if there exists less than 2 owners, return all the records, else return false . You
# need to clearly show us the commands that have helped you to reach your code.
c.execute("""
SELECT * FROM Rental
WHERE EXISTS (SELECT propertyNo, COUNT(ownerID) as totalOwners FROM Property
GROUP BY propertyNo HAVING COUNT (ownerID) < 2);
""")
# formattingPrintings()

# QUESTION 9:
# Write a query to show the properyNo, rentFee for the owner named Tim Cox. Display your result.
# You need to clearly show us the commands that have helped you to reach your code.
c.execute("""
SELECT propertyNo, rentFee FROM Property
WHERE ownerID=(SELECT ownerID FROM Owner WHERE ownerName='Tim Cox')""")
# formattingPrintings()

# QUESTION 10:
# Create a query to list all property whose rent fee is greater than the average rent fee, and list by how
# much their rent fee is greater than the average. You need to clearly show us the commands that
# have helped you to reach your code.
c.execute("""
SELECT propertyNo, propertyAddress, rentFee - (SELECT AVG(rentFee) FROM Property) AS rentFee_difference
FROM Property WHERE rentFee > (SELECT AVG(rentFee) FROM Property);
""")
# formattingPrintings()  # only one property so very above hum

# QUESTION 11:
# For each rentStart (e.g., 1-July-94), list the tenant ID who rent properties, and the address and rent
# fee of the properties they rent. You need to clearly show us the commands that have helped you to
# reach your code.
c.execute("""SELECT Rental.tenantID, rentStart, propertyAddress, rentFee
From Rental, Property
WHERE Rental.propertyNo=Property.propertyNo;
""")
# formattingPrintings()

# Write a query to list all properties that exist but are not been rented. You need to clearly show us
# the commands that have helped you to reach your code.
c.execute("""
SELECT propertyNo FROM Property
EXCEPT SELECT propertyNo FROM Rental;
""")
# formattingPrintings()

c.execute("""
SELECT SUM(rentFee) as rentTotal FROM Property WHERE propertyNo=(SELECT propertyNo
FROM Rental WHERE tenantID="t121");
""")
formattingPrintings()


conn.commit()
conn.close()