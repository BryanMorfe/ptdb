# PTDB v1.0.0 DOCUMENTATION
This file contains a full reference of the Plain Text Database software.

### PTDB DOCUMENTATION

## Index
* [License](https://github.com/BryanMorfe/ptdb/blob/master/REFERENCE.md#license)
* [Global Functions](https://github.com/BryanMorfe/ptdb/blob/master/REFERENCE.md#global-functions)
* [A little about the Ptdb Object](https://github.com/BryanMorfe/ptdb/blob/master/REFERENCE.md#a-little-about-the-ptdb-object)
* [The Database Object](https://github.com/BryanMorfe/ptdb/blob/master/REFERENCE.md#the-database-object)
  * [Properties](https://github.com/BryanMorfe/ptdb/blob/master/REFERENCE.md#properties)
  * [Methods](https://github.com/BryanMorfe/ptdb/blob/master/REFERENCE.md#methods)
* [Understanding Column's Attributes](https://github.com/BryanMorfe/ptdb/blob/master/REFERENCE.md#understanding-columns-attributes)
* [PTDB Examples And Explanations](https://github.com/BryanMorfe/ptdb/blob/master/REFERENCE.md#ptdb-examples-and-explanations)
* [Credits](https://github.com/BryanMorfe/ptdb/blob/master/REFERENCE.md#credits)

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

### Global Functions
There are three main global functions that will help you work with PTDB.

```python
def parseString(string)
```
The above function takes a string as a parameter, and parses it for PTDB use.
This function returns a new Database Object, which later can be manipulated as needed.

```python
def parse(file)
```
Much like the last function, except that this one parses a file instead of a string. It also returns a Database Object, with the exception that the name of the file is also added into the properties of the object (the filename can be modified).

```python
def createDatabase(name)
```
This function creates an empty Database Object and returns it, to then be manipulated later. The parameter `name` is passed to be set as the filename when the file is saved.

### A little about the Ptdb Object
The Ptdb Object simply stores a column with its items in its properties.

```python
class Ptdb
```
The properties hold the title, attribute, type and a list of the items of each column.

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

The `file` property simply holds the name of the file containing all the data, or simply a filename to be set to a new file. This property should **only** be modified if:
1. A string was parsed, but you want to save a new file.
2. If you want to change the filename of your file currently holding the data.

#### Methods
There are quite a few methods in the Database Object. After reading this section you will be familiar with PTDB and will be able to do anything you want with it.

```python
def amountOfColumns()
```
This is one of the simplest methods. It simply returns an int indication how many columns the database has.

```python
def isItemInColumn(col, item)
```
This method returns a boolean value (true or false), whether it finds the specified `item` in a specified column `col`.

```python
def getItemInColumn(col)
```
This method returns all the **items** in a specified column `col`.

```python
def getColumnType(col)
```
This method returns the type (String, Int, Float...) of a column `col`.

```python
def getColumnAttribute(col)
```
This method returns the attribute (none, ai, null) of a column `col`.

```python
def columnHasAttribute(col, attr)
```
This method returns true or false whether a specified column `col`, has an specified attribute `attr`.

```python
def getRowIndex(col, item)
```
This method returns the index of a row, where a column `col` has a value of `item`.

```python
def getColumnItem(col, index)
```
This method returns the item in a column `col`, in a specified `index`.

```python
def getDataForIndex(index)
```
This method returns all the items or data in a specified `index`.

```python
def modifyEntry(col, index, newEntry)
```
This method replaces a column `col` value in a specified `index` with a new value `newEntry`. This method will save the database if it's finished successfully.

```python
def newEntry(titles, entries)
```
This method adds a new entry with a specified **list** of `entries` to the database in a specified **list** of `titles`. They **MUST** be specified as a list, and values most be in the same position as their respective title. This method will save the database if it's finished successfully.

**Note: All columns *must* be entered in this function, *except* those with an attribute of `AI` (*must* not be added) and `NULL` (may or may not be added). Adding a column with an attribute of `AI` will cause the function to return `False` and not add *anything*.**

```python
def removeEntry(index)
```
This method will delete **permanently** all the data in a specified index. After it's done, it saves the database.

```python
def addTitle(title, type = 'STRING', attr = 'NONE')
```
This method adds a new column with the name title. This method can **only** be called if the database is new and has no data in it. The type and attr parameters can be omitted or should only be specified if the values are different from their default values.

```python
def addTitles(titles, types, attrs)
```
Unlike the last method, all the parameters are **obligatory** when executing this method. They **must** be specified as lists as each place in each list belong to each other respectfully.

```python
def saveDatabase()
```
This method simply saves the database to a file, specified in the `file` property of the object.

Those are all the methods in the Database Object. For examples on how to use them, go to the [PTDB Examples And Explanations](https://github.com/BryanMorfe/ptdb/blob/master/REFERENCE.md#ptdb-examples-and-explanations) section.

#### Understanding Column's Attributes
A column attribute--those wrapped between square braquets--give a special meaning to a column. If you want to find out a little more keep reading.
As of **now**, there only two attributes that mean something to PTDB;
* AI
* NULL

AI: Means **Auto Increment**, and much like the Auto Increment from *MySQL*, it means that each new entry that you add will be incremented by one. It is important to add that a column with the attribute of `AI`, should **always** have a type of `INT`; Example: `[AI]ID(INT)`.
**Note: Trying to add a custom value to a column with an attribute of `AI` will cause the specific method to return `False` and not work.**

NULL: This attribute is very simple. All it means to the column is that it is **allowed** to have no value.
**Note: When adding a new entry to the database, a column attribute of `NULL` is *not* necessary.**

#### PTDB Examples And Explanations

#### Credits
