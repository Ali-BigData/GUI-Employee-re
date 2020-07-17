import mysql.connector

all_err= ""

myhost          = "localhost"
myuser          ="root"
mypasswd    ="Zxcasd83"
mydatabase = "python"


try:
    
    conn= mysql.connector.connect(

        host= "localhost",
        user="root",
        passwd="Zxcasd83"
        )
    cur=conn.cursor()
    cur.execute(""" CREATE DATABASE IF NOT EXISTS python DEFAULT CHARACTER SET utf8
        DEFAULT COLLATE utf8 _general_ci  """)

    
except mysql.connector.Error as e:
    all_err += str(e)+ " . Please check Mysql server and user., "


try:
    
    conn= mysql.connector.connect(

        host= "localhost",
        user="root",
        passwd="Zxcasd83",
        database='python'
        )

    
except mysql.connector.Error as e:
    all_err += str(e)+ " , "


def dbrun(sql):
    try:
        
        if 'conn' in globals():
            cur = conn.cursor()
            cur.execute(sql)   
            conn.commit()
       
            return True
        
        else:
            return False
        
    except  mysql.connector.Error as e :
        all_err += str(e)+ " , "
        return False

def dbget (sql):
    try:
        if 'conn' in globals ():
            cur=conn.cursor()
            cur.execute(sql)
            all_rows= cur.fetchall()
            return all_rows
        else:
            return []

    except mysql.connector.Error as e:
        all_err+= str(e)+ " , "
        return []
def dbautonum (table, column):
    try:
        if 'conn' in globals():
            cur=conn.cursor()
            cur.execute("SELECT max(%s) +1 as autonum FROM %s " %( column , table))
            row= cur.fetchone()
            if row[0]==None:
                return "1"
            else:
                return row[0]
        else:
            return ""
    except mysql.connector.Error as r:
        all_err +=str(r)
        return ""
   


   
        
  
        

            
