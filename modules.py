def inserts(sql_description) -> str:

    stringToReturn='('
    for x in sql_description:

        if x[0] == sql_description[-1][0]:
            stringToReturn+=f"{x[0]})"
        else:
            stringToReturn+=f"{x[0]}, "

    return stringToReturn
# This function is used to avoid overusage of string manipulation manually by giving the desired tuple in the form of string in output.

def selectTable(sql_cursor) -> str: #type: ignore "to ignore the warning in VS Code"
    
    sql_cursor.execute('SHOW TABLES;');
    e=[];
    toloop=True
    while toloop==True:
        
        for i in sql_cursor.fetchall():
        
            print(f'-> {i[0]}')
            e.append(i[0])
        
        verify=input('Select the table you want to work with.\n==> ')
        
        if verify.lower() in e:
            toloop=False
            del e
            return verify
        
        else:
            print('Invalid Option! Please try again...')
# This Function helps to return the selected table

def show(sql_cursor) -> str:
    
    for output_list in sql_cursor.fetchall():    

        print('----------------------------------------------------------')
        for item,data in enumerate(output_list):
            print(f'{sql_cursor.description[item][0]} -> {data}')
    print('----------------------------------------------------------')

    return 'End of the list (LIMIT -> 90)'
# This Function helps in showing the return values of the SQL Cursor

def selectField(sql_cursor) -> str: #type:ignore "to ignore the warning in VS Code"
    sql_cursor.fetchone(); # To Avoid the unfetched data error
    fieldList=[]
    for fieldName in sql_cursor.description:
        
        print(fieldName[0])
        fieldList.append(fieldName[0].lower())
    
    print('Here are the available fields to choose from.')
    opt=input('Choose the following field from the given table of the database. \n=> ').lower()
    loop=True
    while loop==True:
        
        if opt in fieldList:
            
            del fieldList
            loop=False
            return opt
        
        else: print('Invalid Option! Please Try again...')
# This function helps us in returning the selected field by the user