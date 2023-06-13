#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

f1 = open("./Input/Letters/starting_letter.txt", "r")
letter = f1.read()

f2 = open("./Input/Names/invited_names.txt", "r")
names = f2.readlines()


for i in names:
    i = i.strip()
    nl = letter.replace("[name]", i)
    with open(f"./Output/ReadyToSend/letters_for_{i}.txt",mode="w") as completed_letter:
        completed_letter.write(nl)



