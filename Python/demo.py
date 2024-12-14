import psycopg2
from camelcase import CamelCase
c = CamelCase()



class Sql_operation:
    def __init__(self):
        self.conn = psycopg2.connect(database="postgres",
                        host="localhost",
                        user="postgres",
                        password="postgreDB@900",
                        port="5432")
    def close(self):
        self.conn.close()
        
    def creating_table(self):
        
        cursor = self.conn.cursor()

        cursor.execute('drop table if exists new_table ')
        creating_table= '''CREATE TABLE IF NOT EXISTS NEW_TABLE(
        ID INT PRIMARY KEY,
        NAME VARCHAR(20),
        SALARY INT ,
        DEPT_NAME VARCHAR(20)
        )
        '''
        cursor.execute(creating_table)
        self.conn.commit()


    def inserting_values(self,id,name,salary,dept_name ):
        cursor = self.conn.cursor()
        namedict = ({ "ID":id,"NAME":name, "SALARY":salary ,"DEPT_NAME":dept_name},)
        
        cursor.executemany("""INSERT INTO NEW_TABLE(ID, NAME,SALARY,DEPT_NAME) VALUES (%(ID)s, %(NAME)s , %(SALARY)s , %(DEPT_NAME)s)""", namedict)
        
        self.conn.commit()

    def update(self,name):
        c.hump(name)
        cursor = self.conn.cursor()
        id_dict = { "ID":1, "name":name ,  "dept_name":"DP4"}
        query = "UPDATE new_table SET name = %(name)s ,DEPT_NAME= %(dept_name)s WHERE id = %(ID)s "
        cursor.execute(query, id_dict)
        self.conn.commit()

    def delete(self,id):
        id_delete ={"id":id}
        cursor = self.conn.cursor()
        delete_query = """delete from new_table where id = %(id)s"""
        cursor.execute(delete_query,id_delete)
        self.conn.commit()
    
  
demo =Sql_operation()
demo.creating_table()
demo.inserting_values(1,"faris",2000,"DP1")
demo.inserting_values(2,"faris",2000,"DP1")
demo.update("faris")
demo.delete(3)
demo.close()




































































# class sql_operation:

#     def create():


# cursor.execute('drop table if exists new_table ')
# creating_table= '''CREATE TABLE IF NOT EXISTS NEW_TABLE(
# ID INT PRIMARY KEY,
# NAME VARCHAR(20),
# SALARY INT ,
# DEPT_NAME VARCHAR(20)
# )
# '''
# cursor.execute(creating_table)


# def insert():  

    




 

    
    # cursor.execute(f''' UPDATE new_table
    #                 SET NAME ='{name}'
    #                 WHERE id = 1''')

    # query = "UPDATE {table_name} SET {data} WHERE id = {id};".format(table_name=table_name, data=data, id=id)
    
    # id_dict = { "ID":2}
    # query = "UPDATE new_table SET name = 'faris' WHERE id = %(ID)s"
    # cursor.execute(query, id_dict)


    
    # print(cursor.fetchone())
    # update_salary = 'update NEW_TABLE set salary = salary + (salary * 0.1)'
    # cursor.execute(update_salary)



# def delete():
#     delete_row = 'delete from new_table where name = %(id)s '
#     delete_name = ('faris',)
#     cursor.execute(delete_row,delete_name)

# insert()
# update("faris")

# conn.commit()
        








# print()
# cursor.execute("SELECT * FROM T_user ")
# # cursor.execute()





# columns = [col[0] for col in cursor.description]
# print([dict(zip(columns, row)) for row in cursor.fetchall()])





#a = cursor.fetchall()
#print(a)
# # json_data = [json.loads(row[0]) for row in a]

# # print(json_data)
# # print(cursor.fetchall())
# # key_value_dict = {row[0]: row[1] for row in a}
# # print(key_value_dict)
