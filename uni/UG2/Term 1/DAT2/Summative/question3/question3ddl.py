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


file = "DVD_XYZ.db"
conn = sqlite3.connect(file)
c = conn.cursor()

c.execute("""BEGIN TRANSACTION;""")
c.execute("""CREATE TABLE A_DistributionCenter (
                dCenterNo TEXT NOT NULL,
                dStreet TEXT,
                dCity TEXT,
                dState TEXT,
                dZipCode TEXT,
                staffNo TEXT,
                PRIMARY KEY (dCenterNo),
                FOREIGN KEY (staffNo) REFERENCES B_Staff(staffNo)
            );""")
c.execute("""COMMIT;""")

c.execute("""BEGIN TRANSACTION;""")
c.execute("""CREATE TABLE B_Staff (
                staffNo TEXT NOT NULL,
                name TEXT,
                position TEXT,
                salary TEXT,
                dCenterNo TEXT,
                PRIMARY KEY (staffNo),
                FOREIGN KEY (dCenterNo) REFERENCES A_DistributionCenter(dCenterNo)
            );""")
c.execute("""COMMIT;""")

c.execute("""BEGIN TRANSACTION;""")
c.execute("""CREATE TABLE C_Supplier (
                supplierNo TEXT NOT NULL,
                name TEXT,
                address TEXT,
                telNo TEXT,
                status TEXT,
                PRIMARY KEY (supplierNo)
            );""")
c.execute("""COMMIT;""")

c.execute("""BEGIN TRANSACTION;""")
c.execute("""CREATE TABLE D_DVD (
                catalogNo TEXT NOT NULL,
                title TEXT,
                genre TEXT,
                rating TEXT,
                supplierNo TEXT,
                PRIMARY KEY (catalogNo),
                FOREIGN KEY (supplierNo) REFERENCES C_Supplier(supplierNo)
            );""")
c.execute("""COMMIT;""")

c.execute("""BEGIN TRANSACTION;""")
c.execute("""CREATE TABLE E_DVDCOPY (
                videoNo TEXT NOT NULL,
                available TEXT,
                catalogNo TEXT,
                dCenterNo TEXT,
                PRIMARY KEY (videoNo),
                FOREIGN KEY (dCenterNo) REFERENCES A_DistributionCenter(dCenterNo),
                FOREIGN KEY (catalogNo) REFERENCES D_DVD(catalogNo)
            );""")
c.execute("""COMMIT;""")


# (ii)
c.execute("""INSERT INTO E_DVDCOPY (videoNo, available, catalogNo, dCenterNo)
VALUES

("178643", "False", "634817", "B001"),
("199004", "True", "207132", "B001"),
("200900", "True", "330553", "B002"),
("210087", "True", "902355", "B002"),
("243431", "True", "634817", "B002"),
("245456", "True", "207132", "B002"),
("245457", "True", "207132", "B002"),
("317411", "True", "781132", "B003");""")
c.execute("""COMMIT;""")
c.execute("""SELECT * FROM E_DVDCOPY""")
formattingPrintings()


c.execute("""INSERT INTO D_DVD (catalogNo, title, genre, rating, supplierNo)
VALUES

("207132", "Casino Royale", "Action", "PG-13", "S02"),
("330553", "Lord of the Rings III", "Action", "PG-13", "S04"),
("445624", "Mission Impossible III", "Action", "PG-13", "S03"),
("634817", "War of the Worlds", "Sci-Fi", "PG-13", "S05"),
("781132", "Shrek 2", "Children", "PG", "S03"),
("902355", "Harry Potter", "Children", "PG", "S01");""")
c.execute("""COMMIT;""")
c.execute("""SELECT * FROM D_DVD""")
formattingPrintings()

c.execute("""INSERT INTO C_Supplier (supplierNo, name, address, telNo, status)
VALUES
("S01", "Universal Home Videos", "100 Universal City Plaza", "8188666000", "OK"),
("S02", "MGM Home Videos", "2500 Broadway St, Santa Monica, CA, 90404", "8189002000", "OK"),
("S03", "Buena Vista Pictures", "1100 Santa Monica Bivid, CA, 90041", "3208406500", "OK"),
("S04", "Paramount Pictures", "5555 Melrose Avenue, Hollywood, CA, 90038", "3238621130", "OK"),
("S05", "20th Century Fox Home Video", "900 Center Plaza, Beverly Hills, CA, 90213", "6007772300", "OK");

""")
c.execute("""COMMIT;""")
c.execute("""SELECT * FROM C_Supplier""")
formattingPrintings()

c.execute("""
INSERT INTO B_Staff (staffNo, name, position, salary, dCenterNo)
VALUES
("S0003", "Sally Adams", "Snr Assistant", "30000", "B001"),
("S0010", "Mary Martinez", "Manager", "50000", "B002"),
("S0415", "Art Peters", "Manager", "41000", "B003"),
("S1500", "Tom Daniels", "Manager", "46000", "B001"),
("S2250", "Sally Stern", "Manager", "48000", "B004"),
("S2350", "Robert Chin", "Supervisor", "32000", "B002");
""")
c.execute("""COMMIT;""")
c.execute("""SELECT * FROM B_Staff""")
formattingPrintings()

c.execute("""INSERT INTO A_DistributionCenter (dCenterNo, dStreet, dCity, dState, dZipCode, staffNo)
VALUES
("B001", "8 Jefferson Way", "Portland", "OR", "97201", "S1500"),
("B002", "City Center Plazza", "Seattle", "WA", "98122", "S0010"),
("B003", "14 -8th Avenue", "New York", "NY", "10012", "S0415"),
("B004", "16 -14th Avenue", "Seattle", "WA", "98128", "S2250");
""")
c.execute("""COMMIT;""")
c.execute("""SELECT * FROM A_DistributionCenter""")
formattingPrintings()

conn.commit()
c.close()

