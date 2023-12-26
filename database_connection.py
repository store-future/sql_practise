''' in this module ----
1- we will build connection with our mysql server
2- then make a test database into our sql server
'''

import mysql.connector

# making connection with database
cunn = mysql.connector.connect(host = 'localhost' , user = 'root' , password = 'dddddddd')


def connection_conf():
    # printing conection id 
    connection_id = cunn.connection_id

    #printing current version of mysql-server
    server_version = cunn.get_server_version()

    # checking do we connected or not
    check_cunn = cunn.is_connected()

    result = f"conection id :{connection_id} \ncurrent version of mysql-server :{server_version} \nchecking if connected or not : {check_cunn}"
    return(result)
# print(connection_conf())

# creating a cursor object to execute sql query
cursor = cunn.cursor()

#creating test database
cursor.execute("CREATE DATABASE if not exists test")

# selecting all the databases
cursor.execute("show databases")
print(cursor.fetchall())

