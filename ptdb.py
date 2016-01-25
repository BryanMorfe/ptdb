#PTDB v1.0.0
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

class Ptdb:
	#Definition of the data object
	def __init__(self, title, type, attr):
		self.title = title
		self.type = type
		self.attr = attr
		self.items = []

def parseString(string):
	#Parsing of a string is done here
	arrayOfLines = string.split('\n')
	firstLine = arrayOfLines[0]
	database = []
	i = 0
	while i < len(firstLine):
		tempAttr = ''
		tempTitle = ''
		tempType = ''
		if firstLine[i] == '\t':
			i += 1
			continue
		if firstLine[i] == '[' and firstLine[i+1] != '[':
			i += 1
			while firstLine[i] != ']':
				tempAttr += firstLine[i]
				i += 1
			i += 1
		else:
			tempAttr = 'NONE'
		while i < len(firstLine) and firstLine[i] != '(' and firstLine[i] != '\t':
			tempTitle += firstLine[i]
			i += 1
		if i < len(firstLine):
			if firstLine[i] == '(':
				i += 1
				while firstLine[i] != ')':
					tempType += firstLine[i]
					i += 1
				i += 1
			else:
				tempType = 'STRING'
		else:
			tempType = 'STRING'
		database.append(Ptdb(tempTitle, tempType, tempAttr))
	i = 1
	j = 0
	while i < len(arrayOfLines):
		items = arrayOfLines[i].split('\t')
		while j < len(items):
			if len(items[j]) == 0:
				database[j].items.append('NONE')
			else:
				database[j].items.append(items[j])
			j += 1
		j = 0
		i += 1

	return Database(database)
		
def parse(file):
	#Parsing of a file is done here.
	ptdb = open(file, 'r')
	string = ptdb.read()
	ptdb.close()

	newDatabase = parseString(string)
	newDatabase.file = file

	return newDatabase

def createDatabase(name):
	#Will create a new Database object with an empty data array and the provided name.
	return Database([], name)

def stripNewLine(str):
	#Done to delete the last '\n' and '\t' in a string
	i = 0
	newString = ""
	if str.endswith('\n') or str.endswith('\t'):
		while i < len(str) - 1:
			newString += str[i]
			i += 1
	return newString

class Database:
	#Definition of the Database object
	def __init__(self, database, file = ''):
		self.database = database
		self.file = file

	def amountOfColumns(self):
		#Returns the amount of data in the database
		return len(self.database)

	def isItemInColumn(self, col, item):
		#This function takes as a parameter a row name and an item. It will look for that item within that row. Returns true if it found it or false 
		#if it doesn't.
		found = False
		for data in self.database:
			if data.title.lower() == col.lower():
				for dataItem in data.items:
					if item.lower() == dataItem.lower():
						found = True
		return found

	def getItemsInColumn(self, col):
		#This function returns an array with all the items for the specified column.
		items = []
		for data in self.database:
			if data.title.lower() == col.lower():
				items = data.items
		return items

	def getColumnType(self, col):
		#This function returns the type of a particular row (Int, Float, Double, String).
		type = ""
		for data in self.database:
			if data.title.lower() == col.lower():
				type = data.type
		return type

	def getColumnAttribute(self, col):
		#This function returns the attributes of a row; Auto Increment, Null.
		attr = ""
		for data in self.database:
			if data.title.lower() == col.lower():
				attr = data.attr
		return attr

	def columnHasAttribute(self, col, attr):
		#This function returns True or False depending if the specified row has the specified attribute.
		found = False
		for data in self.database:
			if data.title.lower() == col.lower():
				if data.attr.lower() == attr.lower():
					found = True
		return found

	def getRowIndex(self, col, item):
		#This function will return an index for the item's row.
		#Example; getColumnIndex('Username', 'admin'); returns 3. Later you can call: getRowItem('password', 3) and returns the password that corresponds
		#to 'admin'.
		index = 0
		for data in self.database:
			if data.title.lower() == col.lower():
				for dataItem in data.items:
					if item == dataItem:
						return index
					index += 1		
		return -1

	def getColumnItem(self, col, index):
		#Return the item for the specified column in the specified index.
		for data in self.database:
			if data.title.lower() == col.lower():
				return data.items[index]
		return ''

	def getDataForIndex(self, index):
		#Returns the data in a specified row by index.
		i = 0
		data = []
		while i < len(self.database):
			data.append(self.database[i].items[index])
			i += 1
	
		return data

	def modifyEntry(self, col, index, newEntry):
		#Modifies an entry. Returns true if successful
		done = False
		for data in self.database:
			if data.title.lower() == col.lower():
				if data.type.lower() == 'int':
					data.items[index] = int(newEntry)
					done = True
				elif data.type.lower() == 'float':
					data.items[index] = float(newEntry)
					done = True
				else:
					data.items[index] = str(newEntry)
					done = True
		if done:
			self.saveDatabase()

		return done
	
	def newEntry(self, titles, entries):
		#This function returns True if the new entry was added successfully, otherwise, returns False
		autoIncrement = False
		amountOfTitles = 0
		index = 0
		notInTitles = []
		notNullTitles = []
		if len(titles) != len(entries):
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
		for data in self.database:
			data.items.pop(index)
		self.saveDatabase()
	
	def addTitle(self, title, type = 'STRING', attr = 'NONE'):
		can = True
		if title == '':
			return False
		for data in self.database:
			if len(data.items) > 0:
				can = False
		if can or not can and attr.lower() == 'null':
			self.database.append(Ptdb(title, type, attr))
			self.saveDatabase()

		return can

	def addTitles(self, titles, types, attrs):
		i = 0
		if len(titles) != len(types) or len(types) != len(attrs):
			return False
		else:
			while i < len(titles):
				if not self.addTitle(titles[i], types[i], attrs[i]):
					return False
				i += 1

		return True

	def saveDatabase(self):
		#Saves all the content in the object to a file with the object's file name.
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
