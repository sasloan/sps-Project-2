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
print("")
    
    
# Problem 2a

print(Header('2a'))
print("")      
print("")      
      
print("""For this Program we will be taking in a associates salary and the percentage \n
      of the salary they earned to determine what their annual bonus should be \n
      you will need to input both the associates salary and what your companies percentage \n
      for bonus's is to determine how much this individuals bonus pay will be. Please \n
      only enter only numbers into this program as anything else will crash the program, thank you!""")
      
associateSalary = input("Please input the associates GROSS annual income here: $")

companyBonusPercentage = input("Please input the companies percentage for bonus here: ")


def findBonus(paramSalary,paramBonusPercent):
    
    convertPercent = float(paramBonusPercent)/100
    
    bonusAmount = float(paramSalary) * float(convertPercent)
    
    return bonusAmount

print(f"The bonus amount for this associate is:${findBonus(associateSalary,companyBonusPercentage)}")
print("")

# Problem 2b

print(Header('2b'))
print("")
print("")

print("""For this Program you will be a HR manager entering in bonuses for your associates \n
      So first you will enter the associates 'employee ID' then the associates 'Annual Salary' \n
      , then the companies 'bonus percentage' for that associate. Then the system will output \n
      the associates employee ID, Annual Salary, Bonus percentage, bonus amount, How many associates \n
      there are, The total bonuses issued and finally the average bonuses issued.\n
      To end the program to get your outputs please type in "quit" for the \n
      employee ID section. Please only enter numbers as anything else you enter \n
      will crash the program, thank you! """)
print("")
print("")
print("")

assRow = []

count = 0

totalBonusesIssued = 0

assEmployeeID = input("Please input the Associates 'Employee ID' here: ")

while(assEmployeeID != "quit"):
 
    assRow.append(assEmployeeID)
     
    assSalary = input("Please input the Associates Annual Salary here: $")
    
    assRow.append(assSalary)
    
    assBonusPercentage = input("Please input the Associates Annual Bonus Percentage here: ")
    
    assRow.append(assBonusPercentage)
    
    assBonus = findBonus(float(assSalary),float(assBonusPercentage))
    
    assRow.append(assBonus)
    
    count = count + 1
    
    totalBonusesIssued = totalBonusesIssued + assBonus
    
    avgAssBonus = totalBonusesIssued/count

    print(f"""\n{assRow}""")    
  
    assEmployeeID = input("Please input the Associates 'Employee ID' here: ")
       
else:
    
    assRow.append(count)
   
    assRow.append(totalBonusesIssued)
    
    assRow.append(avgAssBonus)

print(assRow)