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
MAX_PASSWORD_LENGTH = 64

# Const minimum(s) for three key char types:
# (alphabetical, numeric, and special)
MIN_ALPHABET_CHAR = 1
MIN_NUMERIC_CHAR = 1
MIN_SPECIAL_CHAR = 1

# Dict of char types
CHAR_TYPES = {
    "alphabet": string.ascii_letters,
    "numeric": string.digits,
    "special": string.punctuation
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
    # Get the relevant list of potential chars by type using dict and prep return str var
    chars_selection = CHAR_TYPES[char_type]
    chars_found = ""

    for i in range(num):
        # Randomizes which char from the selection is added to the list and then appends to ret var
        char_index = random.randrange(len(chars_selection))
        chars_found += chars_selection[char_index]

    return chars_found


# build_password_with_chars is the main function called to build the final password string
# that we will return to the user. It calls get_chars_of_type on our three main char types
# to build an unsorted string, then randomizes the position of each char in a string, then
# returns the randomized string as a strong password.
def build_password_with_chars(alphabet_num: int, numeric_num: int, special_num: int):
    # Preps return str var and populates it with a concatenation of 3 strs, representing the random chars of
    # each type we need/want to use in our password.
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

# Get the desired password length
while password_len == 0:
    # Use boolean to track validation
    valid_length = False
    try:
        # Get input and, if invalid, print an error message. Otherwise, assign it and break the while loop.
        proposed_length = int(input("Please input your desired password length: "))
        if proposed_length < MIN_PASSWORD_LENGTH or proposed_length > MAX_PASSWORD_LENGTH:
            print("\n***INPUT ERROR***")
            print(f"Password must be within the length range of {MIN_PASSWORD_LENGTH} to {MAX_PASSWORD_LENGTH}.")
            print("Please input a new desired password length.\n")
        else:
            password_len = proposed_length
            valid_length = True
    except:
        print("\n***INPUT ERROR***\nPlease use numeric characters only.\n")


# Get the desired numeric characters
while numeric_chars_num == 0:
    # Establish the max number of numeric characters possible and prep error msg for 120char line restriction
    max_numeric_chars = password_len - MIN_NUMERIC_CHAR - MIN_SPECIAL_CHAR
    error_msg = f"\n***INPUT ERROR***\nPlease input a number in range {MIN_NUMERIC_CHAR} to {max_numeric_chars}.\n"

    # Use boolean to track validation
    valid_num = False
    try:
        # Get input and, if valid, assign it as the num. Otherwise, print error_msg
        proposed_num = int(input("Please input your desired number of numeric characters: "))
        if MIN_NUMERIC_CHAR <= proposed_num <= max_numeric_chars:
            numeric_chars_num = proposed_num
            valid_num = True
        else:
            print(error_msg)
    except:
        print(error_msg)


# Get the desired numeric characters
while special_chars_num == 0:
    # Establish the max number of numeric characters possible and prep error msg for 120char line restriction
    max_special_chars = password_len - numeric_chars_num - MIN_ALPHABET_CHAR
    error_msg = f"\n***INPUT ERROR***\nPlease input a number in range {MIN_SPECIAL_CHAR} to {max_special_chars}.\n"

    # Use boolean to track validation
    valid_num = False
    try:
        # Get input and, if valid, assign it as the num. Otherwise, print error_msg
        proposed_num = int(input("Please input your desired number of special characters: "))
        if MIN_SPECIAL_CHAR <= proposed_num <= max_special_chars:
            special_chars_num = proposed_num
            valid_num = True
        else:
            print(error_msg)
    except:
        print(error_msg)

# Get the desired numeric characters
alphabet_chars_num = password_len - (numeric_chars_num + special_chars_num)


# Build the password
password = build_password_with_chars(alphabet_chars_num, numeric_chars_num, special_chars_num)
print(f"Your strong password is: {password}")

