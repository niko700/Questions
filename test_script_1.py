"""

***ASSUMING REAL PATHS - I took the paths out for the example***

Testing being able to get a list of feature classes inside a geodatabase.

This works in the python window, but for some reason not in script form like this.
What I am typing in is exactly the same.

Here, the output is 'None'

"""

import arcpy

#------------- SET VARIABLES --------------

#set workspace to database where your clip shapes are
arcpy.env.workspace = r"...path to gdb....."
print(arcpy.env.workspace)

#create list of files in the workspace database
l = arcpy.ListFeatureClasses()
print(l)

