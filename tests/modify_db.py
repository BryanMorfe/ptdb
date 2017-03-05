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
        db_password = my_db.getColumnItem('password', my_db.getRowIndex('email', email.lower()))
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
