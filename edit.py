from modules import inserts, selectTable, selectField
import time

def edit(db):
    
    sqlcursor=db.cursor();
    ask=input("What would you like to go through in settings of the database?\n\n\n- insert => Inserts amount of records you want to register in the database.\n- delete => Deletes the registered Data in the table (specific/all).\n- edit => edits the existing data (specified only)\n\n\n==> ").lower();
    insertDataList=['add','insert','inserts','i'];
    deleteDataList=['delete','delete data','delete-data','del','d'];
    editDataList=['edit','edit data','edit-data','e'];
    replyOptions=["y","ye","yes",'sure',"no","n"];
    
    if ask in insertDataList:
        table=selectTable(sqlcursor);
        toAdd=int(input("Please Enter the amount of rows you want to register\n==> "));
    
        while toAdd<1 or toAdd>99:
            print("Please enter a valid value between 1 - 99");
            toAdd=int(input("Please Enter the amount of rows you want to register\n==> "));
    
        fieldList=[];#  List to store "To Insert"'s data in tuple
        tempList=[]; #  "To Store Data" in List form which will be converted into tuple then inserted into fieldList
        sqlcursor.execute(f'SELECT * FROM {table} LIMIT 1');
        sqlcursor.fetchone();#  To Not get "Unread Result found" error.
        
        for x in range(toAdd):
            
            for item,data in enumerate(sqlcursor.description):
                field=data[0];
                fieldToAdd=input(f'{item+1}. Enter the value for {field}\n==> ');
                tempList.append(fieldToAdd);
        
            fieldList.append(tuple(tempList));
            tempList.clear()
        
        toInsertString=''
        
        for i in fieldList:
        
            if i != fieldList[-1]:
                toInsertString+=f"{i}, "
        
            else: toInsertString+=f"{i}"
        
        del tempList
        
        confirm=input("Do you want to save the changes? (y/n)\n==> ").lower();
        
        while confirm:
            
            if confirm in replyOptions[4:]:
                print('Process was cancelled successfully! Exiting to main menu....');
                sqlcursor.close();
                return
        
            elif confirm in replyOptions[0:4]:
                print("Saving it, Please wait......");
                item=inserts(sqlcursor.description);
                    
                try:
    
                    if len(fieldList) != 1:
                        sqlcursor.execute(f"INSERT INTO {table} {item} VALUES {toInsertString}")

                    else:
                        sqlcursor.execute(f"INSERT INTO {table} {item} VALUES {fieldList[0]}")

                    time.sleep(0.5)
                    db.commit()
                    time.sleep(0.2)
                    print(f"{sqlcursor.rowcount} rows were inserted successfully!")
    
                except:
                    print("Looks like an error occured. Please check your value's data and try again");
            
                finally:
                    sqlcursor.close();
                    print('Returning to main menu.....');
                    return
                
            else:
                confirm=input('Invalid Option...\nDo you want to save the changes? (y/n)\n==>')
    
    elif ask in editDataList:

        table=selectTable(sqlcursor);
        sqlcursor.execute(f'SELECT * FROM {table};')
        field=selectField(sqlcursor);
        newData=input(f'Enter the new data you want to insert in the existing field "{field}". \n==>');
        print("Now you have to select the field for the condition and input the field's value");
        ConditionField=selectField(sqlcursor);
        ConditionValue=input('Enter the value of the Condition Field.');
        confirm=input('Do you want to save the changes? (y/n)\n==>').lower();
            
        while confirm:

            if confirm in replyOptions[4:]:
                print('Process was cancelled successfully! Returning to main menu');
                sqlcursor.close();
                return
                
            elif confirm in replyOptions[0:4]:
                    
                try:
                    sqlcursor.execute(f'UPDATE {table} SET {field}={newData} WHERE {ConditionField}={ConditionValue};')
                    time.sleep(0.2)
                    db.commit()
                    print(f'{sqlcursor.rowcount} row(s) were edited successfully!')

                except:
                    print('Looks like something went wrong, Please try again and make sure that the data type you want to edit is acceptable from the data field');
                    # Will try to work on this error thing so that users can avoid this and in such a manner that SQL/MySQL doesn't give us the error in future.
                
                finally:
                    print('Returning to main menu...');
                    sqlcursor.close();
                    return 
            else:
                confirm=input('Invalid Option...\nDo you want to save the changes? (y/n)\n==>')

    elif ask in deleteDataList:
        
        table=selectTable(sqlcursor);
        sqlcursor.execute(f'SELECT * FROM {table};');
        print("Now you have to select the field for the condition and input the field's value");
        ConditionField=selectField(sqlcursor);
        ConditionValue=input('Enter the value of the Condition Field.\n==> ');
        confirm=input("Do you want to save the changes? (y/n)\n==>").lower();

        while confirm:

            if confirm in replyOptions[4:]:
            
                print('Process was cancelled successfully! Returning to main menu');
                sqlcursor.close();
                return
            
            elif confirm in replyOptions[0:4]:

                try: 
                    sqlcursor.execute(f"DELETE FROM {table} WHERE {ConditionField}={ConditionValue};")
                    time.sleep(0.2)
                    db.commit()
                    print(f"{sqlcursor.rowcount} row(s) were deleted successfully");

                except:
                    print('Some error occurred, Please try again later.....');

                finally:
                    print('Returning to Main Menu....');
                    sqlcursor.close();
                    return
            
            else:
                confirm=input('Invalid Option...\nDo you want to save the changes? (y/n)\n==>')

    else:
        print('Invalid Option found, Please try again.');
        return