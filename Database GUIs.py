
# Python file with GUIs for Database file using dummy variables. 

from easygui import *

box1 = ("Enter Table name to be created: ","Table name")
box2 = ("Enter field names (Enter 0 when done)", "Field names")
box3 = ("Enter field values:", "Record inputs")

fieldNames = []
fieldValues = []
fields = ""

# Enterbox to store table name
tableName = enterbox(box1[0], box1[1])

# loop to store fields of a table
while fields != "0":
    fields = enterbox(box2[0], box2[1])
    if fields != "0":
        fieldNames.append(fields)
    else:
        break

print(fieldNames)


# Multi-Enterbox to store records.
fieldValues = multenterbox(box3[0], box3[1], fieldNames) 

print(fieldValues)

print("Done.")

# run sql with a formatted string using user inputted values

  