#
#===================================================================================
#
# NAME        : any_text_palindrome.py
# DATE        : 15th Oct, 2019
# DESCRIPTION : A Python program to find, if a given text is a Palindrome or not.
# AUTHOR      : V Bhaskar
# VERSION     : 1.0
#
# Change History:
#   VBhaskar    15/10/2019  Created     Added initial version of file
#   VBhaskar    15/10/2019  Edited      Changed logic to use slicing which is faster.
#
#=====================================================================================
#
"""
    This program is to check if the given text is Palindrome or NOT.
    We reverse the text and compare with original text for equality.
    The text is a Palindrome is they are equal, else the text is NOT a palindrome.

    Pseudocode:
        1. Prompt the user for text
        2. Read the text from user
        3. Reverse the user given text
        4. Compare original text with reversed text for equality
        5. IF check is true then it is a palindrome
           ELSE it is not a palindrome
"""
import os
import sys
import inspect
from datetime import datetime

## User defined variables
INPUT_FILENAME = 'input.txt'

LOG_FILENAME = '/tmp/' + str((sys.argv[0]).rsplit('.',1)[0]) + '.log'
# This is a method to print given message with details for debugging.
# Arguments: 
#       msg - The message to be printed
def my_print(msg):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(str(sys.argv[0]) + ': '+ dt_string + ': ' + str(inspect.currentframe().f_back.f_lineno)  + ': INFO: ' + msg)

# This is a method to find if a given string is palindrome or not.
# Arguments:
#       string_word - word of text
def is_palindrome(string_word):
    ret_msg = "{} is NOT a Palindrome".format(string_word)
    # Reverse the given text using slicing and compare with original text
    if string_word[::-1] == string_word:
        ret_msg.replace('NOT', '')
    return ret_msg

# This is a method to readline from given file
# Arguments:
#       inputfile - input file to read a line
def readline_from_file(inputfile):
    try:
        fh = open(inputfile, 'r')
        # Read the text from file and remove trailing newline character
        text_data = fh.readline().rstrip()
        fh.close()
    except Exception as e:
        my_print('Failed to read from file:' + str(e))
        my_print('Setting text as \'default\'')
        text_data = 'default'
    return text_data

## Ensure that only 'bhasvara' user can run this program.
if os.environ['USER'] != 'bhasvara':
    my_print("ERROR: This program must be run by 'bhasvara' user only.")
    exit(1)

# Check if the text is given from Command line interface
if len(sys.argv) >= 2:
    my_print('The last argument from CLI was: ' + str(sys.argv[-1]))
    my_print('Word of text was given via CLI arguments')
    text_data = str(sys.argv[1])
else:
    # Check if the text is given from environment variable
    try:
        text_data = os.environ['TEXT_DATA']
        my_print('Word of text was given via TEXT_DATA variable in the environment.')
    except KeyError:
        # Check if a file input.txt exists in current directory and use it.
        if os.path.isfile(INPUT_FILENAME):
            my_print("{} file exists. Reading from it.".format(INPUT_FILENAME))
            text_data = readline_from_file(INPUT_FILENAME)
        else:
            # Prompt user and read text from console
            # Ternary operator => text_data = input('Please enter a text: ') if sys.stdin.isatty() else input()
            if sys.stdin.isatty():
                try:
                    text_data = input("Please enter a word of text: \n")
                except KeyboardInterrupt:
                    my_print("You have pressed CTRL-C. So, using \'default\' as text.")
                    text_data = 'default'
            else:
                # If we are not having a stdin() attached then read directly without prompy. 
                #   Ex: PIPE (|) input from echo
                text_data = input()
    finally:
        # we have the final text_data to validate
        my_print('\"' + text_data + '" is the given word of text.')

# Check if we have multiple strings with 'space' separation
for wordstr in text_data.split():
    my_print(is_palindrome(wordstr))
