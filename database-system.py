import mysql.connector
conexao = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    database='crudpython'
)
sql = conexao.cursor()

def sqlcreate():
    commandcreate = 'CREATE TABLE IF NOT EXISTS crudpython (sqlid INT AUTO_INCREMENT PRIMARY KEY, sqlname VARCHAR(60), sqlage TINYINT, sqlnum TINYINT, sqlemail VARCHAR(100))'
    sql.execute(commandcreate)
    conexao.commit()
    print("Table was created successfully")

def sqlupdate():
    commandupdate = f'INSERT INTO crudpython (sqlname, sqlage, sqlnum, sqlemail) VALUES ("{dtname}", "{dtage}", "{dtnum}", "{dtemail}")'
    sql.execute(commandupdate)
    conexao.commit()
    print("Update was successfully")

def sqlread():
    commandread = f'SELECT * FROM '
    sql.execute(commandread)
    resultado = sql.fetchall()
    print("\nTable")
    for linha in resultado:
      print(f"ID: {linha[0]} | Name: {linha[1]} | Years Old: {linha[2]} | Number: {linha[3]} | Email: {linha[4]}")
      
def sqldelete():
    commanddelete = f'DROP DATABASE crudpython'
    print("Table was deleted successfully")

def options():
    return int(input(
        "\n===== This is a database CRUD system :) ======\n\n"
        "1.Create | 2.Read | 3.Update | 4.Delete | 0.Finish\n"
    ))

def optioninsert():
    return int(input("This is a create section, then what values do you would like to insert" \
        "\n VALUES: 1.NAME | 2.AGE | 3.NUM | 4.EMAIL | 0.NO ONE"))

def insertname():
    dtname = input("Insert a new name\n")
    cmdinsertname = f'INSERT INTO crudpython (sqlname) VALUES ("{dtname}")'
    sql.execute(cmdinsertname)
    conexao.commit()
    print("Name inserted successfully")

def insertage():
    dtage = input("Insert a new age\n")
    cmdinsertage = f'INSERT INTO crudpython (sqlage) VALUES ("{dtage}")'
    sql.execute(cmdinsertage)
    conexao.commit()
    print("Age inserted successfully")

def insertnum():
    dtnum = input("Insert a new number\n")
    cmdinsertnum = f'INSERT INTO crudpython (sqlnum) VALUES ("{dtnum}")'
    sql.execute(cmdinsertnum)
    conexao.commit()
    print("Number inserted successfully")

def insertemail():
    dtemail = input("Insert a new email\n")
    cmdinsertemail = f'INSERT INTO crudpython (sqlemail) VALUES ("{dtemail}")'
    sql.execute(cmdinsertemail)
    conexao.commit()
    print("Email inserted successfully")

option = options()
insert = optioninsert()

while option != 0:

    if option == 1:
        optioninsert()

        if insert == 1:
            insertname()
        elif insert == 2:
            insertage()
        elif insert == 3:
            insertnum()
        elif insert == 4:
            insertemail()
        else:
            option = options()

    elif option == 2:
        sqlread()
        option = options()

    elif option == 3:
        dtname = input("This is the Name collumn, please enter a new name\n")
        dtage = int(input("This is the Age collumn, please enter a new age\n"))
        dtnum = int(input("This is the Number collumn, please enter a new name\n"))
        dtemail = input("This is the E-mail collumn, please enter a new name\n")
        option = options()

    elif option == 4:
        sqldelete()
        option = options()

    else:
        break