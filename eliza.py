import re

# Eliza chatbot project
# Made with inspiration from https://web.njit.edu/~ronkowit/eliza.html

### Initialize Regex objects at top of tree
key_word_pattern = re.compile(r'i|you|my|if')
reflexive_switch_pattern = re.compile(r'(\bi\b).+(\bam\b)\s(\w+)')
active_verb_pattern = re.compile(r'(\w+ing)\s(\w+)')
question_pattern = re.compile(r'(do you)(\w+)')
exasperated_pattern = re.compile(r'(\w+)\s(is so)\s(\w+)')
quit_pattern = re.compile(r'\bquit\b|\bbye\b')
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
    quit_match = quit_pattern.search(current_sentence)

    # if(keyword_match):
    #     print('pass')
    if(reflexive_match):
        current_response = 'Why are you ' + reflexive_match.group(3) + '?'
    elif(exasperated_match):
        current_response = "Is " + \
            exasperated_match.group(1) + " always so " + \
            exasperated_match.group(3) + "?"
    else:
        pass
        # current_response = response_stack.pop()

    # Add responses from if-else branches to weighted stack
    # Randomly select a response from the stack

    # if(quit_match):
    #     user_quit = True

    # 'I can't' -> 'Why can't you?'

    # 'Today...' -> 'Does ... happen often?'

    # 'feel' -> 'Is this a familiar feeling?


# print("WELCOME TO JAMIE\n")

# print("Hi, my name is Jamie. How are you?")


# # if food is mentioned
# print("I love those! They go great with apple pie!")

# # if statements includes "how are you?"
# print("I've been better, I just got back from Florida.")

# # if music is mentioned
# print("I love heavy metal, electronic, and ambient music.")

# # if name is mentioned
# print("I don't really care about names.")

# # if pet, dog, or cat is mentioned
# print("I love taking care of ...s!")

# # if 'ha' with repetitions
# print("Why are you laughing?")
