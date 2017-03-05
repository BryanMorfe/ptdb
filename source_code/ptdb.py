"""
PTDB Module
-----------
This module parses a text file with a specific format and loads it into a Database Object.

Current Version: 1.1

Objects
-------
'Ptdb': Stores a column of the database.
'Database': Stores all the columns, the filename, and has all the methods for manipulating the database.

Global Functions
----------------
'parse': Parses a text file.
'parseString': Parses a string.
'createDatabase': Creates a new Database Object.

Minor Update 1
--------------
New Features:
    * New type for columns: Bool, Arrays of Ints, Floats, Booleans, and Strings
    * New attributes: DATE, DEFAULT
    * New method for changing or setting the filename in the Database Object.
Other Updates:
    * The attribute 'file' from the Database Object now defaults to None instead of an empty string.
    * If there are NULL columns with no items, it now sets them as None instead of a string 'NONE', that also applies
      for columns with no attributes
    * The code has been cleaned
    * Error Handling for better understanding
    * Bugs fixed
    * Performance Upgrades
Future:
    For PTDB version 2, aside from all the new features it will include, the code will be COMPLETELY cleaned, in the
    sense that it will be written in accordance with the PEP documents. A few changes in the code are to be expected,
    such as:
        * The name of Global Functions, Objects, Methods and Attributes.
        * The way some methods work, like the way arguments are passed; Instead of lists, tuples, etc.
        * The currently called 'file' attribute in the Database Object will be inaccessible, instead,
          it will be set or changed only through its method.
        * The Ptdb Object will be replaced by a Dictionary.

Notes
-----
I try to always keep the documentation on GitHub up to date. If you have any doubts, have a read, I try to make PTDB
as easy as possible.

"""

import time

# Wildcard imports these three functions.
__all__ = ['parse', 'parseString', 'createDatabase']


# Declaration of Objects
class Ptdb:
    """Stores a column, its attribute, type and items

    Parameters
    ----------
    title: String
        Name of the column.

    type_: String
        Type of the column.

    attr: String
        Attribute of the column.

    Other Attributes
    ----------------
    items: String, Int, Float, List or None
        Contains all the items of the column.

    """
    def __init__(self, title, type_, attr):
        self.title = title  # This is the name of the column
        self.type_ = type_  # This is the type of the column--STRING, INT, FLOAT...
        self.attr = attr    # This is the attribute of the column--AI, NULL...
        self.items = []     # This is the list of items of the column


