# import randint function from random library
from random import randint

# set the minimum allowable length of the password
minimum_length = 6

# set lowercase, uppercase, and special charatcter components for password
lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
special_character = '!@#$%^&*'

# generate password takes a length as an input and returns a random password of lower, upper, and special characters of that length
def generate_password( length, upper, special ):
    new_password = ''
    character_options = [lower_alphabet]
    
    # check if the user chose to include upper or special characters in addition to lowercase
    if upper == 'Y' or upper == 'y':
        character_options.append(upper_alphabet)
    if special == 'Y' or special == 'y':
        character_options.append(special_character)

    # generate a random integer to select lower, upper, and special (if included)
    # generate a random number to select a character in selected type
    # add to new_password and decrease length by one
    # repeat for selected password length

    while length > 0:
        a = randint( 0, len(character_options) - 1 )
        b = randint( 0, len(character_options[a]) - 1 )

        new_password += character_options[a][b]

        length -= 1

    print( 'Your new secret password is: %s' % new_password )

def get_password_requirements():
    # ask user if they would like to include UPPERCASE CHARACTERS IN THE PASSWORD
    # include in while loop to verify that either a y or n is input
    while True:
        upper = input('Include UPPERCASE CHARACTERS? (Y/N) \n')
        if upper == 'Y' or upper == 'y' or upper == 'N' or upper == 'n':
            break
        else:
            print('Please input Y or N')
            
    # repeate for special characters
    while True:
        special = input('Include special ch@r@cters? (y/n) \n')
        if special == 'Y' or special == 'y' or special == 'N' or special == 'n':
            break
        else:
            print('Please input Y or N')

    # ask user for desired password length, minimum length is set above, in while loop to require correct length
    while True:
        length = int( input( 'How long would you like your password to be? \n (Minimum length of %d)\n' % minimum_length ) )
        if length < minimum_length:
            print('Minimum password length is 6!')
        else:
            generate_password( length, upper, special )
            break



# call get_password_requirements to execute program
get_password_requirements()