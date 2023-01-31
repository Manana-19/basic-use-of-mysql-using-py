from modules import selectTable ,selectField ,show

def view(db):
    
    showTableList=['table','tables','t',"show-table","showtable","show table",'st'];
    showRecordList=["show-record","show-records","show record","show records","showrecord","showrecords",'sr','r','record','records'];
    showDatabaseList=["show database","show-database","show databases","show-databases","show-db","show db",'sdb','database','databases','db'];
    showUserList=['show users','show user','show-users','show user','su','user','users','u'];
    
    sqlcursor=db.cursor()
    
    stInput = input("What would you like to view in your database?\n\n- table => fetch all the tables available in database\n- record => queries and gets a specific or every record in database's table\n- database => shows all databases available in the server\n- users => shows all the users who are able to connect the database\n\n\n==>").lower();
    
    if stInput in showTableList:

        print('Fetching Data.... Please wait for a moment.')
        sqlcursor.execute('SHOW TABLES');
        print(show(sqlcursor));
        sqlcursor.close();
        return  

    elif stInput in showRecordList:

        table=selectTable(sqlcursor)
        askIfLoop=input('Do you want to fetch your results with specific condition? (y/n)\n =>').lower()
        loop=True
        allOptions=['y','ye','yes','sure','no','n']
    
        while loop==True:
            
            if askIfLoop in allOptions[4:]:
                
                print("Please wait.... We are fetching data from the database.");
                sqlcursor.execute(f"SELECT * FROM {table} LIMIT 90");
                show(sqlcursor);
                sqlcursor.close();
                loop=False

            elif askIfLoop in allOptions[0:4]:
                
                sqlcursor.execute(f'SELECT * FROM {table} LIMIT 1');
                opt=selectField(sqlcursor)
                valueToAsk=input("Please enter the value by which field you're searching the database\n =>")
                sqlcursor.execute(f"SELECT * FROM {table} WHERE {opt}='{valueToAsk}' LIMIT 90")
                show(sqlcursor)
                sqlcursor.close()
                return

    elif stInput in showDatabaseList:
        
        print('Fetching Database(s), Please Wait...');
        sqlcursor.execute("SHOW DATABASES");
        show(sqlcursor);
        sqlcursor.close();
        return
    
    elif stInput in showUserList:

        print('Fetching Management User data, Please wait......');
        sqlcursor.execute('SELECT User from mysql.user;');
        show(sqlcursor);
        print("End of User's List who can access the database");
        sqlcursor.close();
        return

    else:
        print('Invalid Option found, Please try again.');
        return
# 69th Line