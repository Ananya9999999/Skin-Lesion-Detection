import mysql.connector as mysqltor
def db_connection():
  connection= mysqltor.connect(
    host= 'localhost',
    user='root',
    password= 'pass',
    databse= 'skin_lesion_db'
  )
  return connection
