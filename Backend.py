import mysql.connector as mysqltor
def db_connection():
  connection= mysqltor.connect(
    host= 'localhost',
    user='root',
    password= 'pass',
    databse= 'skin_lesion_db'
  )
def find_user(username):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user
if __name__ == '__main__':
    db_connection()
    find_user()
