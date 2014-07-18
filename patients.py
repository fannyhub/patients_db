import sqlite3 as lite
import sys


try:
    con = lite.connect('wizyty.db')
    with con:
        cur = con.cursor()
        cur.execute("CREATE TABLE Patients(Id INT, Name TEXT, Surname TEXT, Pesel INT, Description TEXT)") 
        number = 0
        while raw_input('Should I add a new patient? yes/no\n') == 'yes':
            
            Id = number+1
            number = Id
            Name = raw_input('Name: ')
            Surname = raw_input('Surname: ')
            Pesel = int(raw_input('Pesel: '))
            Description = raw_input('Description: ')
            cur.execute("INSERT INTO Patients VALUES(Id, Name, Surname, Pesel, Description)")
    
        #.mode column
        #.headers on
except:
    print 'no milk today'
