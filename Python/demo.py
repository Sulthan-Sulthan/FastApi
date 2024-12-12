import psycopg2
import json


try:
    conn = psycopg2.connect(database="postgres",
                            host="localhost",
                            user="postgres",
                            password="postgreDB@900",
                            port="5432")
    cursor = conn.cursor()

    CREATE_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS USER_DATA (
        T_userId SERIAL PRIMARY KEY,            -- Auto-increment primary key
        Name VARCHAR(200),                      -- Name with a maximum size of 200 characters
        first_Name VARCHAR(100) NOT NULL,       -- First name, not null
        last_Name VARCHAR(100) NOT NULL,        -- Last name, not null
        email VARCHAR(255) NOT NULL UNIQUE,     -- Email, must be unique and not null
        dateOfBirth DATE,                       -- Date of birth in DATE format
        createdOwner TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, -- Automatically set to current time
        createdBy VARCHAR(100) NOT NULL,        -- Name of the creator, not null
        modified TIMESTAMP                      -- Nullable column for last modification time
    );
    """
    cursor.execute(CREATE_TABLE_QUERY)
    conn.commit()
    print("")
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
except Exception as err:
    print(err)