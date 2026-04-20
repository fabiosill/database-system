import mysql.connector
conexao = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    database='crudpython'
)
sql = conexao.cursor()

def options():
    return int(input(
        "\n===== This is a database CRUD system :) ======\n\n"
        "1.CREATE | 2.READ | 3.UPDATE | 4.DELETE | 0.FINISH\n"
    ))

# === CREATE ===

def sqlcreate():
    dtname = input("Name: \n")
    dtage = input("Age: \n")
    dtcell = input("Cellphone: \n")
    dtemail = input("E-mail: \n")

    cmdsqlinsert = f'INSERT INTO crudpython (sqlname, sqlage, sqlcell, sqlemail) VALUES ("{dtname}", "{dtage}", "{dtcell}", "{dtemail}")'

    sql.execute(cmdsqlinsert)
    conexao.commit()
    print("Create successfully")

# === READ ===
def sqlread():
    commandread = 'SELECT * FROM crudpython'
    sql.execute(commandread)
    resultado = sql.fetchall()
    print("\nTable")
    for linha in resultado:
        print(f"ID: {linha[0]} | Name: {linha[1]} | Years Old: {linha[2]} | Cellphone: {linha[3]} | Email: {linha[4]}")

# === UPDATE ===
def sqlupdate():
    idupdate = input("ID: ")
    collumnoupdate = int(input("UPDATE: 1.NAME | 2.AGE | 3.CELL | 4.EMAIL | 0.RETURN \n=>: "))
    valueupdate = input("New value: ")

    if collumnoupdate == 1:
        collumnoupdate = "sqlname"
    elif collumnoupdate == 2:
        collumnoupdate = "sqlage"
    elif collumnoupdate == 3:
        collumnoupdate = "sqlcell"
    elif collumnoupdate == 4:
        collumnoupdate = "sqlemail"
    else:
        return

    sql.execute(f"UPDATE crudpython SET {collumnoupdate} = '{valueupdate}' WHERE sqlid = {idupdate}")
    conexao.commit()
    if sql.rowcount:
        print("Updated successfully")
    else:
        print("ID not found")

# === DELETE ===
def sqldelete():
    iddelete = input("ID: ")
    commanddelete = f'DELETE FROM crudpython WHERE sqlid = {iddelete}'
    sql.execute(commanddelete)
    conexao.commit()

    if sql.rowcount:
        print("Deleted successfully")
    else:
        print("ID not found")

option = options()

while option != 0:

    if option == 1:
        sqlcreate()
        option = options()

    elif option == 2:
        sqlread()
        option = options()

    elif option == 3:
        sqlupdate()
        option = options()

    elif option == 4:
        sqldelete()
        option = options()

    else:
        break
