import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-LCE34S8\PRADEEPSQL;'
                      'Database=test;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM test.dbo.Student')

for row in cursor:
    print(row)