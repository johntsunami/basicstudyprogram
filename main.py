from studybank import *
import os 
import itertools  #required to chunk together parts of python dictionary
from pathlib import Path  # Used to check if file exists

missed_dir = 'studybank/missed/'
Path(missed_dir).mkdir(parents=True, exist_ok=True)  # Create missed directory if it doesn't exist


def addblankspaces(num_of_blank_spaces):
    for i in range(num_of_blank_spaces):
        print("")

## asks users initial questions
def inital_options():
    addblankspaces(3)
    print("Hello!  Welcome to JC Master Study Program.  Please select one of the following options below.")
    print("1. Input study questions and answers")
    print("2. Select a study subject")
    print("3. Repeat Challenging questions")
    addblankspaces(3)
    initialanswer = input("Enter your choice (1/2/3): ")
    addblankspaces(3)
    return initialanswer
   
## Based on answer it proceeds to next  section

selected_option = inital_options()
addblankspaces(3)

def option2section():
    # Starting with option 2 now this is the main function I need to finish first I can go back and add 2 and 3 later
    if selected_option == '2':
        print("Ok Lets look at what you can study.")
        ## GETS ALL OF THE FILE NAMES WITHIN A FOLDER TO TELL USER WHAT SUBJECTS THEY CAN STUDY
        path = r"C:\Users\johnc\OneDrive\Desktop\John_Script\jc_study_software\jcstudyprogram\studybank"  # Replace with your folder path
        num = 0
        file_name_list = []
        for file_name in os.listdir(path):  # takes off the txt on the end 
            num += 1
            stripped_word = file_name.split('.', 1)[0]  # Split at first occurrence of '.' and select second part
            file_name_option = str(num) + ': ' + stripped_word
            print(file_name_option)
            # Output: 'txt'
            file_name_list.append(file_name_option)
        subjectanswer = input("Enter your choice: ")   
        addblankspaces(5)
        print("Great lets begin studying:",stripped_word+'.'," You will master 7 questions at a time before moving to the next set of 7 questions. ")
        addblankspaces(8)


        ## OPEN THE CORRECT OPTION:
        for i in range(50):
            if str(i) in str(subjectanswer): #searches for number 
                for file in file_name_list:
                    if str(i) in file:
                        print("FILE:",file)
                        print("FOUND IT")
                        file_subject = file[3:]
                        subjectfile = 'studybank/' + file_subject + '.txt'  #GOTTA DELETE THE 1: from the line
                        addblankspaces(5)
                        print("Great lets begin studying:",file_subject+'.'," You will master 7 questions at a time before moving to the next set of 7 questions. ")
                        addblankspaces(8)
                
        return subjectfile


## #used in add_questions function
def get_missed_file(subjectfile):

    if three == False:
        filename = missed_dir + Path(subjectfile).stem + '_missed.txt'
    else:
        filename = subjectfile
        return filename

## #used in add_questions function
def add_missed_question(subjectfile, question, answer):
    missed_file = get_missed_file(subjectfile)
    with open(missed_file, 'a+') as f:
        f.seek(0)
        if question not in f.read():
            f.write('Q: ' + question + '\n')
            f.write('A: ' + answer + '\n')
    

subjectfile = option2section()

three = False
## USED TO ITERATE THROUGH MISSED FOLDERS
if selected_option == '3':
    three = True
    path = r"C:\Users\johnc\OneDrive\Desktop\John_Script\jc_study_software\jcstudyprogram\studybank\missed"  # Replace with your folder path
    num = 0
    file_name_list = []
    for file_name in os.listdir(path):  # takes off the txt on the end 
        num += 1
        stripped_word = file_name.split('.', 1)[0]  # Split at first occurrence of '.' and select second part
        file_name_option = str(num) + ': ' + stripped_word
        print(file_name_option)
        # Output: 'txt'
        file_name_list.append(file_name_option)
    subjectanswer = input("Enter your choice: ")   
    addblankspaces(5)
    print("Great lets begin studying:",stripped_word+'.'," You will master 7 questions at a time before moving to the next set of 7 questions. ")
    addblankspaces(8)


    ## OPEN THE CORRECT OPTION:
    for i in range(50):
        if str(i) in str(subjectanswer): #searches for number 
            for file in file_name_list:
                if str(i) in file:
                    print("FILE:",file)
                    print("FOUND IT")
                    file_subject = file[3:]
                    subjectfile = 'studybank/missed/' + file_subject + '.txt'  #GOTTA DELETE THE 1: from the line
                    addblankspaces(5)
                    print("Great lets begin studying:",file_subject+'.'," You will master 7 questions at a time before moving to the next set of 7 questions. ")
                    addblankspaces(8)
    
print("SUBJECT FILE:",subjectfile) 
 

wrong_answers_dic = {}
all_questions_answers_dic = {}

