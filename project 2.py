def Header(param1):
    
    intro = f"""\n Good Day and Welcome to Sebastian Sloan's project 2!! You are currently \n
            viewing problem {param1} Please read the instructions for this specific \n
            problem carefully before starting the program. Thank you and enjoy!"""
            
    return intro

# Problem 1

print(Header(1))
print("")
print("")

print("""For this program will take any sentance that you type in and return \n
      how many words are in the sentence! So please type in a sentance or phrace \n
      all in one go and then hit ENTER to see the count of the words in your \n
      sentence! Enjoy.""")
print("")

userSentence = input("Please enter your full sentence here: ")
print("")

def countWords(paramString):
    
    stringLength = len(paramString.split())
    
    return stringLength

print(f"The number of words in your Sentance is: {countWords(userSentence)}")
    
    
      
      