class Database:
    """Contains all the data, attributes and methods to operate the database.

    Parameters
    ----------
    database: List of Ptdb Objects
        Contains a list of columns.
    file: String or None, Optional
        Contains the filename of the database or None.

    ===================    =============================================================
    Method                 What does it do?
    ===================    =============================================================
    amountOfColumns        Returns an int with the amount of columns.
    -------------------    -------------------------------------------------------------
    set_file_to            Changes or sets the filename of the database.
    -------------------    -------------------------------------------------------------
    isItemInColumn         Returns True or False if it finds an item in a column.
    -------------------    -------------------------------------------------------------
    getItemsInColumn       Returns all the items for a column.
    -------------------    -------------------------------------------------------------
    getColumnType          Returns a string with the type of a column.
    -------------------    -------------------------------------------------------------
    getColumnAttribute     Returns a string with the attribute of a column.
    -------------------    -------------------------------------------------------------
    columnHasAttribute     Returns True or False if a column has a specified attribute.
    -------------------    -------------------------------------------------------------
    getRowIndex            Returns an int with the index of a row.
    -------------------    -------------------------------------------------------------
    getColumnItem          Returns an item for a specified column.
    -------------------    -------------------------------------------------------------
    getDataForIndex        Returns all the data in a specified row.
    -------------------    -------------------------------------------------------------
    modifyEntry            Modifies a specific column item.
    -------------------    -------------------------------------------------------------
    newEntry               Creates a new row or new entry in the database.
    -------------------    -------------------------------------------------------------
    removeEntry            Removes a row in the database.
    -------------------    -------------------------------------------------------------
    addTitle               Adds a new column to the database, if possible.
    -------------------    -------------------------------------------------------------
    addTitles              Adds multiple columns to the database, if possible.
    -------------------    -------------------------------------------------------------
    saveDatabase           Saves or updates the database file.
    ===================    =============================================================

    """
    def __init__(self, database, file=None):
        """Initializes the Database Object.

        database: List of Ptdb Objects
            Contains a list of columns
        file: String or None, Optional
            Contains the filename of the database or None
        """
        self.database = database  # List of columns
        self.file = file          # Filename

    def amountOfColumns(self):
        """Returns the amount of columns in the database."""
        return len(self.database)

    def set_file_to(self, name):
        """Sets or changes the filename of the database.

        Parameters
        ----------
        name: String
            The new name of the file

        """
        if name:
            self.file = name

    def isItemInColumn(self, col, item):
        """Returns True or False if a specified item is in the specified column.

        Parameters
        ----------
        col: String
            Name of the column.
        item: String, Int, Float or Bool
            item of the row

        Returns
        -------
        return: Bool
            If the item is found, True, if not, False

        Notes
        -----
        This method is NOT case sensitive. When looking for a column 'Name' with a value of 'John', passing
        ('id', 'john') will find it just fine, if it exists.

        """
        for data in self.database:
            # 'data' represents a column and its information.
            if data.title.lower() == col.lower():
                # This condition it's True if the column name passed is the same one of this data's name (column.title).
                try:
                    # This is the error handler;
                    # When looking for an item that is a string, we want to look for a lower case string.
                    # If it's not a string, you will get either a TypeError or an AttributeError.
                    if item.lower() in map(str.lower, data.items):
                        # If the item matches, we successfully find it.
                        return True
                except (TypeError, AttributeError):
                    # If the item is not a string, then ignore the error.
                    pass

                if item in data.items:
                    # When the above error is ignored, make a general comparison with no 'lower' attribute.
                    return True

        return False  # It will reach this point if it didn't find the item, so we return False.

    def getItemsInColumn(self, col):
        """Returns all the items for a specified column.

        Parameters
        ----------
        col: String
            Name of the column

        Returns
        -------
        return: List
            List of items.

        Notes
        -----
        This method is NOT case sensitive. Looking for ('id') is the same as looking for ('ID').

        This method, however, returns the items just as written in the Database File; If Name has the values John and
        Casper, it will return ['John', 'Casper'], not ['john', 'casper'].

        """

        for data in self.database:
            # data represents a column and its information.
                if data.title.lower() == col.lower():
                    # This condition is True if the column name passed is the one in 'data'.
                    return data.items  # Return all the items for that 'data'.

        return []  # If it didn't find the items, we return an empty List.

    def getColumnType(self, col):
        """Returns the type of a specified column or an empty string.

        Parameters
        ----------
        col: String
            Name of the column

        Return
        ------
        return: String
            Type of the column or empty string

        Notes
        -----
        This method is NOT case sensitive, looking for ('id') is the same as ('ID').

        This method, however, returns the Type just as written in the Database File; If it is [AI]Id(INT),
        it will return 'INT', not 'int'.

        """
        for data in self.database:
            # 'data' contains all the information of a column.
            if data.title.lower() == col.lower():
                # This condition it's true if the column name passed belongs to the column's title.
                return data.type_  # Returns the type of that column.

        return ''  # If it reaches this point, no column was found, return an empty string.

    def getColumnAttribute(self, col):
        """Returns the attribute of a column or an empty string.

        Parameters
        ----------
        col: String
            Name of the column

        Return
        ------
        return: String
            Attribute of the column or empty string

        Notes
        -----
        This method is NOT case sensitive. Looking for ('Name'), will produce the same result as looking for ('name').

        This method, however, returns the Attribute just as written in the Database File; If it is [AI]Id(INT),
        it will return 'AI', not 'ai'.

        """
        for data in self.database:
            # 'data' contains a column and all its information.
            if data.title.lower() == col.lower():
                # If the passed column name matches the one in data (column), the condition is True.
                return data.attr

        return ''  # If the column wasn't found, return an empty string.

    def columnHasAttribute(self, col, attr):
        """Returns True or False if a column has an attribute or not.

        Parameters
        ----------
        col: String
            Name of the column
        attr: String
            Attribute to find

        Return
        ------
        return: Bool
            If it finds the attribute in the column, True, if not, False

        Notes
        -----
        This method is NOT case sensitive. Looking for ('id', 'ai') will produce the same result as ('ID', 'AI')

        """
        for data in self.database:
            # 'data' contains a column and all its information.
            if data.title.lower() == col.lower():
                # Looks for that passed column name in the data.
                return data.attr.lower() == attr.lower()  # Returns True only if the passed attribute is in the column.

        return False  # If the column wasn't found, we reach this point and return False.

    def getRowIndex(self, col, item):
        """Returns the index (int) of a specified column item.

        Parameters
        ----------
        col: String
            Name of the column
        item: Int, Float, String or Bool
            Item in the column

        Return
        ------
        return: Int
            Index of the item in the column

        Notes
        -----
        This method is NOT case sensitive. Looking for ('Name', 'John') will produce the same result
        as ('name', 'john').

        """
        index = 0  # This variable will represent the index of the column

        for data in self.database:
            # 'data' contains all the information of a column
            if data.title.lower() == col.lower():
                # If it's the right column, loop through all the items.
                for data_item in data.items:
                    # If it finds the item, this condition will be True
                    if item == data_item:
                        return index
                    index += 1  # If it doesn't find the item, then we increase the index to move on to the next item.

        return None  # None is the generic value if it doesn't find the item.

    def getColumnItem(self, col, index):
        """Returns an item for a specified column in the specified row.

        Parameters
        ----------
        col: String
            Name of the column
        index: Int, Float, String or Bool
            Item in the column

        Return
        ------
        return: Int, Float, String, Bool or List
            Item of column

        Notes
        -----
        This method is NOT case sensitive. Looking for ('password', 5), will produce the same result as looking for
        ('Password', 5)

        This method, however, returns the Item just as written in the Database File; If the Password for index 5 is
        P@5sW0rD, it will return 'P@5sW0rD' instead of 'p@5sw0rd'. This is useful specially in these cases where
        you have to look for information like passwords or case sensitive codes.

        """
        for data in self.database:
            # 'data' contains all the information of a column
            if data.title.lower() == col.lower():
                return data.items[index]  # Return the column's item at the specified index.

        return None  # If it doesn't find the column, returns None.

    def getDataForIndex(self, index):
        """Returns the value of all the columns in a specified row.

        Parameters
        ----------
        index: Int
            Index of the row

        Return
        ------
        return: List
            List of values

        """
        try:
            data = [self.database[i].items[index] for i in range(len(self.database))]
        except IndexError:
            print 'Error: The index exceeds the number of items in the database.'
        else:
            return data

    def modifyEntry(self, col, index, new_entry):
        """Modifies a column in a specified row.

        Parameters
        ----------
        col: String
            Name of the column
        index: Int
            Index for the row
        new_entry: Int, Float, String, Bool or List
            New replacement value

        Return
        ------
        return: Bool
            If modified successfully, True, if not, False

        Notes
        -----
        This method is NOT case sensitive when LOOKING for a column. Looking for ('name', 5, 'new_name') will produce
        the same result as ('NAME', 5, 'new_name'). However, the 'new_entry' parameter IS case sensitive. Passing
        'John', will replace the current column's value with 'John', not 'john' or 'JOHN'.

        """
        changed_entry = False  # Variable that determines whether the process is done or not.

        for data in self.database:
            # 'data' contains all the information of a column
            if data.title.lower() == col.lower():
                # If the column is found, this condition is True.
                if data.attr is not None and (data.attr.upper() == 'AI' or data.attr.upper() == 'DATE'):
                    # This is a security check to make sure that a column with attributes 'AI' and 'DATE' are NOT
                    # modified.
                    return False  # If they're trying to modify them, return False.

                # This private function '_assign_column_type' assigns the right type to the item, according to the
                # column's type.
                entry = _assign_column_type(new_entry, data.type_)
                data.items[index] = entry  # Replaces the item at the index with the new value
                changed_entry = True  # Let's the method know the change was made successfully.

            if changed_entry:
                # If the value was replaced, the break out of the loop.
                break

        if changed_entry:
            # If the process finished successfully; save the database.
            self.saveDatabase()

        return changed_entry  # Returns if the process was completed or not.

    def newEntry(self, titles, entries):
        """Adds a new row to the database.

        Parameters
        ----------
        titles: List
            Names of the columns
        entries: List
            Value of each column

        Return
        ------
        return: Bool
            True if successful, otherwise False

        Notes
        -----
        This method is NOT case sensitive when LOOKING for the titles. Looking for ['Name', 'Lastname'] will produce
        the same result as ['name', 'lastname']. However, everything you pass in the list of entries, will be saved
        to the database as is, ['John', 'Appleseed'] is DIFFERENT than ['john', 'appleseed'].

        Validation
        ----------
        For a new entry to be valid, it needs to meet the following five conditions:
            * It must have as many entries as it has titles.
            * All passed titles MUST be in the database
            * A column with the attributes; AI and DATE cannot be passed.
            * A column with the attribute 'DEFAULT' MUST have a default value.
            * A column with the no attribute 'None' MUST be passed.

        """
        amount_of_titles = 0  # This stores the amount of titles passed that exist in the database.
        value = ''            # If there's a column with the DEFAULT attribute, this will store the default value.

        if len(titles) != len(entries):
            # This makes sure that the same amount of title and entries were passed.
            return False  # If not, then it's invalid, return False.

        for title in titles:
            # 'title' is ONE title of those passed to the method.
            for data in self.database:
                # 'data' is a column with its information.
                if data.attr is None and data.title.lower() not in map(str.lower, titles):
                    # This conditions is True if an title with no attribute is NOT passed to the method.
                    return False  # Invalid, return False.

                if data.attr is not None and \
                        data.attr.upper().startswith('DEFAULT') and data.title.lower() not in map(str.lower, titles):
                    # This is True if a column has the attribute 'DEFAULT'.
                    value = data.attr[8:]  # Assigns the default value (after the = sign).
                    if not value:
                        # If the 'DEFAULT' attribute has no value, it is invalid.
                        return False

                if title.lower() == data.title.lower():
                    # If the title is in data, this condition is True.
                    amount_of_titles += 1  # Increase the amount of passed titles that are in the database.
                    if data.attr is not None:
                        if data.attr.upper() == 'AI' or data.attr.upper() == 'DATE':
                            # This condition is True if the column passed has an attribute of 'AI' or 'DATE'.
                            return False

        if amount_of_titles != len(titles):
            # If all the titles passed are NOT in the database, this condition is True.
            return False

        i = 0  # This is a counter for the database.
        while i < len(self.database):
            # In this loop, all the new data will be added to the database.
            for j in range(len(titles)):
                # Loops through the titles to add each entry to the corresponding column.
                if titles[j].lower() == self.database[i].title.lower():
                    # This condition is True if the title corresponds to the current column.
                    self.database[i].items.append(entries[j])  # Appends the entry corresponding to the column.

            if self.database[i].attr is not None:
                # It's True only if the column has an attribute
                if self.database[i].attr.upper() == 'NULL' and \
                                self.database[i].title.lower() not in map(str.lower, titles):
                    # If the attribute of the column is NULL, and is not passed, then this condition is True.
                    self.database[i].items.append(None)  # Appends None to the NULL column.
                elif self.database[i].attr.upper() == 'DATE':
                    # This condition is True if the attribute of the column is 'DATE'.
                    self.database[i].items.append(time.strftime("%c"))  # Sets the date and appends it to the column.
                elif self.database[i].attr.upper().startswith('DEFAULT'):
                    # True if the attribute is 'DEFAULT'.
                    value = _assign_column_type(value, self.database[i].type_)  # Assigns the type to the value.
                    self.database[i].items.append(value)  # Appends it to the column.
                elif self.database[i].attr.upper() == 'AI':
                    # True if the attribute is Incremental.
                    if len(self.database[i].items) > 0:
                        # True if the current column has items.
                        self.database[i].items.append(self.database[i].items[-1]+1)  # Appends the ID of the last + 1.
                    else:
                        # If it doesn't have items it enters here.
                        self.database[i].items.append(0)  # Appends 0 to the ID.
            i += 1  # Goes to the next column

        self.saveDatabase()  # Saves the database.

        return True  # If it reaches this point, then the entry was completed successfully.

    def removeEntry(self, index):
        """Removes a specified row in the database.

        Parameters
        ----------
        index: Index
            Index for the row

        """
        for data in self.database:
            data.items.pop(index)  # Removes the item of the column in the specified index

        self.saveDatabase()  # Saves the database

    def addTitle(self, title, type_='STRING', attr=None):
        """Adds a new column, if possible.

        Parameters
        ----------
        title: String
            Name of the column
        type_: String, Optional
            Type of the column
        attr: String, Optional
            Attribute of the column

        Return
        ------
        return: Bool
            If the new column is added successfully, True, otherwise, False

        """
        can_add_title = True  # This variables dictates whether you can add a new title or not. By default you can

        if not title:
            # This condition checks whether you entered an empty name for your column
            return False

        # Loops through the columns
        for data in self.database:
            # Condition that checks if at least one column has items
            if len(data.items) > 0:
                # If entered, then we say that you can't add a new column with one exception; keep reading.
                can_add_title = False

        # The condition says; if we can add a title OR if we can't but the attribute is 'NULL', then let's do it.
        if can_add_title or (not can_add_title and attr is not None and attr.upper() == 'NULL'):
            # If enters then add the new title and save the database
            self.database.append(Ptdb(title, type_, attr))
            self.saveDatabase()
            can_add_title = True

        # Returns true if successfully, false otherwise.
        return can_add_title

    def addTitles(self, titles, types, attrs):
        """This method adds multiple columns to the database.

        Parameters
        ----------
        titles: List
            Names of the columns
        types: List
            Type of each column
        attrs: List
            Attribute of each column

        Return
        ------
        return: Bool
            True if successful, otherwise, False

        """
        i = 0  # This will work as our column index.

        # This condition checks that we have the same amount of title, types and attributes
        if len(titles) != len(types) or len(types) != len(attrs):
            # If entered, then return False and end execution.
            return False
        else:
            # If not, the loop through the list of titles to be added.
            while i < len(titles):
                # This condition will call the function addTitle, and attempt to add the titles one by one.
                if not self.addTitle(titles[i], types[i], attrs[i]):
                    # If entered here, then return False and end execution
                    return False
                i += 1  # Go to the next title

        # If got to this point, then everything went smooth, return True.
        return True

    def saveDatabase(self):
        # Saves all the content in the object to a file with the object's file name.

        if self.file is not None:
            # The file will only be saved if a filename has been set.
            _save_file(self.file, _format_data_for_saving(self.database))
