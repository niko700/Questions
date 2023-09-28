"""
***ASSUMING REAL PATHS - I took the paths out for the example***

Testing being able to get a list of feature classes inside a geodatabase.

This works in the python window, but for some reason not in script form like this.
What I am typing in is exactly the same.

Here, the output is
[]
['J', ':', '\\', 'G', 'I', 'S', '\\', '_', 'c', 'o', 'o', 'r', 'd', 'i', 'n', 'a', 't', 'o', 'r', 'W', 'I', 'P', '\\', 'V', 'e', 'r', 'a', '\\', 'G', 'd', 'b', 's', '\\', 'T', 'o', 'w', 'n', 's', 'F', 'o', 'r', 'C', 'l', 'i', 'p', 's', '.', 'g', 'd', 'b']

so it seems it's just treating the path as a string
"""

import arcpy
import os
from sys import argv


#------------- SET VARIABLES --------------

#set workspace to database where your clip shapes are
arcpy.env.workspace = r"...path to gdb....."
print(arcpy.env.workspace)

#set workspace as a variable
source_gdb = arcpy.env.workspace
print(source_gdb)

l = []
print(l)

for file in source_gdb:
    l.append(file)

print(l)


