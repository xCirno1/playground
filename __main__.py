import sqlite3

con = sqlite3.connect("test.db")
con.execute("CREATE TABLE data (a INT)")
con.commit()