# End of declaration of Objects


# Private global functions are defined next
def _convert_element_to_type(list_, type_):
    new_list = []
    if type_.upper() == 'INT':
        try:
            new_list = [int(item) for item in list_]
        except ValueError:
            print 'Error: One or more items have an invalid type.'
    elif type_.upper() == 'FLOAT':
        try:
            new_list = [float(item) for item in list_]
        except ValueError:
            print 'Error: One or more items have an invalid type.'
    elif type_.upper() == 'STRING':
        new_list = list_
    elif type_.upper() == 'BOOL':
        try:
            new_list = [bool(int(item)) for item in list_]
        except ValueError:
            print 'Error: One or more items have an invalid type.'
    else:
        raise ValueError('Invalid column type.')
    return new_list


def _assign_column_type(item, type_):
    if type_.upper() == 'INT':
        try:
            return int(item)
        except ValueError:
            print 'One or more items have an invalid type.'
    elif type_.upper() == 'FLOAT':
        try:
            return float(item)
        except ValueError:
            print 'One or more items have an invalid type.'
    elif type_.upper() == 'STRING':
        try:
            return str(item)
        except ValueError:
            print 'One or more items have an invalid type.'
    elif type_.upper() == 'BOOL':
        try:
            return bool(int(item))
        except ValueError:
            print 'One or more items have an invalid type.'
    elif type_.upper() == '[INT]':
        list_ = item.split(',')
        list_ = _convert_element_to_type(list_, 'INT')
        return list_
    elif type_.upper() == '[FLOAT]':
        list_ = item.split(',')
        list_ = _convert_element_to_type(list_, 'FLOAT')
        return list_
    elif type_.upper() == '[STRING]' or type_.upper() == '[]':
        list_ = item.split(',')
        return list_
    elif type_.upper() == '[BOOL]':
        list_ = item.split(',')
        list_ = _convert_element_to_type(list_, 'BOOL')
        return list_
    else:
        raise TypeError('The type of the column is invalid.')