def add_questions_answers_to_dic():
    global all_questions_answers_dic
    # Open the file and read the questions
    with open(subjectfile, 'r') as f:
        lines = f.readlines()

    # Loop through the questions and ask the user to answer them
    #making dic to save wrong question and answer
    
    for line in lines:
          # MAKES SURE ITS IN THIS FORMAT
        if line.startswith('Q: '):
            current_question = line.strip().capitalize()
            current_question = current_question[3:]

            #GETS ANSWERS
            correct_answer = lines[lines.index(line) + 1].lower().strip()
            correct_answer = correct_answer.split(' ', 1)[-1]  # need to strip a: off string.
            all_questions_answers_dic[current_question] =correct_answer
    return all_questions_answers_dic


#Used to check if memoryque is recorded.. if not it will add it in the ask questions function
def modify_file(subjectfile, question):
    # Read the lines from the file
    with open(subjectfile, 'r') as f:
        lines = f.readlines()

    # Loop through the lines and find the question
    for i, line in enumerate(lines):
       
        
        if line.strip().lower().startswith('q: '):
            # print("QUESTION:",question)
            
            questionline = line[3:].strip().lower()
            # print("QUESTOINLINE:",questionline)
            if question in questionline:
                    
                # Find the answer line
                answer_index = i + 1
                while not lines[answer_index].strip().startswith('A: '):
                    answer_index += 1

                # Check if the T line already exists
                t_index = answer_index + 1
                t_exists = False
                while t_index < len(lines) and lines[t_index].strip():

                    if lines[t_index].strip().startswith('M: '):
                        t_exists = True

                        if t_index < len(lines): 
                            print("TAKE A MOMENT TO REMEMBER MEMORY QUE")
                            addblankspaces(2) 
                            print(lines[t_index].strip()) # PRINTS THE LINE
                            addblankspaces(3)
                        break
                    t_index += 1

                # Insert the new text line after the answer line if it doesn't already exist
                if not t_exists:
                    print("")
                    memoryque = input("What does this word sound like or remind you of?")
                    print("")
                    new_line = 'M: ' + memoryque + '\n'
                    lines.insert(answer_index + 1, new_line)

                    # Insert a blank line after the new text line
                    lines.insert(answer_index + 2, '\n')

                    # Write the modified lines back to the file
                    with open(subjectfile, 'w') as f:
                        f.writelines(lines)
            
                break



def ask_questions():
    global wrong_answers_dic
    chunk_size = 7   ### NOW ITERATE THROUGH THE Dic of all questions to user
    chunks = [list(all_questions_answers_dic.items())[i:i+chunk_size] for i in range(0, len(all_questions_answers_dic), chunk_size)]
    #chunk is 7 questions
    for chunk in chunks: ## HAVE IT iterate a chunk until all are correct then progress to next chunk
        num_questions_in_chunk = len(chunk)
        question_count = 0
        score = 0
        passing = False
        ##MAKE IT REPEAT THIS UNTIL ITS A PERFECT SCORE


        while passing == False:
            for current_question, correct_answer in chunk:    #Must convert  the list of sets
                question_count += 1
                print(str(question_count)+ ':',current_question.capitalize())
                # Ask the user for an answer
                user_answer = input('Your answer: ') 
                user_answer = user_answer.lower().strip()
                # print("USER ANSWER:",user_answer)
                # print("CORRECT ANSWER:",correct_answer)


                if user_answer == correct_answer:
                    addblankspaces(5)
                    print('Correct!')
                    addblankspaces(6)
                    score += 1

                else:
                    # WRITES IT TO MISES WORKING
                    add_missed_question(subjectfile, current_question, correct_answer)
                    print('Incorrect! The correct answer is:', correct_answer)
                    addblankspaces(1)
                    wrong_answers_dic[current_question] = correct_answer
                    #SAVE INCORRECTION QUESTIONS in new file to repeat until they are correct.
                    #add the incorrect ones to the next set of of questions so it keeps asking 7 rotating. 

                    
                    ## RETREAVE MEMORY QUE if its their, if not it will ask user for it and add it.
                    # #not adding it in the dictionary because it might not exist and or have duplicates the dic would delete 
                    modify_file(subjectfile, current_question)


                 

                    ###NOW HAVE IT REPEAT THIS QUESTION 3x
                    print("Since you missed this question it will repeat 3x for memory")
                    for i in range(3):
                        print(str(question_count)+ ':',current_question.capitalize())
                        # Ask the user for an answer
                        user_answer = input('Your answer: ') 
                        user_answer = user_answer.lower().strip()
                addblankspaces(3)   

                
            print("Your score for these questions:", score, '/', num_questions_in_chunk)
             
            if score <=num_questions_in_chunk-1:
                addblankspaces(20)  
                print("You missed",num_questions_in_chunk -score,'questions please review and press enter to try again!')
                addblankspaces(3)  
                score = 0

                ## Have it show all questions with answers here for review
                for key,value in wrong_answers_dic.items():
                    print(key,":",value)

                addblankspaces(3)  
                input("PRESS ENTER WHEN READY")
                addblankspaces(25) 

                #RESET DICTIONARY 
                wrong_answers_dic = {}

                continue
            else:
                print("Good Job continuing to next section")
                break


        
            

    
add_questions_answers_to_dic()

ask_questions()
 



#OTHER
# ask questions other way around... instead of what is the spanish word for "good",  write what is bueno in spanish?


 
    

