import re

# Eliza chatbot project

userQuit = False
currentResponse = 'Hello, my name is Jamie. My friends call me Eliza.'
# Main loop
while userQuit == False:
    currentSentence = input(currentResponse)
    


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

# TODO: Parsing function, extract and ranks keywords
# Words following 'the', 'my', 'this' stored as nouns


# TODO: Response generator, embed previously identified keywords
# Consider more decomposition templates
