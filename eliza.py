import re

# Author: Ankur Patel
# Natural Language Processing CMSC 416-001
#   Dr. Bridget McInnes
# Spring 2022
# Chatbot meant to emulate the classic Eliza bot. 
#   This is a simplified pythonic interpretation. 
# Made with inspiration from https://web.njit.edu/~ronkowit/eliza.html

# Input: Hello Eliza, I am feeling unmotivated.  
# Output: Why are you feeling unmotivated?

# Algorithm: Each pattern searches the input for a match.
#   Responses are generated in a heirarchy according
#       to position in if-else tree
#       In descending order of importance:
#           Reflexive statements ('I am sad/happy/etc.)
#           Descriptive statements ('___ is so ___')
#           Questions to bot ('Do you think ___ ?)
#           Conversation termination ('Bye/I'm done/I quit')

### Initialize Regex objects at top of tree
key_word_pattern = re.compile(r'i|you|my|if')

reflexive_switch_pattern = re.compile(r'(\bi\b).+(\bam\b)\s(.*)')
active_verb_pattern = re.compile(r'(\w+ing)\s(\w+)')
question_pattern = re.compile(r'(\bdo you\b)\s(.*)')
exasperated_pattern = re.compile(r'(\w+)\s(is so)\s(\w+)')
quit_pattern = re.compile(r'\bquit\b|\bbye\b|\bdone\b')
# posessive_pattern = re.compile()

### Create stack of possible responses
response_stack = []

### Initialize variables for user interface
user_quit = False
current_response = 'Hello, my name is Jamie. My friends call me Eliza.'

### Main loop
while user_quit == False:
    ### Perform all parsing on lowercase input
    current_sentence = input(current_response + '\n')
    current_sentence = current_sentence.lower()

    ### Parse sentence against each regex pattern
    # keyword_match = key_word_pattern.search(current_sentence)
    reflexive_match = reflexive_switch_pattern.search(current_sentence)
    exasperated_match = exasperated_pattern.search(current_sentence)
    question_match = question_pattern.search(current_sentence)
    quit_match = quit_pattern.search(current_sentence)

    # if(keyword_match):
    if(reflexive_match):
        current_response = 'Why are you ' + reflexive_match.group(3) + '?'
    elif(exasperated_match):
        current_response = "Is " + \
            exasperated_match.group(1) + " always so " + \
            exasperated_match.group(3) + "?"
    elif(question_match):
        current_response = "I am incapable of " + question_match.group(2)
    elif(quit_match):
        print("\n Okay then, goodbye! \n")
        break
    else:
        pass
        # current_response = response_stack.pop()