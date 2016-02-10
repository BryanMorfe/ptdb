# PTDB DOCUMENTATION

Note: This document is almost always kept up to date with the current version of PTDB.

**Current Version: 1.1**

### PTDB DOCUMENTATION

## Index
* 1. [License](https://github.com/BryanMorfe/ptdb/blob/master/DOCUMENTATION.md#license)
* 2. [How is the Data Parsed](https://github.com/BryanMorfe/ptdb/blob/master/DOCUMENTATION.md#how-is-the-data-parsed)
  * 2.1. [Columns](https://github.com/BryanMorfe/ptdb/blob/master/DOCUMENTATION.md#columns)
  * 2.2. [Items](https://github.com/BryanMorfe/ptdb/blob/master/DOCUMENTATION.md#items)
* 3. [Global Functions](https://github.com/BryanMorfe/ptdb/blob/master/DOCUMENTATION.md#global-functions)
* 4. [A little about the Ptdb Object](https://github.com/BryanMorfe/ptdb/blob/master/DOCUMENTATION.md#a-little-about-the-ptdb-object)
* 5. [The Database Object](https://github.com/BryanMorfe/ptdb/blob/master/DOCUMENTATION.md#the-database-object)
  * 5.1. [Properties](https://github.com/BryanMorfe/ptdb/blob/master/DOCUMENTATION.md#properties)
  * 5.2. [Methods](https://github.com/BryanMorfe/ptdb/blob/master/DOCUMENTATION.md#methods)
* 6. [Understanding Columns](https://github.com/BryanMorfe/ptdb/blob/master/DOCUMENTATION.md#understanding-columns)
  * 6.1. [Attributes](https://github.com/BryanMorfe/ptdb/blob/master/DOCUMENTATION.md#attributes)
  * 6.2. [Types](https://github.com/BryanMorfe/ptdb/blob/master/DOCUMENTATION.md#types)
* 7. [PTDB Examples And Explanations](https://github.com/BryanMorfe/ptdb/blob/master/DOCUMENTATION.md#ptdb-examples-and-explanations)
 * 7.1. [Creating Our Database](https://github.com/BryanMorfe/ptdb/blob/master/DOCUMENTATION.md#creating-our-database)
 * 7.2. [Creating a Simple Login Validator](https://github.com/BryanMorfe/ptdb/blob/master/DOCUMENTATION.md#creating-a-simple-login-validator)
 * 7.3. [Modifying the Database Data](https://github.com/BryanMorfe/ptdb/blob/master/DOCUMENTATION.md#modifying-the-database-data)
* 8. [Credits](https://github.com/BryanMorfe/ptdb/blob/master/DOCUMENTATION.md#credits)

### License
The MIT License (MIT)

Copyright (c) 2016 Bryan Morfe

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

### How is the Data Parsed
Welcome! This is an overview of how the data is parsed into the object.

This is important to know because if you don't know how the code formats the data it will be hard to manipulate and know what's going on.

#### Columns
The columns are fairly simple. 

They can have an attribute; these attributes are stored as strings, when present; Example: `AI`, `DATE`. If the column has no attributes, the attribute is `None`.

They have a title or name, stores as a string; Example: `Name`, `Password`.

They *must* have a type; these are always present. They vary from Int, Float, String, Bool, or Array, and are stored as strings; Example: `INT`, `STRING`, `[FLOAT]`.

#### Items
On the other hand, the items of the column can take many different format that depends on the type of the column.

If a column's type is `INT`, all the items will be formated as such, and should be address as an int rather than a string or float.
If a column has an attribute of `NULL` it is allowed to have NO value. These items are address as `None` in the code.

A column with the type `'STRING'` and an item with the value of 25, should be addressed as `'25'`, if the type of that column was `'INT'`, the item should be addressed as `25`. In the same way, a `'FLOAT'` should be addressed as `25.0`.

Bools: In the file, bools are stores with 1's and 0's, representing True and False respectfully. These items in the code are address in the python way; `True` or `False`.

Arrays: These files are separated by a comma (,) in the file, but in the code they are addressed as lists. Examples; An array of ints, `'[INT]'` should be addressed in this format `[5, 6, 7]`, an array of strings, `'[STRING]'` would be `['5', '6', 'seven']`.

###### Note: To learn fully about the column's attributes and types, [click here](https://github.com/BryanMorfe/ptdb/blob/master/DOCUMENTATION.md#understanding-columns).

### Global Functions
There are three main global functions that will help you work with PTDB.

```python
def parseString(string)
```
The above function takes a string as a parameter, and parses it to a [Database Object](https://github.com/BryanMorfe/ptdb/blob/master/DOCUMENTATION.md#the-database-object).

```python
def parse(file)
```
Much like the last function, except that this one parses a file instead of a string. It also returns a Database Object, with the exception that the name of the file is also added into the properties of the object (the filename can be modified with the method `set_file_to(name)`).

```python
def createDatabase(name=None)
```
This function creates an empty Database Object and returns it to be manipulated later. The parameter `name`, optional, sets the filename.

### A little about the Ptdb Object
The Ptdb Object simply stores a column with its items in its properties.

```python
class Ptdb
```
The properties hold the title, attribute, type and a list of the items of each column.
**This object is for internal use of the module only.**

### The Database Object
The Database Object basically handles all of the functionality of the PTDB parser, along with holding all the data.
```python
class Database
```
#### Properties
The properties of this object most likely won't be modified by the user (you), but it is useful to know them, and know how it all works together.
```python
database = []
file = ''
```
The `database` property holds a list of all the columns in the database (A list of Ptdb Objects). This is **not** to be modified, since all the methods below will do it in a more semantically correct way.

The `file` property simply holds the name of the file containing all the data, or simply a filename to be set to a new file. This property should **not** be modified, instead, you use the method `set_file_to(name)`.

#### Methods
There are quite a few methods in the Database Object. After reading this section you will be familiar with PTDB and will be able to do anything you want with it.


##### Method Declaration:
```python
def amountOfColumns()
```
Returns an int with the amount of columns in the database.


##### Method Declaration:
```python
def set_file_to(name)
```
Sets or changes the filename of the database.

**Parameters**
```
name: String
    Filename to be set or changed to.
```
**Returns**
```
return: Int
    Amount of columns.
```


##### Method Declaration:
```python
def isItemInColumn(col, item)
```
Returns True or False if a specified item is in the specified column.

**Parameters**
```
col: String
    Name of the column.
item: String, Int, Float or Bool
    item of the row.
```
**Returns**
```
return: Bool
    If the item is found, True, if not, False.
```
**Notes**

This method is NOT case sensitive. When looking for a column 'Name' with a value of 'John', passing ('id', 'john') will find it just fine, if it exists.


##### Method Declaration:
```python
def getItemsInColumn(col)
```
Returns all the items for a specified column.

**Parameters**
```
col: String
    Name of the column.
```
**Returns**
```
return: List
    List of items.
```
**Notes**

This method is NOT case sensitive. Looking for ('id') is the same as looking for ('ID').

This method, however, returns the items just as written in the Database File; If Name has the values John and Casper, it will return ['John', 'Casper'], not ['john', 'casper'].


##### Method Declaration:
```python
def getColumnType(col)
```
Returns the type of a specified column or an empty string.

**Parameters**
```
col: String
    Name of the column.
```
**Returns**
```
return: String
    Type of the column.
```
**Notes**

This method is NOT case sensitive, looking for ('id') is the same as ('ID').

This method, however, returns the Type just as written in the Database File; If it is [AI]Id(INT), it will return 'INT', not 'int'.


##### Method Declaration:
```python
def getColumnAttribute(col)
```
Returns the attribute of a column or an empty string.

**Parameters**
```
col: String
    Name of the column.
```
**Returns**
```
return: String
    Attribute of the column.
```
**Notes**

This method is NOT case sensitive. Looking for ('Name'), will produce the same result as looking for ('name').

This method, however, returns the Attribute just as written in the Database File; If it is [AI]Id(INT), it will return 'AI', not 'ai'.


##### Method Declaration:
```python
def columnHasAttribute(col, attr)
```
Returns True or False if a column has an attribute or not.

**Parameters**
```
col: String
    Name of the column.
attr: String
    Attribute to find
```
**Returns**
```
return: Bool
    True if the column has the attribute, otherwise False.
```
**Notes**

This method is NOT case sensitive. Looking for ('id', 'ai') will produce the same result as ('ID', 'AI')


##### Method Declaration:
```python
def getRowIndex(col, item)
```
Returns the index (int) of a specified column item.

**Parameters**
```
col: String
    Name of the column.
item: Int, Float, String or Bool
    Item in the column.
```
**Returns**
```
return: Int
    Index of the row to which the item belongs to.
```
**Notes**

This method is NOT case sensitive. Looking for ('Name', 'John') will produce the same result as ('name', 'john').


##### Method Declaration:
```python
def getColumnItem(col, index)
```
This method returns the item in a column `col`, in a specified `index`.

**Parameters**
```
col: String
    Name of the column.
index: Int
    Index for the row.
```
**Returns**
```
return: Int, Float, String, Bool or List
    Item of the column.
```
**Notes**

This method is NOT case sensitive. Looking for ('password', 5), will produce the same result as looking for ('Password', 5)

This method, however, returns the Item just as written in the Database File; If the Password for index 5 is P@5sW0rD, it will return 'P@5sW0rD' instead of 'p@5sw0rd'. This is useful specially in these cases where you have to look for information like passwords or case sensitive codes.


##### Method Declaration:
```python
def getDataForIndex(index)
```
Returns the value of all the columns in a specified row.

**Parameters**
```
index: Int
    Index for the row.
```
**Returns**
```
return: List
    List of values.
```


##### Method Declaration:
```python
def modifyEntry(col, index, new_entry)
```
Modifies a column in a specified row.

**Parameters**
```
col: String
    Name of the column.
index: Int
    Index for the row.
new_entry: Int, Float, String, Bool or List
    New replacement value.
```
**Returns**
```
return: Bool
    If modified successfully, True, if not, False.
```
**Notes**

This method is NOT case sensitive when LOOKING for a column. Looking for ('name', 5, 'new_name') will produce the same result as ('NAME', 5, 'new_name'). However, the 'new_entry' parameter IS case sensitive. Passing 'John', will replace the current column's value with 'John', not 'john' or 'JOHN'.


##### Method Declaration:
```python
def newEntry(titles, entries)
```
Adds a new row to the database.

**Parameters**
```
titles: List
    Names of the columns.
entries: List
    Value of each column.
```
**Returns**
```
return: Bool
    True if successful, otherwise False.
```

**Validation**

For a new entry to be valid, it needs to meet the following five conditions:
* It must have as many entries as it has titles.
* All passed titles MUST be in the database
* A column with the attributes; AI and DATE cannot be passed.
* A column with the attribute 'DEFAULT' MUST have a default value.
* A column with the no attribute 'None' MUST be passed.
            
**Notes**

This method is NOT case sensitive when LOOKING for the titles. Looking for ['Name', 'Lastname'] will produce the same result as ['name', 'lastname']. However, everything you pass in the list of entries, will be saved to the database as is, ['John', 'Appleseed'] is DIFFERENT than ['john', 'appleseed'].


##### Method Declaration:
```python
def removeEntry(index)
```
Removes **permanently** a specified row in the database.

**Parameters**
```
index: Int
    Index for the row.
```


##### Method Declaration:
```python
def addTitle(title, type_='STRING', attr=None)
```
Adds a new column, if possible.

**Parameters**
```
title: String
    Name of the column.
type_: String, Optional
    Type of the column.
attr: String, Optional
    Attribute of the column.
```
**Returns**
```
return: Bool
    If the new column is added successfully, True, otherwise, False.
```


##### Method Declaration:
```python
def addTitles(titles, types, attrs)
```
This method adds multiple columns to the database.

**Parameters**
```
titles: List
    Names of the columns.
types: List
    Type of each column.
attrs: List
    Attribute of each column.
```
**Returns**
```
return: Bool
    True if successful, otherwise False.
```


##### Method Declaration:
```python
def saveDatabase()
```
Saves all the content in the object to a file with the object's file name.

**Notes**

Before calling this method, we need to make sure that our filename is set. Because of that, when parsing a string, or creating a new Database Object, is *necessary* to set the filename with the method `set_file_to(name)`.

###### Those are all the methods in the Database Object. For examples on how to use them, go to the [PTDB Examples And Explanations](https://github.com/BryanMorfe/ptdb/blob/master/DOCUMENTATION.md#ptdb-examples-and-explanations) section.

### Understanding Columns

#### Attributes
A column attribute--those wrapped between square braquets--give a special meaning to a column. If you want to find out a little more keep reading.

As of **now**, four attributes can define a PTDB column;
* AI
* NULL
* DATE
* DEFAULT=value

AI: Means **Auto Increment**, and much like the Auto Increment from *MySQL*, it means that each new entry that you add will be incremented by one. It is important to add that a column with the attribute of `AI`, should **always** have a type of `INT`; Example: `[AI]ID(INT)`, or the Database is doomed to fail at any point.
**Note: Trying to add a custom value to a column with an attribute of `AI` will cause the specific method to return `False` and not work.**

NULL: This attribute is very simple. All it means to the column is that it is **allowed** to have no value.
**Note: When adding a new entry to the database, a column attribute of `NULL` is *not* necessary.**

DATE: This is almost self-explanatory. A column with this attribute will add the date in which the entry was created (if created through the code).
**Note: A column with this attribute is unmodifiable. Trying to do so will result in an error.**

DEFAULT: This attribute basically adds a default value to a column which value is not specified.
It works as follows: `[DEFAULT=value]column_name(TYPE)` means that `column_name` has a *default* value of `value`, and the code *casts* the value to the column's type `TYPE`. If the value is specified when adding a new entry, the default value is *ommited*.

#### Types
Types simply define the value type in a column.

There are a couple of types supported by PTDB:
* INT
* FLOAT
* STRING
* BOOL
* ARRAY OF TYPE

INT: Is a number with no decimal points. Casted to a Python int object.

FLOAT: A number with a floating point or decimals. Casted to a python float object.

STRING: An array of characters. Casted to a python str object.

BOOL: A binary True or False value. Casted to a python bool object.

ARRAY OF TYPE: Makes a list of any type; Ints, floats, strings or bools; It is defined as `([TYPE])`; Examples: `([INT])`, `([STRING])` or the array of strings shorthand `([])`. Casted to a Python list object.

### PTDB Examples And Explanations
Welcome to the examples section. In this section you will see some of the methods in practice and their expanations.

Here are some examples using PTDB and their explanations:

#### Creating Our Database

```python
from ptdb import createDatabase

my_db = createDatabase('mydatabase')  # Creates a new database 'mydatabase' but DOESN'T CREATE A FILE YET.

# I don't like 'mydatabase' for a file name, so I'll change it to 'database' accessing the 'set_file_to' method of the Object.
my_db.set_file_to('database')

# Now let's add some content in there (everytime a method that modifies the data in some way is called, 
# it will save the file (if successful).
my_db.addTitle('ID', type_='INT', attr='AI') # This create a single column called 'ID' with a type of 'INT' and an attribute of 'AI'

my_db.addTitles(
        ['Name', 'Lastname', 'Email', 'Friends_Ids', 'Password', 'Admin'], 
        ['STRING', 'STRING', 'STRING', '[INT]', 'STRING', 'BOOL'], 
        [None, None, None, 'NULL', None, 'DEFAULT=0']
    )  # This method creates all these columns with their respective name, type and attribute

my_db.newEntry(
        ['id', 'name', 'lastname', 'email', 'password'], 
        [0, 'Bryan', 'Morfe', 'bryanmorfe@gmail.com', 'password1']
    )  # This will return False and not create a new entry nor save the file, because the column 'ID' has an attribute of 'AI'

my_db.newEntry(
        ['name', 'lastname', 'email', 'password'], 
        ['Bryan', 'Morfe', 'bryanmorfe@gmail.com', 'password1']
    )  # This method will work. the column 'ID' is letting its attribute 'AI' work its magic, we're not any friends,
       # and since we're also NOT specifying a True or False for 'admin', it will add the default '0' which translates to False.

# Let's add a few more entries
my_db.newEntry(
        ['name', 'lastname', 'email', 'password', 'friends_ids'], 
        ['Gabriella', 'Ashton', 'gabriellaashton@gmail.com', 'password2', [0, 2]]
    )
my_db.newEntry(
        ['name', 'lastname', 'email', 'password', 'friends_ids'], 
        ['Bernie', 'Carter', 'berniecarter@gmail.com', 'password3', [3]]
    )
my_db.newEntry(
        ['name', 'lastname', 'email', 'password', 'admin'], 
        ['Julie', 'Benson', 'juliebenson@gmail.com', 'password4', True]
    )
# Those will add all those entries and save the file each time. Note on the second entry, when adding `Bernie` to the database,
# we only have ONE friend id, but we still have to specify it a list. Also, when adding `Julie`, we specified `Admin` as True.
```

The resulting file `database` should be defined as follows:
```
[AI]ID(INT) Name      Lastname    Email                      (NULL)Friends_Ids([INT])  Password    [DEFAULT=0]Admin(BOOL)
0           Bryan     Morfe       bryanmorfe@gmail.com                                 password1   0 
1           Gabriella Ashton      gabriellaashton@gmail.com  0,2                       password2   0
2           Bernie    Carter      berniecarter@gmail.com     3                         password3   0
3           Julie     Benson      juliebenson@gmail.com                                password4   1
```
**Note: The file will NOT look aligned like that, I manually aligned for presentation purposes.**

The above PTDB database will be used for our following examples.

#### Creating a Simple Login Validator
```python
from ptdb import parse

def login(email, password):
    # Returns true or false whether is logged successfully
 
    # parse the database
    my_db = parse('database')
 
    # Check if email is in database
    if my_db.isItemInColumn('email', email.lower()):
        # If email is in the database, check the password for that entered email.
  
        db_password = my_db.getColumnItem('password', my_db.getRowIndex('email', email.lower()) 
        # This above statement is saying; 'Get the password of the row where the column email is 'email.lower()'
  
        # Now we compare the entered password with the one corresponding to that email, if they're equal, the login is successfully,          # else, it's not
        if password == dbPassword:
            return True
        else:
            return False
    else:
        # If email is not in database then return false.
        return False
  
# Now we test the function login.
if login('bryanmorfe@gmail.com', 'password1'):
    print("User logged successfully.")
else:
    print("Credentials are incorrect.")
# Prints 'User logged successfully'
```
#### Modifying the Database Data

For this example, we will simply modify the password in one of our entries.
```python
from ptdb import parse

def change_password(email, current_password, new_password):
    # This function will return True if we change the password in an entry or false if we couldn't.
 
    # Before anything, we make sure that the current_password and the new_password are different and have a value.
    if current_password == new_password or not current_password or not new_password:
        return False
  
    # Now, we parse our data
    my_db = parse('database')
 
    # Now we check if the email is in the database
    if my_db.isItemInColumn('email', email.lower()):
        # Now we make sure that the currentPassword matches the one for that email
        db_password = my_db.columnItem('password', my_db.getRowIndex('email', email.lower()))
        if db_password == current_password:
            # If it entered here, then we can change the password.
            my_db.modifyEntry('password', my_db.getRowIndex('email', email.lower()), new_password)
            # The above method is saying; Replace the column 'Password' with 'new_password', where the column 'Email', is 'email.lower()' and saves the file
            return True
    else:
        return False

# Gabriella feels like her password is not secure enough, and she asked me to write this code for her.
# She's my friend, so I said of course!

# We first need Gaby's information
gabys_email = 'gabriellaashton@gmail.com'
gabys_password = 'password2'
gabys_new_password = 'P@s5w0rd'

if change_password(gabys_email, gabys_password, gabys_new_password):
    print('Password has been changed successfully.')
else:
    print('There was an error changing your password.')
    
# Prints 'Password has been changed successfully.' and the database is saved.
```

After the execution of the above code, our new file should look like this:

```
[AI]ID(INT) Name      Lastname    Email                      (NULL)Friends_Ids([INT])  Password    [DEFAULT=0]Admin(BOOL)
0           Bryan     Morfe       bryanmorfe@gmail.com                                 password1   0 
1           Gabriella Ashton      gabriellaashton@gmail.com  0,2                       P@s5w0rd    0
2           Bernie    Carter      berniecarter@gmail.com     3                         password3   0
3           Julie     Benson      juliebenson@gmail.com                                password4   1
```

### Credits
PTDB: The idea behind PTDB is mine. It created iniatially for personal usage, but then I thought it could be useful for you developers our there too. Although PTDB, as of **now**, has been programmed solely by me, Bryan Morfe,  I do owe a 'Thank you' to a lot of people out the in the internet who have taught me a lot.
