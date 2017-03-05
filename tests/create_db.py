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
