#PTDB v1.0.1
#The MIT license (MIT)
#Copyright (c) 2016 Bryan Morfe. All rights reserved.
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

#Patch 1
#Fixes a bug that causes a FileNotFound error when trying to save or modify a database with no filename
#Fixes a bug that stopped empty attributes defined as '[]' to be checked properly.
#This is some what a 'new' feature, but I will leave it as a bug because it was mean't to do this from the beginning and I forgot to readd it; Fixed a bug in the parsing that didn't let the column type define the value type in the Ptdb Object.
#Fixes a bug that would cause an error when checking for an item in a column different than 'STRING'
#Other small bugs fixed.
#Extra: Added better source code documentation.

class Ptdb:
	#Definition of the data object
	def __init__(self, title, type, attr):
		self.title = title #This is the name of the column
		self.type = type #This is the type of the column--STRING, INT, FLOAT...
		self.attr = attr #This is the attribute of the column--AI, NULL...
		self.items = [] #This is the list of items of the column

def parseString(string):
	#Parsing of a string is done here
	#Variables
	arrayOfLines = string.split('\n') #This statement separates the string into a list of its lines
	firstLine = arrayOfLines[0] #This is the first line, also where all the columns are.
	database = [] #This is an empty list that will be added to the Database Object
	i = 0 #This is a index counter for parsing

	#This first loop is for getting all the columns, their types and attributes.
	while i < len(firstLine):
		#These are some temporary variables for use within the loop
		tempAttr = ''
		tempTitle = ''
		tempType = ''
		
		#This is a simple condition check; It says; If it's a new element separator, then simply increase 'i' and start the loop again.
		if firstLine[i] == '\t':
			i += 1
			continue

		#This condition checks whether there's a predefined attribute for the particular column
		if firstLine[i] == '[' and firstLine[i+1] != ']':
			i += 1
			#This loop stores the name of the attribute without the square brackets.
			while firstLine[i] != ']':
				tempAttr += firstLine[i]
				i += 1
			i += 1
		else:
			#If no attribute is specified, then add the default 'NONE'
			tempAttr = 'NONE'
		
		#Simply store the title of the column in a temporary variable, until the first line is done, or until there's a type start or until there's a new element start.
		while i < len(firstLine) and firstLine[i] != '(' and firstLine[i] != '\t':
			tempTitle += firstLine[i]
			i += 1
		
		#This condition checks for types unless the first line is over.
		if i < len(firstLine):
			#Checking for a type start
			if firstLine[i] == '(':
				i += 1
				#Store it until the end of the type is reached.
				while firstLine[i] != ')':
					tempType += firstLine[i]
					i += 1
				i += 1
			else:
				#If no type is specified, then default to 'STRING'.
				tempType = 'STRING'
		else:
			tempType = 'STRING'
		#Add this column to a list of the Ptdb Object, which stores a column, its attribute, type, and items.
		database.append(Ptdb(tempTitle, tempType, tempAttr))
	
	#Reset the counters for the items
	i = 1 #This is set to 1 because 0 is the line we already used to store the columns, attributes and types.
	j = 0 #This will be used for storing the items in each column
	#In this loop the items will be parsed and added to the Ptdb Object
	while i < len(arrayOfLines):
		#The following statement splits each line into '\t' and creates a list of items, which are separated by '\t'.
		items = arrayOfLines[i].split('\t')
		#This loop will go through each title and append each corresponding item to it.
		while j < len(items):
			#This will simply check if the item is empty or not.
			if len(items[j]) == 0:
				#If the item is empty, then let's make it 'NONE'
				database[j].items.append('NONE')
			else:
				#If the item is not empty, then let's add a type cast to it, depending on its column type.
				if database[j].type.upper() == 'FLOAT':
					database[j].items.append(float(items[j])) #If the column type is float, then let's make it a float.
				elif database[j].type.upper() == 'INT':
					database[j].items.append(int(items[j])) #If the column type is int, then let's make it an int.
				else:
					database[j].items.append(items[j]) #For everything else, let's make it a string.
			j += 1 #Let's move on to the next column
		j = 0 #After the previews loop is done, we start from the first column again.
		i += 1 #We move on to the next array of items.

	#Finally, this function returns a Database Object with all the data that was parsed.
	return Database(database)
		
def parse(file):
	#Parsing of a file is done here.
	ptdb = open(file, 'r') #This opens a file
	string = ptdb.read() #This gets the string and stores it into a variable called 'string'
	ptdb.close() #This closes the file to free up the memory

	newDatabase = parseString(string) #This parses the string from the file and the object is stored in a variable 'newDatabase'
	newDatabase.file = file #This sets the filename of 'newDatabase'.

	#Finally, it returns the Database Object.
	return newDatabase

def createDatabase(name):
	#Will create a new Database object with an empty data array and the provided name.
	return Database([], name)

