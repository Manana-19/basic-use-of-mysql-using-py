print("Importing Modules")

from view import view
from edit import edit
# Importing internal modules

import mysql.connector
from dotenv import dotenv_values
# Importing external modules

print("Module Imported successfully! Connecting Database...")

config=dotenv_values(".env")
#Loading .env for login details
database_connection = mysql.connector.connect(
    host=config['host'],
    user=config['user'],
    password=config['password'],
    database=config['db']
)

print('Connection has been successfully established to database.')

ex=input("Do you want to proceed? (y/n)\n==> ").lower()
# Not your actual ex 🗿
replyOptions=["y","ye","yes",'sure',"no","n"]

while ex:
    if ex in replyOptions[4:]:

        print('Closing the Program\nThanks for using it.')
        exit()
        
    elif ex in replyOptions[0:4]:

        optionList=["s","view","show",'v'];
        settingsList=["setting","settings","sets","set",'edit','e'];
        askInput=input("What do you want to do in your database?\n- view => You can view records, tables, databases and users available in the server.\n- edit => You can edit, delete, or insert records through this option.\n\n ==>").lower()
        
        if askInput in optionList:
        
            view(database_connection)
            ex=input("Do you want to proceed? (y/n)\n==> ").lower()
        
        if askInput in settingsList:
        
            edit(database_connection)
            ex=input("Do you want to proceed? (y/n)\n==> ").lower()
    
    else:
    
        print('Invalid option found, please try again.')
        ex=input("Do you want to proceed? (y/n)\n==> ").lower()