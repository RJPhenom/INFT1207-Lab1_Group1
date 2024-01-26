###############################################################################
#   Class:          INFT1207
#   Authors:        Robert Macklem and Afoma Egwuatu
#   Date:           January 23 2024
#   File:           Lab1_robert_afoma.py
#   Description:    A strong password generator that takes length and number
#                   of different character inputs from the user to generate
#                   a strong password.
###############################################################################
import random
import string

# CONSTS
# Const minimum password length
MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 24

# Const minimum(s) for three key char types:
# (alphabetical, numeric, and special)
MIN_ALPHABET_CHAR = 1
MIN_NUMERIC_CHAR = 1
MIN_SPECIAL_CHAR = 1

# Dict of char types
CHAR_TYPES = {
    "alphabet": string.ascii_letters,
    "numeric": string.digits,
    "special": "@#$%"
}


# VARS
# Variables that track the total length and how many of each
# char we need (note, alpha = len-(special+numeric)).
password_len = 0
alphabet_chars_num = 0
numeric_chars_num = 0
special_chars_num = 0

# Var to store the actual password
password = ""


# FUNCTIONS
# get_chars_of_type is the main function that will grab number of characters
# from a type list (alpha, numeric, special) and return how many we need for
# the password.
def get_chars_of_type(num: int, char_type: str):
    chars_selection = CHAR_TYPES[char_type]
    chars_found = ""

    for i in range(num):
        chars_found += chars_selection[i]

    # TODO: Randomization
    return chars_found


# build_password_with_chars is the main function called to build the final password string
# that we will return to the user. It calls get_chars_of_type on our three main char types
# to build an unsorted string, then randomizes the position of each char in a string, then
# returns the randomized string as a strong password.
def build_password_with_chars(alphabet_num: int, numeric_num: int, special_num: int):
    temp_password = ""
    temp_password += (get_chars_of_type(alphabet_num, "alphabet")
                      + get_chars_of_type(numeric_num, "numeric")
                      + get_chars_of_type(special_num, "special")
                      )

    # Use random lib to shuffle password (randomize char order/jumble it)
    char_list = list(temp_password)  # Convert to list
    random.shuffle(char_list)  # Shuffle
    temp_password = ''.join(char_list)  # Convert back to str

    return temp_password


# PROGRAM
# Startup message
print("\nRandom Password Generator\n")
print(get_chars_of_type(1, "alphabet"))  # testing only, to be removed

# Get the desired password length
while password_len == 0:
    valid_length = False
    try:
        proposed_length = int(input("Please input your desired password length: "))
        if proposed_length < MIN_PASSWORD_LENGTH or proposed_length > MAX_PASSWORD_LENGTH:
            print(f"\nPassword must be within the length range of {MIN_PASSWORD_LENGTH} to {MAX_PASSWORD_LENGTH}.")
            print("Please input a new desired password length.\n")
        else:
            password_len = proposed_length
    except:
        print("\n***INPUT ERROR***\nPlease use numeric characters only.\n")


# Get the desired numeric characters
# TODO: Add similar while loop to above for special chars


# Get the desired numeric characters
# TODO: Add similar while loop to above for special chars


# Get the desired numeric characters
alphabet_chars_num = 4#password_len - (numeric_chars_num + special_chars_num)


# Build the password
password = build_password_with_chars(alphabet_chars_num, numeric_chars_num, special_chars_num)
print(f"Your strong password is: {password}")

