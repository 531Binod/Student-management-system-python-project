import mysql.connector
conn=mysql.connector.connect(host='localhost',username='root',password='Binod@1234',database='bagar')
my_curser=conn.cursor()
conn.commit()
conn.close()
print('successfully')