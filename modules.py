# Storing all other modules here.
def inserts(sqldescription):
    stringToReturn='('
    for x in sqldescription:
        if x[0] == sqldescription[-1][0]:
            stringToReturn+=f"{x[0]})"
        else:
            stringToReturn+=f"{x[0]}, "
    return stringToReturn;#Hell yea, I don't have to take headache for creating tuples and go through tons of string manipulations