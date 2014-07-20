import sqlite3 as lite
import sys
 
 
try:
    
    con = lite.connect('wizyty.db')
    with con:
        cur = con.cursor()
         
        cur.execute("CREATE TABLE IF NOT EXISTS Patients_db(name TEXT, surname TEXT, date DATE, pesel INT, description TEXT)")
        answer = raw_input('Add a new patient: A\nShow whole database: D \nLook up a patient: S \nRemove patient: R \nQuit: Q\n')
        while  answer.upper() <> 'Q':
            if answer.upper() == 'A':
            
                name = raw_input('First name:')
            
                surname = raw_input('Surname:')
                date = raw_input('Date of the visit:')
                pesel = int(raw_input('Pesel:'))
                description = raw_input('Description:')
                patient = (name, surname, date, pesel, description)
                cur.execute("INSERT INTO Patients_db VALUES(?,?,?,?,?)", patient)
                
                
            elif answer.upper() == 'D':
                cur.execute("SELECT * from Patients_db")
                rows = cur.fetchall()
                for row in rows:
                    print row
                    
            elif answer.upper() == 'S':
                
                person = (raw_input("Last name:\n"),)
                cur.execute("SELECT * from Patients_db WHERE Surname=?",person)
                
                row = cur.fetchall()
                print row
                
            elif answer.upper() =='R':
                person = (raw_input("Last name, please: \n"),)
                print person
                cur.execute("DELETE from Patients_db WHERE surname=?",person)
                
            else:
                pass

            answer = raw_input('A/S/D/R/Q?\n')
            
except Exception, e:
    print e
