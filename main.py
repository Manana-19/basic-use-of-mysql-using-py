print("Importing Modules")

import json
# Getting json to load user's data for sql's connection
from user import option, settings
# Importing modules from user.py
import mysql.connector
# Importing MySQL's Connector

print("Module Imported successfully! Connecting Database...")
file=open("config.json","r")
config=json.load(file);file.close()
#Loading JSON for login details and closing file to avoid file open error if anyone tries to delete it while it's running 
database_connection = mysql.connector.connect(
    host=config['host'],
    user=config['user'],
    password=config['password'],
    database=config['db']
)
print('Connection has been successfully established to database.')

table=config['table']
# For using some default table instead of messing up. I'll make this customizable through user input later on with database too....
ex=input("Do you want to proceed? (y/n)\n").lower()
# Not your actual ex 🗿
replyOptions=["y","ye","yes",'sure',"no","n"];positiveReply=["y","ye","yes",'sure']
while ex:
    if ex not in positiveReply and ex in replyOptions:
        print('Closing the Program\nThanks for using it.')
        exit()
    elif ex in positiveReply:
        optionList=["s","view","show",'v'];settingsList=["setting","settings","sets","set",'s']
        askInput=input("What do you want to do in your database?\n- view => You can view records, tables, databases and users available in the server.\n- settings => You can use settings of your database or insert new records through this option.\n\n >>>").lower()
        if askInput in optionList:
            option(database_connection,table)
            ex=input("Do you want to proceed? (y/n)\n").lower()
        if askInput in settingsList:
            settings(database_connection,table)
            ex=input("Do you want to proceed? (y/n)\n").lower()
    else:
        print('Invalid option found, please try again.')
        ex=input("Do you want to proceed? (y/n)\n").lower()
# Changes to add in future:
# - Error Handling (with logins, random input that db won't allow and other stuff), - Choose Database and table options, - Work a bit more on User Management stuff