def _strip_new_line(string):
    i = 0  # This is used to index a string
    new_string = ''  # This is used to create a copy of the string with the changes made

    # This conditions checks whether the finally ends with '\n' or '\t'
    if string.endswith('\n') or string.endswith('\t'):
        # If it enters, then add all the characters to the newString, except for the last one.
        new_string = string[:-1]

    # Finally, it returns the newString
    return new_string


def _format_data_for_saving(database):
    # Formats a string for PTDB
    new_str = ''
    i = 0
    for data in database:
        if data.attr is not None:
            new_str += '[' + data.attr.upper() + ']'
        new_str += data.title
        if data.type_.upper() != 'STRING':
            new_str += '(' + data.type_.upper() + ')'
        new_str += '\t'
    new_str = _strip_new_line(new_str) + '\n'

    while i < len(database[0].items):
        j = 0
        while j < len(database):
            if database[j].type_.startswith('[') and database[j].items[i] is not None:
                new_str += ','.join(map(str, database[j].items[i]))
                new_str += '\t'
                j += 1
                continue
            try:
                if database[j].items[i] is not None:
                    if database[j].type_.upper() == 'BOOL':
                        if database[j].items[i]:
                            new_str += '1'
                        else:
                            new_str += '0'
                    else:
                        new_str += str(database[j].items[i])
            except IndexError:
                break
            new_str += '\t'
            j += 1
        new_str = _strip_new_line(new_str) + '\n'
        i += 1

    return _strip_new_line(new_str)


