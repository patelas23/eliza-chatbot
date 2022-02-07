import re

# Eliza chatbot project
# Made with inspiration from https://web.njit.edu/~ronkowit/eliza.html


# Initialize Regex objects at top of tree
reflexiveSwitch = re.compile(r'(I)(am|don\'t|)(\w+)')

active_verb_pattern = re.compile(r'(\Bing)')
# posessive_pattern = re.compile()

# Create stack of possible responses


userQuit = False
currentResponse = 'Hello, my name is Jamie. My friends call me Eliza.'
currentMutation = ''

# Main loop
while userQuit == False:
    currentSentence = input(currentResponse + '\n')

    ### Mutation of 'I am...' to 'Why are you...?'
    # print(rs.group(0))
    # print("Hey, I'm here.")
    if(reflexiveSwitch.search(currentSentence) != None):
        # Save the rest of the input sentence
        # Append it to new statement
        currentTemplate = reflexiveSwitch.search(currentSentence)
        currentMutation = 'Why are you ' + currentTemplate.group(2)
        currentResponse = currentMutation

    elif(active_verb_pattern.search(currentSentence)):
        pass
    elif():
        pass
    else: # Pull response from available stack
        pass
    
    if(currentSentence == 'quit'):
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

