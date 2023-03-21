from studybank import *
import os 
import itertools  #required to chunk together parts of python dictionary
from pathlib import Path  # Used to check if file exists
import time


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

    if initialanswer == '1':
        print("This function has not been built yet, please choose another!")
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
       
            if file_name == 'missed': # to avoid it from getting the missed folder
                num -= 1
                continue
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
    
def add_memorycue_incorrect_correct(input_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    new_lines = []
    for i, line in enumerate(lines):
        new_lines.append(line)

        if line.startswith("A:"):
            if (i + 1 >= len(lines) or
                not (lines[i + 1].startswith("M:") and
                     lines[i + 2].startswith("Incorrect:") and
                     lines[i + 3].startswith("Correct:"))):
                
                new_lines.append("M: \n")
                new_lines.append("Incorrect: 0\n")
                new_lines.append("Correct: 0\n")
                new_lines.append("\n")

    with open(input_file, 'w') as f:
        f.writelines(new_lines)


add_memorycue_incorrect_correct(subjectfile)


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
    print("There are",len(all_questions_answers_dic),'total questions in this subject')
    return all_questions_answers_dic


#Used to check if memoryque is recorded.. if not it will add it in the ask questions function
def modify_m_line(subjectfile, question):
    # Read the lines from the file
    with open(subjectfile, 'r') as f:
        lines = f.readlines()

    # Loop through the lines and find the question
    for i, line in enumerate(lines):
        if line.strip().lower().startswith('q: '): # finds question
            questionline = line[3:].strip().lower()
       
            if question in questionline:
                # Find the Attempts line
                answer_index = i + 1
                #THIS IS WORKING

                #Now print 2 lines below it.
                m_line = lines[i+2].strip().lower()

                if len(m_line)< 3:
                    new_memory_cue = input('Input a memory cue that will help you remember this answer:')
                    new_memory_cue = 'M: '+ new_memory_cue +'\n'
                    print("UNDER 3 len")

                    lines[i+2] = new_memory_cue  #INITIALIZe the line change

                    with open(subjectfile, 'w') as file:  #finalyze the line change
                        file.writelines(lines)
                    break


                else:
                    print(m_line)





             
















## USING THIS TO TRACK HOW MANY TIMES A QUESTION IS DONE WRONG
def track_num_of_times_answered_incorrect(subjectfile, question):
    # Read the lines from the file
    with open(subjectfile, 'r') as f:
        lines = f.readlines()

    # Loop through the lines and find the question
    for i, line in enumerate(lines):
        if line.strip().lower().startswith('q: '): # finds question
            questionline = line[3:].strip().lower()
       
            if question in questionline:
                # Find the Attempts line
                answer_index = i + 1
            
                while not lines[answer_index].strip().startswith('A: '):
                    answer_index += 1

                # Check if the T line already exists
                t_index = answer_index + 2
            
               
                while t_index < len(lines) and lines[t_index].strip():
                    if lines[t_index].strip().startswith('Incorrect: '):
                       

                        if t_index < len(lines): #Gets the amount of attempts done already and adds 1 to it.
                            attempt_line = lines[t_index].strip() # PRINTS THE LINE
                       
                            attempts_num = attempt_line[10:]
                            attempts_num = int(attempts_num)
                            attempts_num += 1
                            new_attempts_num = str(attempts_num)
            
                            new_attempts_line = "Incorrect: "+ new_attempts_num + '\n'
                            lines[t_index] = new_attempts_line  #INITIALIZe the line change

                            with open(subjectfile, 'w') as file:  #finalyze the line change
                                file.writelines(lines)

                        
                            addblankspaces(3)
                            return attempts_num -1
                        break
                    t_index += 1

                break

def track_num_of_times_answered_correct(subjectfile, question):
    # Read the lines from the file
    with open(subjectfile, 'r') as f:
        lines = f.readlines()

    # Loop through the lines and find the question
    for i, line in enumerate(lines):
        if line.strip().lower().startswith('q: '): # finds question
            questionline = line[3:].strip().lower()
       
            if question in questionline:
                # Find the Attempts line
                answer_index = i + 1
            
                while not lines[answer_index].strip().startswith('A: '):
                    answer_index += 1


                # Check if the T line already exists
                t_index = answer_index + 3
            
                t_exists = False
          
                while t_index < len(lines) and lines[t_index].strip():
                
                 
                    if lines[t_index].strip().startswith('Correct: '):
                   
                        t_exists = True

                        if t_index+2 < len(lines): #Gets the amount of attempts done already and adds 1 to it.
                            attempt_line = lines[t_index].strip() # PRINTS THE LINE
                            print("Correct_LINE:",attempt_line)
                            attempts_num = attempt_line[9:]
                            print("ATTEMPTS NUM:",attempts_num)
                            attempts_num = int(attempts_num)
                            attempts_num += 1
                            new_attempts_num = str(attempts_num)
            
                            new_attempts_line = "Correct: "+ new_attempts_num + '\n'
                            lines[t_index] = new_attempts_line  #INITIALIZe the line change

                            with open(subjectfile, 'w') as file:  #finalyze the line change
                                file.writelines(lines)

                            print("Correct:",attempts_num)
                            addblankspaces(3)
                            return attempts_num -1
                        break
                    t_index += 1

                break


def check_how_many_incorrect(subjectfile, question):
    # Read the lines from the file
    with open(subjectfile, 'r') as f:
        lines = f.readlines()

    # Loop through the lines and find the question
    for i, line in enumerate(lines):
        if line.strip().lower().startswith('q: '): # finds question
            questionline = line[3:].strip().lower()
       
            if question in questionline:
                # Find the Attempts line
                answer_index = i + 1
            
                while not lines[answer_index].strip().startswith('A: '):
                    answer_index += 1

                # Check if the T line already exists
                t_index = answer_index + 2

                t_exists = False
                while t_index < len(lines) and lines[t_index].strip():
                    if lines[t_index].strip().startswith('Incorrect: '):
                        t_exists = True

                        if t_index < len(lines): #Gets the amount of attempts done already and adds 1 to it.
                            attempt_line = lines[t_index].strip() # PRINTS THE LINE
    
                            attempts_num = attempt_line[10:]
                            attempts_num = int(attempts_num)
                         
                            return attempts_num 
                        break
                    t_index += 1

                # Insert the new text line after the answer line if it doesn't already exist
                if not t_exists:
                  
                    return 0  #return value of 1 since i only used it once
            
                break


def check_how_many_times_answered_correct(subjectfile, question):
    # Read the lines from the file
    with open(subjectfile, 'r') as f:
        lines = f.readlines()

    # Loop through the lines and find the question
    for i, line in enumerate(lines):
        if line.strip().lower().startswith('q: '): # finds question
            questionline = line[3:].strip().lower()
       
            if question in questionline:
                # Find the Attempts line
                answer_index = i + 1
            
                while not lines[answer_index].strip().startswith('A: '):
                    answer_index += 1

                # Check if the T line already exists
                t_index = answer_index + 3
                t_exists = False
                while t_index < len(lines) and lines[t_index].strip():
                    if lines[t_index].strip().startswith('Correct: '):
                        t_exists = True

                        if t_index+2 < len(lines): #Gets the amount of attempts done already and adds 1 to it.
                            attempt_line = lines[t_index].strip() # PRINTS THE LINE
                            attempts_num = attempt_line[9:]
                            print("ATTEMPTS NUM:",attempts_num)
                            attempts_num = int(attempts_num)
                        
                            return attempts_num
                        break
                    t_index += 1

                # Insert the new text line after the answer line if it doesn't already exist
                if not t_exists:
                    pass
                
                return 0
             

def convert_seconds_to_minutes_and_seconds(seconds):
    if len(str(seconds)) > 2:
        minutes = int(seconds)//60
        remaining_seconds = int(seconds) % 60
        print(minutes,"Minute and",remaining_seconds,"Seconds.")
    else:
        print(seconds,"Seconds.")
        



def ask_questions():
    global wrong_answers_dic
    chunk_size = 7   ### NOW ITERATE THROUGH THE Dic of all questions to user
    chunks = [list(all_questions_answers_dic.items())[i:i+chunk_size] for i in range(0, len(all_questions_answers_dic), chunk_size)]
    #chunk is 7 questions
    total_correct = 0

    ## Start timer ##
    start_time = time.time()
    print("")
    new_question_response = input("Would you like only new questions?, type yes or no: ").lower().strip()
    print("")
    for chunk in chunks: ## HAVE IT iterate a chunk until all are correct then progress to next chunk
        num_questions_in_chunk = len(chunk)
        question_count = 0
        score = 0
        passing = False
        ##MAKE IT REPEAT THIS UNTIL ITS A PERFECT SCORE

        while passing == False:
            for current_question, correct_answer in chunk:    #Must convert  the list of sets
                if new_question_response == 'yes':  # then skip all questions that arent new
                    correct_num = check_how_many_times_answered_correct(subjectfile, current_question)
                    incorrect_num = check_how_many_incorrect(subjectfile, current_question)
                    print("CORRECT2:",correct_num)
                    print("INCORRECT2:",incorrect_num)

                    if incorrect_num == 0 and correct_num == 0:
                        print("YUP incorrect greater than 0")
      
                    else:
                        continue
                    
    ## THIS NEW QUESTION FUNCTION AND SKIP NEEDS WORK STILL
                
                question_count += 1
                print(str(question_count)+ ':',current_question.capitalize())
                addblankspaces(5)
                # Ask the user for an answer
                user_answer = input('Your answer: ') 
                user_answer = user_answer.lower().strip()

                if user_answer == "":  # ADDING THIS BECAUSE IT MADE IT CORRECT IF they press enter
                    while user_answer == "":
                            user_answer = input('Your answer: ') 
                            user_answer = user_answer.lower().strip()

                    

                if user_answer == correct_answer or user_answer in correct_answer:
                    addblankspaces(5)
                    print('Correct!')
                    addblankspaces(6)
                    score += 1
                    total_correct +=1
                    track_num_of_times_answered_correct(subjectfile, current_question)

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
                    modify_m_line(subjectfile,current_question)
                    track_num_of_times_answered_incorrect(subjectfile, current_question)

                    ###NOW HAVE IT REPEAT THIS QUESTION 3x
                    print("Since you missed this question it will repeat for memory")
                    for i in range(1):
                        print(str(question_count)+ ':',current_question.capitalize())
                        # Ask the user for an answer
                        user_answer = input('Your answer: ') 
                        addblankspaces(3)   

                        addblankspaces(2) 
                addblankspaces(3)   

                
            print("Your score for these questions:", score, '/', num_questions_in_chunk)
            print("")
            elapsed_time = time.time()- start_time
            elapsed_time = str(elapsed_time)

            period = str(elapsed_time)
    
        
            period = period.find(".")
            period = int(period)
            elapsed_time = elapsed_time[:period]
            
            print("You have learned",total_correct, 'questions in')
            convert_seconds_to_minutes_and_seconds(elapsed_time)
            
             
            if score <=num_questions_in_chunk-1:
                total_correct = total_correct - score  # since i need to delete the ones they got correct so they dont duplicate. 
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
                addblankspaces(3)
                break


        
            

    
add_questions_answers_to_dic()

ask_questions()
 
## HOW TO USE THIS  ###
# Review the full file first

# One hour later do this missed questions for review
# One Day later-


## WHEN ADDING A SUBJeCT
## MEMORIZE KEY CONCEPTS FIRST aDD THOSE FIRST
#  

#OTHER
## Choose new questions so i get x amount of questions new 
## this way i get to keep learning new and avoid too many repeats
##  If I have no attempts then it means Its new or I never got it wrong
## I'll need another way to track correct attempts

## Add line in .txt to track how many times a question has been answered right and wrong.  Starting with 0.  if both are 0 then i know the question is new so i can review only new or know how many new items i reviewed.

##if i'm getting it wrong because I mix it together then add a new question so I understand the difference in the test
# add the different tenses in spanish words
## add audio to the question, which is important so i get used to hearing and responding for spanish.Make correct sound and incorrect sound so i dont have to look at screen.
## FIND OUT TOTAL NUMBER OF QUESTIONS ON A PAGE.
# ask questions other way around... instead of what is the spanish word for "good",  write what is bueno in spanish?

## I want to know how long it takes me to learn completely new words
# So start timer
# track num of questions
# show every 5 minutes how many items i've learned

## TRACK AMOUNT OF TIMES A QUESTION IS MISSED
## create a TIMES MISSED IN TXT FILE to 0 if its not there.
## If it is their then moodify it to Plus 1 each time a question is missed
## This way I can only review questions that have missed a certain amount
## Ex.. TIME MISSED 0- none, Time_missed 1-3 -easy,  Time_missed 4-6 Moderate, Time_missed 7 + = hard
# for the purpose of reviewing questions that are too easy too many times.  
# might just need to only review it 

# SO THE QUESTION IS.. HOW DO I AVOID REPEATING QUESTIONS TOO MANY TIMES IN ONE DAY
# gRADUATE THEM AFTER 3X IN ONE DAY IS PROBABLY A GOOD STRATEGY BECAUSE MY MAX QUESTIONS IS GONNA GET TOO HIGH
## OR JUST MODIFY THE MISSED FILE?  PROBABLY EASIER TO KEEP THEM IN ONE FILE AND JUST TRACK AMOUNT OF TIMES ITS BEEN MISSED

#actually  THE QUESTION IS HOW TO AVOID REPEATING QUESTIONS TOO MANY TIMES 
# SO EVENTUALLY I'M GOING TO HAVE 4000 ITEMS
# NEED TO KEEP VOLUME DOWN 10%
# SO TO KEEP IT DOWN TO JUST THE 10% I NEED TO GRADUATE THEM FASTER BUT CAN'T RISK A POOR RETENTION RATE
# SO IF I WANT TO MASTER 4000 ITEMS i MUST GET THEM ALL CORRECT AT LEAST 7X EACH.
## MY CONCLUSION IS TO USE THIS PROGRAM AND SEE WHEN IT BECOMES TOO MUCHA ND THEN AND ONLY THEN MAKE MODIFICATIONS TO THE CODE
# KEEP IT SIMPLE AND SEE IF IT WORKS FIRST


# next i can add a timestamp function to track when i studied that material so i can do more

# REMEMBER THe goal is to create something that helps me put information fast and effectively into my long term memory.