def _save_file(file_, string):
    with open(file_, 'w') as db_:
        db_.write(string)
# End of private global functions


# Public Global Functions are defined next
def parseString(string):
    """This function parses a string into a Database Object.

    Parameters
    ----------
    string: String
        Name of the column

    Return
    ------
    return: Database Object
        Database Object containing all the data.

    """
    list_of_lines = string.split('\n')  # Split the file string in files.
    first_line = list_of_lines[0]       # The first line contains the columns.
    database = []                       # This empty list will be filled with the columns data.
    i = 0                               # This is counter will be used through the entire parsing process.

    # This first loop is for getting all the columns, their types and attributes.
    while i < len(first_line):
        # These are some temporary variables for use within the loop
        temp_attr = ''
        temp_title = ''
        temp_type = ''

        # This is a condition checks if it's a new element separator
        if first_line[i] == '\t':
            i += 1    # Go to the next column
            continue

        # This condition checks whether there's a predefined attribute for the particular column
        if first_line[i] == '[' and first_line[i+1] != ']':
            i += 1
            # This loop stores the name of the attribute without the square brackets.
            while first_line[i] != ']':
                temp_attr += first_line[i]
                i += 1
            i += 1
        else:
            # If no attribute is specified, then add the default None
            temp_attr = None

        # Appends the title until a type starts, or a new column, or it's the end of the string.
        while i < len(first_line) and first_line[i] != '(' and first_line[i] != '\t':
            temp_title += first_line[i]
            i += 1

        # This condition is True if it still has data to process.
        if i < len(first_line):
            # Checking for a type start.
            if first_line[i] == '(':
                i += 1
                # Store it until the end of the type is reached.
                while first_line[i] != ')':
                    temp_type += first_line[i]
                    i += 1
                i += 1
            else:
                temp_type = 'STRING'  # If the type is not specified, default to 'STRING'.
        else:
            temp_type = 'STRING'  # If we reached the end of the file, then default to 'STRING'.
        # Add this column to a list of the Ptdb Object, which stores a column, its attribute, type, and items.
        database.append(Ptdb(temp_title, temp_type, temp_attr))

    # Reset the counters
    i = 1  # This is set to 1 because 0 is the line we already used to store the columns, attributes and types.
    j = 0  # This will be used for parsing the items in each column
    # In this loop the items will be parsed and added to the Ptdb Object.
    while i < len(list_of_lines):
        items = list_of_lines[i].split('\t')  # Get all items in a row by splitting them by tabs.
        # This loop will go through each title and append each corresponding item to it.
        while j < len(items):
            # This will be true if the item is an empty string.
            if not items[j]:
                database[j].items.append(None)  # Sets that item to None
            else:
                # If the item is not empty, then let's add a type cast to it, depending on its column type.
                database[j].items.append(_assign_column_type(items[j], database[j].type_))
            j += 1  # Moves on to the next column
        j = 0   # Restarts to the first column.
        i += 1  # To get the next list of items.

    # Finally, this function returns a Database Object with all the data that was parsed.
    return Database(database)


def parse(file_):
    """Parses a file into a Database Object.

    Parameters
    ----------
    file_: File
        Text file to be parsed

    Return
    ------
    return: Database Object
        Database Object containing all the data

    """
    db_ = open(file_, 'r')  # This opens a file
    string = db_.read()     # This gets the string of the file
    db_.close()             # This closes the file to free up the memory

    new_database = parseString(string)  # This parses the string from the file
    new_database.set_file_to(file_)     # This sets the filename of 'new_database'.

    # Finally, it returns the Database Object.
    return new_database


def createDatabase(name=None):
    """Creates an empty Database Object.

    Parameters
    ----------
    name: String, Optional
        Filename to be set on the Database

    Return
    ------
    return: Database Object
        An empty Database

    """
    return Database([], name)
# End of public global function definitions
