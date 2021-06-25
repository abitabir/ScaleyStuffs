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

conn = sqlite3.connect("movies.db")
c = conn.cursor()

"""
Q1: If you look at your result, who is Sally Adam’s supervisor?
Q2: Write a query so that the result lists member number, first name and last name of all members
recorded in the DB.
Q3: Write a query to list the set of cities in which Distribution Centres are based. Note: we do not
want any repetition of cities in our result.
Q4: Write a query that lists the weekly salary of all staff members. How much does Sally Adams earn
per week?
Q5: Write a query to list all rows from the DVDOrderLine table where the order quantity is less than
4. Since quantity is of TEXT data type in the table, we need single quotes in our query: ‘4’
Q6: Write a query so that the result lists the full details of all Staff members who earn at least
$30000 but less than $40000 per year.
Q7: From Q6 how many records were returned?
Q8: Write a query so that the result lists the full details of all distribution centres where the street
address ends in ‘Avenue’.
Q9: Write a query to show all details of all actors listed in alphabetical order by actor name.
Q10: From Q9, in your result, what is the name of the actor in the second record?

"""

c.execute("SELECT * FROM Staff;")
# formattingPrintings()  # Sally Adam's supervisor is Tom Daniels, yup

c.execute("SELECT memberNo, mfName, mlName FROM Member;")
# formattingPrintings()

c.execute("SELECT DISTINCT dCity FROM DistributionCenter;")
# ugh spelling americanisms XP
# formattingPrintings()

c.execute("""SELECT salary/52 AS weeklySalary FROM Staff;""")
# formattingPrintings()  # Sal Adams earns $576 per week

c.execute("""SELECT * FROM DVDOrderLine
            WHERE quantity<'4';""")
# Comparatively, an effective way would be the use of CAST() Function
# SELECT * FROM DVDOrderLine WHERE CAST(quantity AS INT)<4;
# formattingPrintings()

c.execute("""SELECT * FROM Staff
            WHERE salary >= 30000 AND salary < 40000;""")
# formattingPrintings() # two records returned in range

c.execute("""SELECT * FROM DistributionCenter
            WHERE dStreet LIKE '%Avenue';""")
# formattingPrintings()

c.execute("""SELECT * FROM Actor ORDER BY actorName ASC;""")
# formattingPrintings()
# Elijah Wood is the actor represented by the second record

"""
Another important function of SQL is to allow users to modify data. The three main commands are
UPDATE, INSERT and DELETE.
Q11: Write a query to increase the salary of all managerial staff by 2%.
Now check that the INSERT has taken place by performing an appropriate SELECT command.
**********************************************************************************
A new member has joined the library. His details are as follows:
memberNo - M166785
mfName - Richard
mlName - Head
mStreet – 2 Hope Street
mCity - Portland
mState - OR
mZipCode – 97233
This is not a complete row. The values for the member’s e-mail, password and membership type are
not yet known, so you will need to specify a field or column list after the table name, otherwise SQL
will be expecting values for all fields.
Q12: Complete the following query to add this new member:
INSERT [ ] [ ] (memberNo, mfName, mlName, [ ], mCity, mState, [ ]) VALUES (‘M166785’, ‘Richard’,
[ ],’2 Hope Street’, ‘Portland’, ‘OR’, [ ]);
2
DATA2 (Data Analysis and Management)
Now check that the INSERT has taken place by performing an appropriate SELECT command.
**********************************************************************************
You have just discovered that the new member record for Richard Head was entered in error.
Review the DELETE command syntax and construct a command to remove this record from the DB.
Q13: Write a query to remove Richard Head (M166785) from the member table of the database.
Once again, use a SELECT to check that the change has taken place. 
"""

c.execute("SELECT * FROM Staff")
print("before change:")
formattingPrintings()
c.execute("""UPDATE Staff
            SET salary = salary * 1.02
            WHERE position = 'Manager';""")
### formattingPrintings() # only setting rn so this returns None
c.execute("SELECT * FROM Staff")
print("after change:")
formattingPrintings()

# adding member
# c.execute("SELECT mZipCode FROM Member WHERE mfName='Serena';")  # tried checking data type of mZipCode using this - text
# formattingPrintings()
# c.execute("""INSERT INTO Member (memberNo, mfName, mlName, mStreet, mCity, mState, mZipCOde)
#             VALUES ('M166785', 'Richard', 'Head', '2 Hope Street', 'Portland', 'OR', '97233');""")
# better to use parameterised SQL for INSERT statements tbf for security by averting SQL injection attacks e.g
c.execute("""INSERT INTO Member (memberNo, mfName, mlName, mStreet, mCity, mState, mZipCOde)
            VALUES (?, ?, ?, ?, ?, ?, ?);""", ('M166785', 'Richard', 'Head', '2 Hope Street', 'Portland', 'OR', '97233'))
c.execute("SELECT * FROM Member;")  # checking if new member added
formattingPrintings()

# deleting member
c.execute("""DELETE FROM Member WHERE memberNo = 'M166785'""")
c.execute("SELECT * FROM Member;")  # checking if new member errorneously added deleted
formattingPrintings()


conn.commit()

conn.close()




