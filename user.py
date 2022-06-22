from modules import inserts;
# Exporting Functions and I am using time for delaying stuff by milliseconds because.... I am bored 😊
import time
def option(db, table):
    showTableList=['table','tables','t',"show-table","showtable","show table",'st'];showRecordList=["show-record","show-records","show record","show records","showrecord","showrecords",'sr','r','record','records'];showDatabaseList=["show database","show-database","show databases","show-databases","show-db","show db",'sdb'];showUserList=['show users','show user','show-users','show user','su'];
    sqlcursor=db.cursor()
    stInput = input("What would you like to view in your database?\n\n- table => fetch all the tables available in database\n- record => queries and gets a specific or every record in database's table\n- database => shows all databases available in the server\n- users => shows all the users who are able to connect the database\n\n\n|| -> ").lower();
    if stInput in showTableList:
        print('Fetching Data.... Please wait for a moment.')
        sqlcursor.execute('SHOW TABLES')
        for items,data in enumerate(sqlcursor.fetchall()):
            time.sleep(0.1)
            print(f'Table {items+1} => {data[0]}')
        return print('End of the list of available tables in the database.');sqlcursor.close()
    elif stInput in showRecordList:
        askIfLoop=input('Do you want to fetch your results with specific condition? (y/n)\n =>').lower()
        loop=True
        allOptions=['y','ye','yes','sure','no','n'];positiveReply=['y','yes','ye','sure']
        while loop==True:
            if askIfLoop in allOptions and askIfLoop not in positiveReply:
                print("Please wait.... We are fetching data from the database.");time.sleep(0.3)
                sqlcursor.execute(f"SELECT * FROM {table} LIMIT 90")
                for x in sqlcursor.fetchall():
                    print('----------------------------------------------------------------------------------------------')
                    for items,data in enumerate(x):
                        time.sleep(0.1)
                        print(f"{sqlcursor.description[items][0]} => {data}")
                    print('----------------------------------------------------------------------------------------------')
                return print('End of the List. (LIMIT => 90)');sqlcursor.close();loop=False
            elif askIfLoop in positiveReply:
                sqlcursor.execute(f'SELECT * FROM {table} LIMIT 1');time.sleep(0.1)
                sqlcursor.fetchone();#Just to clear that "unread error"
                fieldList=[]
                for fieldName in sqlcursor.description:
                    print(fieldName[0])
                    fieldList.append(fieldName[0].lower())
                print('Here are the available fields to choose from.')
                opt=input('By What field do you want to fetch data from? \n=> ')
                if opt.lower() in fieldList:
                    valueToAsk=input("Please enter the value by which field you're searching the database\n =>")
                    sqlcursor.execute(f"SELECT * FROM {table} WHERE {opt}='{valueToAsk}' LIMIT 90")
                    for x in sqlcursor.fetchall():
                        print('----------------------------------------------------------------------------------------------')
                        for items,data in enumerate(x):
                            print(f"{sqlcursor.description[items][0]} => {data}")
                        print('----------------------------------------------------------------------------------------------')
                        return print("End of the List (Limit => 90)");sqlcursor.close()
                else:
                    return print('Invalid Option Registered, please try again.');sqlcursor.close()
    elif stInput in showDatabaseList:
        print('Fetching Database(s), Please Wait...')
        sqlcursor.execute("SHOW DATABASES")
        for items,data in enumerate(sqlcursor.fetchall()):
            time.sleep(0.1)
            print(f"{items+1} => {data[0]}")
        return print("End of the list.");sqlcursor.close();
    elif stInput in showUserList:
        print('Fetching Management User data, Please wait......');sqlcursor.execute('SELECT User from mysql.user;')
        for item,data in enumerate(sqlcursor.fetchall()):
            time.sleep(0.1)
            print(f"User {item+1} => {data[0]}")
        print("End of User's List who can access the database")
    else:
        return print('Invalid Option found, Please try again.')
# End of "Viewing Option"

def settings(db, table):
    sqlcursor=db.cursor()
    ask=input("What would you like to go through in settings of the database?\n\n\n- insert => Inserts amount of records you want to register in the database.\n- drop-table (won't work) => Deletes/Drops a table in the database.\n- delete-record (won't work) => Deletes the registered Data in the table (specific/all).\n\n\n=> ").lower();
    insertList=["mass-insert",'mass insert','add','insert','inserts','i']
    if ask in insertList:
        toAdd=int(input("Please Enter the amount of rows you want to register\n|| -> "))
        while toAdd==0:
            print("Please enter a valid value between 1 - 99")
        fieldList=[];# List to store "To Insert"'s data in tuple
        tempList=[];#"To Store Data" in List form which will be converted into tuple then inserted into fieldList
        for x in range(toAdd):
            sqlcursor.execute(f'SELECT * FROM {table} LIMIT 1');sqlcursor.fetchone();#To Not get "Unread Result found" error.
            for items,data in enumerate(sqlcursor.description):
                field=data[0]
                fieldToAdd=input(f'Enter the value for {field}\n|| => ')
                tempList.append(fieldToAdd)
            fieldList.append(tuple(tempList))
        replyOptions=["y","ye","yes",'sure',"no","n"];positiveReply=["y","ye","yes",'sure']
        confirm=input("Do you want to save the changes? (y/n)").lower()
        while confirm:
            if confirm not in positiveReply and confirm in replyOptions:
                return print('Process was cancelled successfully! Exiting to main menu....');sqlcursor.close()
            elif confirm in positiveReply:
                print("Saving it, Please wait......")
                item=inserts(sqlcursor.description)
                try:
                    if len(fieldList) != 1:
                        sqlcursor.executemany(f"INSERT INTO {table} {item} VALUES {fieldList}")
                    else:
                        sqlcursor.execute(f"INSERT INTO {table} {item} VALUES {fieldList[0]}")
                    time.sleep(0.5)
                    db.commit()
                    time.sleep(0.2)
                    print(f"{sqlcursor.rowcount} rows were inserted successfully!")
                except:
                    print("Looks like an error occured. Please check your value's data and try again")
                finally:
                    return sqlcursor.close();print('Returning to main menu.....')
    # Gonna Add More Functions. 