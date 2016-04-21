#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('/home/pi/Documents/Python_projects/Database/My_Python_SqliteDB')
print "opened database good"

cursor = conn.execute( "select * from audiofilelist " )
#cursor = conn.execute( "select date('now') " )
for row in cursor:
    print row, "\n"

conn.close()


