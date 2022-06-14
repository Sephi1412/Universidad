import random 

dictVerbs = {"Agree": 1, "Offer": 1, "Promise": 1, "Refuse": 1, "Threaten": 1, 
             "Advise": 2, "Ask": 2, "Convince": 2, "Encourage": 2, "Invite": 2,
             "Invite": 2,  "Persuade": 2, "Remind": 2, "Tell": 2, "Warn": 2, 
             "Doubt": 2, "Complain": 2, "Apologize For": 3, "Insist On": 3,
             "Accuse Somebody Of": 3, "Recommend": 3, "Admit": 3, "Regret": 3,
             "Blame Somebody Of": 3, "Suggest": 3, "Deny": 3, "Announce": 3
             }

def main():
    print("Initializing Exercise: \n")
    boolCycle = True
    sizeDict = len(dictVerbs) - 1
    counter = 0
    while(boolCycle):
        index = random.randint(0,sizeDict)
        selectedVerb = list(dictVerbs.keys())[index]
        correctAnswer = list(dictVerbs.values())[index]
        print(f"Selected Verb: {selectedVerb}")
        print("Category of The Verb? [1], [2] or [3]\n")
        answer = input()
        checkAnswer = answer == str(correctAnswer)

        if (checkAnswer):
            print("Correct!\n")
            counter+=1
        else:
            print(f"Wrong!\nThe correct category was {correctAnswer}\n")
            print(f"Final Score: {counter}\n")
            boolCycle = False

main()