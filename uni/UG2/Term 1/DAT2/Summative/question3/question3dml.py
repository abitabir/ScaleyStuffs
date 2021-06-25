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

# c.execute("""
# -- assuming length means the number of characters in the title string
# SELECT title, LENGTH(title) as title_length
# FROM D_DVD ORDER BY title_length ASC;
# """)
# formattingPrintings()

# c.execute("""
# SELECT * FROM D_DVD
# WHERE catalogNo=(SELECT catalogNo FROM E_DVDCOPY
# WHERE dCenterNo="B001" OR dCenterNo="B003");
# """)
# formattingPrintings()

# c.execute("""
# SELECT dCenterNo, total_salaries FROM (SELECT A_DistributionCenter.dCenterNo, SUM(B_Staff.salary) as total_salaries
# FROM B_Staff, A_DistributionCenter
# WHERE A_DistributionCenter.dCenterNo=B_Staff.dCenterNo) WHERE total_salaries > 50000;
# """)
# formattingPrintings()

# c.execute("""
# SELECT dCenterNo, COUNT(videoNo) as totalDVDCopy FROM E_DVDCOPY
# GROUP BY dCenterNo
# ORDER BY totalDVDCopy DESC; """)
# formattingPrintings()

#these all dont work but in interest of time T.T better than nothing uhuhm X'SSSS
# c.execute("""
# SELECT D_DVD.title, E_DVDCOPY.available FROM D_DVD, E_DVDCOPY
# WHERE D_DVD.supplierNo=(SELECT supplierNo FROM C_Supplier WHERE name="20th Century Fox Home Videos")
# """)
# formattingPrintings()

# c.execute("""
# UPDATE Staff
# SET name = 'Sally Daniels'
# SET salary = (SELECT salary + 1000 as new_salary FROM Staff WHERE staffNo ='S0003')
# WHERE staffNo ='S0003';
#
# """)
# formattingPrintings()


conn.commit()
c.close()