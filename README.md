# 291MiniProject
CMPUT 291 Mini Project

## nurses.sql, doctors.sql, staff.sql
These files are designed to make the prototypes of the queries that will be used in the program.
They can be read into an sqlite3 instance to check the output during development. They will not be the complete solution for any part because they will not have the dynamic data that will be used in the python script.

#### To test for example the doctors requirement 2:

obs_date will be set to a fake value in the and clause so that the query will complete correctly but in the python version it will be a variable.

## Data.sql
This is the data that will be used to test against. Someone needs to make fake insert statements for each of the tables that are outlined in the hospital.sql file.


## hospital.py

This is the main program. It should be mostly filled with the flow of the program. Other files will be imported so that we can test in smaller components.

For example the build_database.py will be included and then called upon the the database needs to be initialized.
