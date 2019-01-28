
#!/usr/bin/python
# coding=utf-8
import pymysql.cursors
'''
Para hacer la interacción con la base de datos
se ha importado la libreria pymysql,
la documentación se puede revisar en el siguiente enlace:
https://pymysql.readthedocs.io/en/latest/user/examples.html
'''

#creación de la base de datos
'''
Este método permite la creación de la base de datos 
con Gmail_Filter como nombre por defecto
'''
def CreateDB (usr,pwd):
    connection = pymysql.connect(host='localhost',
    user=usr,password=pwd)
    try:
        with connection.cursor() as cursor:
            cursor.execute('CREATE DATABASE IF NOT EXISTS Gmail_Filter' )
    finally:
        connection.close()

# Creación de tabla
'''
Este método ejecuta el Query qeu permite la creación 
de la tabla con nombre por defecto data2
'''
def CreateTable(usr,pwd):
    connection = pymysql.connect(host='localhost',user=usr,password=pwd,db='Gmail_Filter', cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            Query= "CREATE TABLE IF NOT EXISTS data2(id int AUTO_INCREMENT, Fecha varchar(1000), Remitente varchar(1000), Asunto varchar(1000), PRIMARY KEY (id))"   
            cursor.execute(Query)

    finally:
        connection.close()

#insercion de data
def InsertData(usr,pwd,Fecha,Remitente,Asunto):
    connection = pymysql.connect(host='localhost',user=usr,password=pwd,db='Gmail_Filter',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql= "INSERT INTO `data2` (`Fecha`, `Remitente` , `Asunto`) VALUES (%s, %s,%s)" 
            cursor.execute(sql, (Fecha,Remitente,Asunto))
            connection.commit()
    finally:
        connection.close()