def stripNewLine(str):
	#Done to delete the last '\n' and '\t' in a string
	i = 0 #This is used to index a string
	newString = "" #This is used to create a copy of the string with the changes made
	
	#This conditions checks whether the finally ends with '\n' or '\t'
	if str.endswith('\n') or str.endswith('\t'):
		#If it enters, then add all the characters to the newString, except for the last one.
		while i < len(str) - 1:
			newString += str[i]
			i += 1

	#Finally, it returns the newString
	return newString

class Database:
	#Definition of the Database Object
	def __init__(self, database, file = ''):
		#This is the initializer of the Database Object. It takes a list of Ptdb Objects and a filename. If no filename is provided, an empty filename is used.
		self.database = database
		self.file = file

	def amountOfColumns(self):
		#Returns the amount of data in the database
		return len(self.database)

	def isItemInColumn(self, col, item):
		#This function takes as a parameter a row name and an item. It will look for that item within that row. Returns true if it found it or false if it doesn't.
		
		#This loops through the entire data in the list of columns.
		for data in self.database:
			#Checks if the column specified is there.
			if data.title.lower() == col.lower():
				#If it is, the loop through the list of items in that column
				for dataItem in data.items:
					#This conditions checks if it's a string to prevent capitalization problems.
					if data.type == 'STRING':
						#Check if the item is or not in the items
						if item.lower() == dataItem.lower():
							#If it's found, then return true
							return True
					else:
						#If it's not a string, then simply check for the item in the database
						if item == dataItem:
							return True

		#If it loops through all the data and does not the the column or the item in the column, then return False.
		return False

	def getItemsInColumn(self, col):
		#This function returns a list with all the items for the specified column.
		
		#This will loop through all the columns in the database.
		for data in self.database:
			#This will check for the particular name of the column specified.
			if data.title.lower() == col.lower():
				#If it finds it, then return the items
				return data.items

		#If it loops through all the data and doesn't find the column, then return an empty list.
		return []

	def getColumnType(self, col):
		#This function returns the type of a particular column (Int, Float, String).
		
		#This loops through all the data
		for data in self.database:
			#Check for the specified column
			if data.title.lower() == col.lower():
				#Return the type of the column
				return data.type

		#If it loops through all the data and doesn't find the column, then return an empty string.
		return ''

	def getColumnAttribute(self, col):
		#This function returns the attributes of a row; Auto Increment, Null.
		
		#This loops through all the data
		for data in self.database:
			#Check for the specified column
			if data.title.lower() == col.lower():
				#Return the attribute of the column
				return data.attr
		
		#If it loops through all the data and doesn't find the column, then return an empty string.
		return ''

	def columnHasAttribute(self, col, attr):
		#This function returns True or False depending if the specified column has the specified attribute.
		
		#This loops through all the data
		for data in self.database:
			#Check for the specified column
			if data.title.lower() == col.lower():
				#This condition checks if the specified attr matches the one in the column
				if data.attr.lower() == attr.lower():
					#If it does, the return true
					return True
				else:
					#If it doesn't, return False
					return False

		#If it loops through all the data and doesn't find the column, then return False.
		return False

	def getRowIndex(self, col, item):
		#This function will return an index for the item's row.
		#Example; getRowIndex('username', 'admin'); returns 3. Later you can call: getColumnItem('password', 3) and returns the password that corresponds
		#to 'admin'.
		index = 0 #This variable will be the index of the column

		#This will loop through all the columns
		for data in self.database:
			#Check for the specified column
			if data.title.lower() == col.lower():
				#If it's the right column, loop through all the items.
				for dataItem in data.items:
					#If it finds the item, then return the index
					if item == dataItem:
						return index
					index += 1 #If it doesn't find the item, then increase the index by one.
		
		#If it loops through all the columns and doesn't find the column or item, return -1.
		return -1

	def getColumnItem(self, col, index):
		#Return the item for the specified column in the specified index.

		#This loops through the columns
		for data in self.database:
			#Check for the specified column
			if data.title.lower() == col.lower():
				#Return the column's item at the specified index.
				return data.items[index]

		#If it loops through the data and doesn't find the column, then return -1.
		return -1

	def getDataForIndex(self, index):
		#Returns the data in a row specified by index.
		i = 0 #Will count all the items in each column.
		data = [] #Empty list of data that will be return later.

		#Loop through the column until the last one.
		while i < len(self.database):
			#Add the item of the current column at the specified index.
			data.append(self.database[i].items[index])
			i += 1
		
		#returns the data.
		return data

	def modifyEntry(self, col, index, newEntry):
		#Modifies an entry. Returns true if successful
		done = False #Variable that determines whether the process is done or not.

		#Loops through all the columns
		for data in self.database:
			#Check for the specified column
			if data.title.lower() == col.lower():
				#If the column is found, the check for the type.
				if data.type.lower() == 'int':
					#Replace the current value with the new one, and sets done to true.
					data.items[index] = int(newEntry)
					done = True
				elif data.type.lower() == 'float':
					#Replace the current value with the new one, and sets done to true.
					data.items[index] = float(newEntry)
					done = True
				else:
					#Replace the current value with the new one, and sets done to true.
					data.items[index] = str(newEntry)
					done = True

			#Checks if the value has been already replaced.
			if done:
				#If the value was replaced, the break out of the loop.
				break
		#If the process finished successfully; save the database
		if done:
			self.saveDatabase()

		#Return if the process was completed or not.
		return done
	
	def newEntry(self, titles, entries):
		#This method returns True if the new entry was added successfully, otherwise, returns False
		autoIncrement = False #This boolean is used to determine whether a column with an attribute of AI has been added
		amountOfTitles = 0 #This stores the amount of titles
		index = 0
		notInTitles = []
		notNullTitles = []
		#This condition makes sure that there are as many titles as there are entries
		if len(titles) != len(entries):
			#If it enters, then simply return False and end execution
			return False
		
		for title in titles:
			for data in self.database:
				if data.attr.upper() != 'NULL' and data.attr.upper() != 'AI':
					notNullTitles.append(data.title)
				
				if title.lower() == data.title.lower():
					if data.attr.upper() == 'AI':
						autoIncrement = True
					amountOfTitles += 1
		
		if amountOfTitles != len(titles) or autoIncrement:
			return False
		
		#Check if not null title isn't there.
		i = 0
		j = 0
		for title in notNullTitles:
			for secondTitle in titles:
				if title.lower() != secondTitle.lower():
					j += 1
				i += 1
			if j == i:
				return False
			i = 0
			j = 0
		
		i = 0
		while i < len(self.database):
			if self.database[i].attr.upper() == 'AI':
				if len(self.database[i].items) > 0:
					index = int(self.database[i].items[-1]) + 1
				else:
					index = 0
				break
			i += i
		self.database[i].items.append(index)
		
		i = 0

		while i < len(titles):
			for data in self.database:
				if titles[i].lower() == data.title.lower():
					data.items.append(entries[i])
			i += 1
		i = 0

		for data in self.database:
			if data.attr.upper() == 'NULL':
				for title in titles:
					if data.title != title:
						j += 1
					i += 1
			if j == i and i != 0:
				data.items.append('NONE')
			i = 0
			j = 0
		
		self.saveDatabase()

		return True

	def removeEntry(self, index):
		#Removes the entire entry in an specified index

		#Loop through the columns
		for data in self.database:
			#Removes the item of the column in the specified index
			data.items.pop(index)
		
		#Saves the database
		self.saveDatabase()
	
	def addTitle(self, title, type = 'STRING', attr = 'NONE'):
		#This method adds a new column to the da
		can = True #This variables dictates whether you can add a new title or not. By default you can

		#This condition checks whether you entered an empty name for your column
		if title == '':
			#If entered, return False
			return False
		
		#Loops through the columns
		for data in self.database:
			#Condition that checks if at least one column has items
			if len(data.items) > 0:
				#If entered, then we say that you can't add a new column with one exception; keep reading.
				can = False

		#The condition says; if we can add a title OR if we can't but the attribute is 'NULL', then let's do it.
		if can or not can and attr.lower() == 'null':
			#If enters then add the new title and save the database
			self.database.append(Ptdb(title, type, attr))
			self.saveDatabase()
			can = True
		
		#Returns true if successfully, false otherwise.
		return can

	def addTitles(self, titles, types, attrs):
		#This method adds multiple columns.
		i = 0 #This will work as our column index.

		#This condition checks that we have the same amount of title, types and attributes
		if len(titles) != len(types) or len(types) != len(attrs):
			#If entered, then return False and end execution.
			return False
		else:
			#If not, the loop through the list of titles to be added.
			while i < len(titles):
				#This condition will call the function addTitle, and attempt to add the titles one by one.
				if not self.addTitle(titles[i], types[i], attrs[i]):
					#If entered here, then return False and end execution
					return False
				#Go to the next title
				i += 1
		
		#If got to this point, then everything went smooth, return True.
		return True

	def saveDatabase(self):
		#Saves all the content in the object to a file with the object's file name.

		#The file will only be saved if a filename has been set.
		if len(self.file) > 0:
			saveFile(self.file, formatDataStr(self.database))
		

def formatDataStr(database):
	#Formats a string for ptdb
	newStr = ""
	i = 0
	for data in database:
		if data.attr != 'NONE':
			newStr += '[' + data.attr.upper() + ']'
		newStr += data.title
		if data.type.lower() != 'string':
			newStr += '(' + data.type.upper() + ')'
		newStr += '\t'
	newStr = stripNewLine(newStr) + '\n'
	
	while i < len(database[0].items):
		j = 0
		while j < len(database):
			if database[j].items[i] != 'NONE':
				newStr += str(database[j].items[i])
			newStr += '\t'
			j += 1
		newStr = stripNewLine(newStr) + '\n'
		i += 1

	return stripNewLine(newStr)
	
def saveFile(file, str):
	#Saves a file with a specified name and content. 
	ptdb = open(file, 'w')
	ptdb.write(str)
	ptdb.close()
