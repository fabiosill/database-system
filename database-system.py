## database

dtname = ["Fabio", "Arthur", "Henrique"]
dtage = [25, 18, 23]
dtcity = ["S.A", "SBC", "SC"]

def congrats():
    print("Congratulations, the data was added with successfuly")
def options():
    return int(input("\n===== This is a database system :) ======\n\nWhich collumn you gonna to open\n 1.Name | 2.Age | 3.City | 4.Consult | 0.Finish\n"))

option = options()

while option != 0:

    if option == 1:
        newname = input("This is the Name collumn, please enter a new name\n")
        dtname.append(newname)
        congrats()
        option = options()
    elif option == 2:
        newage = input("This is the Age collumn, please enter a new age\n")
        dtage.append(newage)
        congrats()
        option = options()
    elif option == 3:
        newcity = input("This is the City collumn, please enter a new name\n")
        dtcity.append(newcity)
        congrats()
        option = options()
    elif option == 4:
        consulttable = int(input("Which collumn you would like to consult\n 1 - Name | 2 - Age | 3 - City | 0 - Left\n"))
        if consulttable == 1:
            print(f"This is the Name collunm\n{dtname}")
        elif consulttable == 2:
            print(f"This is the Age collunm\n{dtage}")
        elif consulttable == 3:
            print(f"This is the City collunm\n{dtcity}")
        else:
            print("\n")
            option = options()
    else:
        break