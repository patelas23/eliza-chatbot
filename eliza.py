import re

# Eliza chatbot project
# Made with inspiration from https://web.njit.edu/~ronkowit/eliza.html

# Initialize Regex objects at top of tree
key_word_pattern = re.compile(r'i|you|my|if')
reflexive_switch = re.compile(r'(I)(am|don\'t|)(\w+)')
active_verb_pattern = re.compile(r'(\Bing)(\w+)')
question_pattern = re.compile(r'(do you)(\w+)')
# posessive_pattern = re.compile()

# Create stack of possible responses
response_stack = []

user_quit = False
current_response = 'Hello, my name is Jamie. My friends call me Eliza.'
current_mutation = ''
emotion_response = ''
emotional_state_stack = []

# Main loop
while user_quit == False:
    current_sentence = input(current_response + '\n')

    # If-else branches for most important templates
    # I am... -> Why are you...?
    keyword_match = key_word_pattern.search(current_sentence)
    if(keyword_match):
        print('pass')

    reflexive_match = reflexive_switch.search(current_sentence)
    if(reflexive_match):
        current_template = reflexive_switch.search(current_sentence)
        current_mutation = 'Why are you ' + current_template.group(2)
        current_response = current_mutation
    # until... -> What will happen after...?
    elif(active_verb_pattern.search(current_sentence)):
        pass
    # ... is so ... -> is ... always ...?
    elif():
        pass
    # do you... -> I could hope to ..., maybe someday
    # 
    # 
    else: # Pull response from available stack
        pass

    # Add responses from if-else branches to weighted stack
    # Randomly select a response from the stack
    
    if(current_sentence == 'quit'):
        break

    ### 'I can't' -> 'Why can't you?'

    ### 'Today...' -> 'Does ... happen often?'

    ### 'feel' -> 'Is this a familiar feeling?

    ### TODO: Assign weights to each possible response

    ### TODO: Randomize sub-responses

    ### TODO: Construct stack of possible responses    


print("WELCOME TO JAMIE\n")

print("Hi, my name is Jamie. How are you?")

# if name is mentioned
print("Sorry, I didn't want to lead with anything too personal.")

# if food is mentioned
print("I love those! They go great with apple pie!")

# if statements includes "how are you?"
print("I've been better, I just got back from Florida.")

# if music is mentioned
print("I love heavy metal, electronic, and ambient music.")

# if name is mentioned
print("I don't really care about names.")

# if pet, dog, or cat is mentioned
print("I love taking care of ...s!")

# if 'ha' with repetitions
print("Why are you laughing?")


# TODO: Parsing function, extract and ranks keywords
# Words following 'the', 'my', 'this' stored as nouns


# TODO: Response generator, embed previously identified keywords
# Consider more decomposition templates

