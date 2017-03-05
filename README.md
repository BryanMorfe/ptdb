# PTDB
***PTDB--Plain Text Database-- Is a flat file database system written in python. When simplicity and functionality are required, use PTDB.***

**Current Version: 2.0**

**NOTE: This README is always up to date with the lastest release, an update is always adviced.**

**NOTE: PTDB 2 IS UNSTABLE AS IT IS STILL IN DEVELOPMENT. A FULL UPDATE IS NOT RECOMMENDED AT THIS TIME.**

**NOTE 2: This README contains super BASIC examples. If you really want to learn and use PTDB with its maximum capabilities, read the [DOCUMENTATION](https://github.com/BryanMorfe/ptdb/blob/master/DOCUMENTATION.md).**

**NOTE 3: PTDB was programmed in python 2.7. However, it was written so it can support python 3 too. There are no guarantees that it will work perfectly for python 3, though.**

## How To Guide

### Index:
* 1. [Creating a PTDB Database](https://github.com/BryanMorfe/ptdb/blob/master/README.md#1-creating-a-ptdb-database)
  * 1.1. [Manually](https://github.com/BryanMorfe/ptdb/blob/master/README.md#11-manually)
  * 1.2. [Using Python](https://github.com/BryanMorfe/ptdb/blob/master/README.md#12-through-python)
* 2. [Reading a PTDB Databasa](https://github.com/BryanMorfe/ptdb/blob/master/README.md#2-reading-a-ptdb-database)
* 3. [Writing to a PTDB Database](https://github.com/BryanMorfe/ptdb/blob/master/README.md#3-writing-to-a-ptdb-database)
* 4. [Installing PTDB](https://github.com/BryanMorfe/ptdb/blob/master/README.md#4-installation)

#### 1. Creating a PTDB Database
##### There are two ways to create a PTDB database; 
1. Manually
2. Through Python

###### 1.1. Manually:

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
**NOTE: EVEN IF IT APPEARS TO BE SPACES SEPARATING TITLES AND VALUE, A TABULATION IS NEEDED FOR PROPER PARSING. IN SOME CASES IT MAY NOT LOOK ALIGNED, BUT AS LONG AS EACH VALUE IS UNDER THEIR TITLE (IN TAB SPACES), IT WILL WORK FINE.**

###### 1.2. Through Python:

The best way to ensure that your database is properly created is to do it using the code itself.
The first thing to always do is importing PTDB (After installing it of course);
```python
import ptdb
# To import everything just use 'from ptdb import *' and you won't have to use the ptdb prefix.
```
After that, we use a couple of the built-in methods in the database object to create our PTDB database;
```python
my_db = ptdb.createDatabase('database') # Creates a new PTDB database named 'database'.
my_db.addTitle('Name')  # Creates a new Column with the title 'Name', type 'STRING', and attribute None.
my_db.addTitles(
        ['Lastname', 'Email', 'Phone'], 
        ['STRING', 'STRING', 'STRING'], 
        [None, None, 'NULL']
    )
my_db.newEntry(['name', 'lastname', 'email', 'phone'], ['Blake', 'Jefferson', 'bj@h.com', '0000000'])
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
This method simply returns an empty database object with the name provided as the file name. *Note: It will not create the file until something is been added to it.*

```python
def addTitle(title, type='STRING', attr=None)
```
This method adds a new column with its title to the database. The type and attr parameters are not needed unless they're different from the default. *Note: Each time this function is executed, if the filename is set, a file representing the database is created or saved, depending on whether it exists or not. To set the file name, use the method `set_file_to(name)`.*

```python
def addTitles(titles, types, attrs)
```
This is much like the previews method, but accepting multiple titles to be create. In this case, all parameters are obligatory and **must** be specified as a list of titles, types, and attributes following the same order.

```python
def newEntry(titles, entries)
```
This method is to add a new entry to the database. As the previews method, the parameters **must** be passed as lists. All titles that do not have one of the following attribute; 'NULL', 'AI' (Auto Increment), 'DATE' or 'DEFAULT', must be included in the list, as their values.

#### 2. Reading a PTDB Database
Reading a PTDB database is the most simple thing to do, whether you want to read a file or a string.

```python
from ptdb import parse # Most important thing to do is to import ptdb, remember that.

def greetPerson(email)
    # This function will greet a person if they're on out ptdb database.
    # Variables we will use
    name = ''
    # Time to work with ptdb
    my_db = parse('database')  # Will parse a file named 'database' (which we created before)
  
    if my_db.isItemInColumn('email', email):
        name = my_db.getColumnItem('name', my_db.getRowIndex('email', email))
        print("Hello {0}!".format(name))
    else:
        print("Email not in database.")
    
greetPerson('bj@h.com') # Prints 'Hello Blake!'
```

Brief idea of what those PTDB methods are doing:
```python
def isItemInColumn(col, item)
```
This bool method simply returns True or False if a specified item exists in a specified column.

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

#### 3. Writing to a PTDB Database
We already know a little bit about writing to a database from the [Creating a PTDB Database] Chapter, this will simply illustrate a little better the methods used specifically for writing.
```python
def modifyEntry(col, index, new_entry)
```
This method replaces a column's value at a specified index with a new entry. This functions saves the database after it's done.

```python
def removeEntry(index)
```
This method will remove an **entire** entry on a specified row (index) and saves the database after it's done.

```python
def set_file_to(name)
```
Changes or sets the filename of the database.

**NOTE: A FULL [DOCUMENTATION](https://github.com/BryanMorfe/ptdb/blob/master/DOCUMENTATION.md) FOR ALL THE FUNCTIONALITY OF PTDB IS AVAILABLE.**

#### 4. Installation:
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
* Run the command `python setup.py install`.

Feel free to contact me at anytime if you have any questions or to report anything about the software.
