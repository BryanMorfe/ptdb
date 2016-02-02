# PTDB
***PTDB--Plain Text Database-- Is a flat file database system written in python. When simplicity and functionality are required, use PTDB.***

**NOTE: PTDB is compatible with python 2 and 3.**

## How To Guide

### Index:
* [Creating a PTDB Database](https://github.com/BryanMorfe/ptdb/blob/master/README.md#creating-a-ptdb-database)
  * [Manually](https://github.com/BryanMorfe/ptdb/blob/master/README.md#manually)
  * [Using Python](https://github.com/BryanMorfe/ptdb/blob/master/README.md#through-python)
* [Reading a PTDB Databasa](https://github.com/BryanMorfe/ptdb/blob/master/README.md#reading-a-ptdb-database)
* [Writing to a PTDB Database](https://github.com/BryanMorfe/ptdb/blob/master/README.md#writing-to-a-ptdb-database)
* [Installing PTDB](https://github.com/BryanMorfe/ptdb/blob/master/README.md#installation)

#### Creating a PTDB Database
##### There are two ways to create a PTDB database; 
1. Manually
2. Through Python

###### Manually:

To create a PTDB Database manually, all we need to do is create a new plain text file, example: `'database'`
After that, we need to give it a specific format for the PTDB parser to do its job properly:
* The titles of each column may or *may not* have an attribute, if it does, it's indicated between square brackets; `[Attribute]`
* Then comes the name of the title, which can contain any characters, except for parentheses or brackets; `[, ], (, )`
* Then comes the type, which is indicated by parentheses. These may be ommited if the type is string; `(INT)`
* Each other title is separated by a *tab*; `Username Score(FLOAT)`
* If done with titles, a ***new line*** is required for each row of values to be entered.
* The values all go below their respective row (In tab spaces), each separated by a *tab key*;
```
Name  Lastname  Email [NULL]Phone
Blake Jefferson bj@h.com  0000000
Donie Peterson dp@h.com  0000000
Ralph Donaldson rd@h.com  0000000
```
**NOTE: IF IT APPEARS TO BE SPACES SEPARATING TITLES AND VALUE, A TABULATION IS NEEDED FOR PROPER PARSING. IT SOME CASES IT MAY NOT LOOK ALIGNED, BUT AS LONG AS EACH VALUE IS UNDER THEIR TITLE (IN TAB SPACES), IT WILL WORK FINE.**

###### Through Python:

The best way to ensure that your database is properly created is to do it using the code itself.
The first thing to always do is importing PTDB (After installing it of course);
```python
import ptdb
# To import everything just use 'from ptdb import *' and you won't have to use the ptdb prefix.
```
After that, we use a couple of the built-in methods in the database object to create our PTDB database;
```python
myDB = ptdb.createDatabase('database') #Creates a new PTDB database named 'database'.
myDB.addTitle('Name') #Creates a new Column with the title 'Name', type 'STRING', and attribute 'NONE'.
myDB.addTitles(['Lastname', 'Email', 'Phone'], ['string', 'string', 'string'], ['none', 'none', 'null'])
myDB.newEntry(['name', 'lastname', 'email', 'phone'], ['Blake', 'Jefferson', 'bj@h.com', '0000000'])
```
The end result would be:
```
Name  Lastname  Email [NULL]Phone
Blake Jefferson bj@h.com  0000000
```
Explaning the functions a little bit;
```python
def createDatabase(name)
```
This method simply returns an empty database object, with the name provided. *Note: It will not create the file until something has been added to it.*
```python
def addTitle(title, type = 'STRING', attr = 'NONE')
```
This method adds a new column with its title to the database. The type and attr parameters are not needed unless they're different from the default. *Note: Each time this function is executed, a file representing the database is created or saved, depending on whether it exists or not.*
```python
def addTitles(titles, types, attrs)
```
This is much like the previews method, but accepting multiple titles to be create. In this case, all parameters are obligatory and **must** be specified as a list of titles, types, and attributes following the same order.
```python
def newEntry(titles, entries)
```
This method is to add a new entry to the database. As the previews function, the parameters **must** be passed as lists. All titles that do not have an attribute of 'NULL' or 'AI' (Auto Increment), must be included in the list, as their values.

#### Reading a PTDB Database
Reading a PTDB database is the most simple thing to do, whether you want to read a file or a string.
```python
from ptdb import parse # Most important thing to do is to import ptdb, remember that.

def greetPerson(email)
  # This function will greet a person if they're on out ptdb database.
  # Variables we will use
  name = ''
  # Time to work with ptdb
  myDB = parse('database') # Will parse a file named 'database' (which we created before)
  
  if myDB.isItemInColumn('email', email):
    name = myDB.getColumnItem('name', myDB.getRowIndex('email', email))
    print("Hello {0}!".format(name))
  else:
    print("Email not in database.")
    
greetPerson('bj@h.com') # Prints 'Hello Blake!'
```
Brief idea of what those PTDB methods are doing:
```python
def isItemInColumn(col, item)
```
This boolean method simply returns true or false where an specified item exists in a specified columns.
```python
def parse(file)
```
This methos simply parses the file and returns a Database object with all the data in it.
```python
def getColumnItem(col, index)
```
This method returns the value of the specified column for an specified index.
```python
def getRowIndex(col, item)
```
This method returns the index of the row where the specified column has a value of the specified item.
#### Writing to a PTDB Database
We already know a little bit about writing to a database from the [Creating a PTDB Database] Chapter, this will simply illustrate a little better the methods used specifically for writing.
```python
def modifyEntry(col, index, newEntry)
```
This method replaces a column's value at a specified index with a new entry. This functions saves the database after it's done.
```python
def removeEntry(index)
```
This method will remove an **entire** entry on a specified row (index).

**NOTE: A FULL [DOCUMENTATION](https://github.com/BryanMorfe/ptdb/blob/master/DOCUMENTATION.md) FOR ALL THE FUNCTIONALITY OF PTDB IS AVAILABLE.**
#### Installation:
##### For Windows Users:
* [Download](https://github.com/BryanMorfe/ptdb/releases/) the lastest PTDB version available in the 'zip' format.
* Extract the archive.
* Open the Command Prompt as an administrator (cmd.exe).
* Navigate to the resulting folder of the archive (where the .py files are) in the cmd. Example: If the folder is called PTDB and it's on the desktop, you write the command `cd c:\users\youruser\desktop\ptdb`, assuming the drive where windows is installed is 'C:\' and replacing 'youruser' for your current windows user.
* Run the command `python setup.py install` and it should install.

##### For Linux:
* [Download](https://github.com/BryanMorfe/ptdb/releases/) the lastest PTDB version available in the 'tar.gz' format.
* Extract the archive.
* Open the Terminal Window.
* Navigate to the resulting folder of the archive (where the .py files are), using the 'cd' command.
* To install for Python 3, run the command `python3 setup.py install`.
* To install for Python 2, run the command `python setup.py install`.

Feel free to contact me at anytime if you have any questions or to report anything about the software.
