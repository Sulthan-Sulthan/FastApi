import psycopg2

conn = psycopg2.connect(database="postgres",
                        host="localhost",
                        user="postgres",
                        password="postgreDB@900",
                        port="5432")
cursor = conn.cursor()
# if cursor :
#     print("df")

cursor.execute("SELECT * FROM T_user ")
print(cursor.fetchall())
