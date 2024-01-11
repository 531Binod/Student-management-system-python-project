import mysql.connector
conn=mysql.connector.connect(host='localhost',username='root',password='Binod@xxxx',database='bagar')
my_curser=conn.cursor()
conn.commit()
conn.close()
print('successfully')