###############################################################################
#   Class:          INFT1207
#   Authors:        Robert Macklem and Afoma Egwuatu
#   Date:           January 23 2024
#   File:           Lab1_robert_afoma.py
#   Description:    A strong password generator that takes length and number
#                   of different character inputs from the user to generate
#                   a strong password.
###############################################################################


# CONSTS
# Const minimum password length
MIN_PASSWORD_LENGTH = 8

# Const minimum(s) for three key char types:
# (alphabetical, numeric, and special)
MIN_ALPHABET_CHAR = 1
MIN_NUMERIC_CHAR = 1
MIN_SPECIAL_CHAR = 1

# Dict of char types
CHAR_TYPES = {
    "alphabet": "abcdef",
    "numeric": "123",
    "special": "@#$%"
}


# VARS
# Variables that track the total length and how many of each
# char we need (note, alpha = len-(special+numeric)).
password_len = 0
special_chars = 0
numeric_chars = 0


# FUNCTIONS
# get_chars_of_type is the main function that will grab number of characters
# from a type list (alpha, numeric, special) and return how many we need for
# the password.
def get_chars_of_type(num: int, char_type: str):
    chars_selection = CHAR_TYPES[char_type]
    chars_found = ""

    for i in range(num):
        chars_found += chars_selection[num]

    # TODO: Randomization
    return chars_found


# PROGRAM
# Startup message
print("\nRandom Password Generator\n")
print(get_chars_of_type(1, "alphabet")) # testing only, to be removed

