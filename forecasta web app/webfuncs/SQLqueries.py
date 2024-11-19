import pg8000


def already_exists(Table,FieldName,Data):
    connection = pg8000.connect(database="ForecastaDB", user="postgres", password="Password123!", host="localhost", port="5432")
    cursor = connection.cursor()

    query = f"SELECT EXISTS (SELECT 1 FROM {Table} WHERE {FieldName} = %s);"

    cursor.execute(query,(Data,))
    Data_Exists = cursor.fetchone()
    
    connection.commit()  
    cursor.close() 
    connection.close()
    return Data_Exists[0]


#fieldnames is a list,Data is a list
def conditional_insert_data(Table,FieldNames,Data,Field,Value):
    connection = pg8000.connect(database="ForecastaDB", user="postgres", password="Password123!", host="localhost", port="5432")
    cursor = connection.cursor()
    formatted_fields = ", ".join(FieldNames)
    variable_placeholders = ", ".join(["%s"] * len(Data))
    query = f"INSERT INTO {Table} ({formatted_fields}) VALUES({variable_placeholders}) WHERE {Field} = {Value};"
    cursor.execute(query,(tuple(Data),))
    connection.commit() 
    cursor.close() 
    connection.close()

def insert_data(Table,FieldNames,Data):
    connection = pg8000.connect(database="ForecastaDB", user="postgres", password="Password123!", host="localhost", port="5432")
    cursor = connection.cursor()
    formatted_fields = ", ".join(FieldNames)
    variable_placeholders = ", ".join(["%s"] * len(Data))
    query = f"INSERT INTO {Table} ({formatted_fields}) VALUES ({variable_placeholders});"
    cursor.execute(query,(tuple(Data)))
    connection.commit()  
    cursor.close() 
    connection.close()