from ptdb import parse

def login(email, password):
    # Returns true or false whether is logged successfully

    # parse the database
    my_db = parse('database')

    # Check if email is in database
    if my_db.isItemInColumn('email', email.lower()):
        # If email is in the database, check the password for that entered email.

        db_password = my_db.getColumnItem('password', my_db.getRowIndex('email', email.lower())) 
        # This above statement is saying; 'Get the password of the row where the column email is 'email.lower()'

        # Now we compare the entered password with the one corresponding to that email, if they're equal, the login is successfully,          # else, it's not
        if password == db_password:
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
