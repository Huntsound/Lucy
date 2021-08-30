from library.misc import *
from library.VoiceIO import *

## <ToDoList>

def WriteToDo(todolistdir):
    
    # Enters a loop to form a session of entry writing to prevent false-recognized entries
    assistant_response("I'm waiting for your entry")  # Notifying the user
    written = False
    while True:  # Entry loop
        entry = listen()  # Listens to user for an entry
        if entry != '':
            assistant_response(entry + "\nDo you wish to submit this entry?")  # Reads the entry and asks if it's what
                                                                               # user wants
            while True:  # Answer loop
                answer = listen()  # Listens to user for an answer to the question above
                if "yes" in answer:  # If user  accepts the entry
                    assistant_response("writing entry")  # Notifying the user
                    file = open(todolistdir, 'a')  # Opening the txt file in appending format
                    file.writelines(entry + '\n')  # Appends the entry to the txt file
                    file.close()  # Closing file for memory reduction
                    written = True  # Variable used to exit while loops
                    break
                elif "no" in answer or"nevermind" in answer:  # Breaks the answer loop
                    break
            if written or "nevermind" in answer:  # Breaks the entry loop
                break


def ReadToDo(todolistdir):
   
    # Lucy reads the contents of the to-do list
    response = ''
    file = open(todolistdir, "r")  # Open txt file in reading format
    todo = file.readlines()  # Save each line in an individual element of the list called todo
    file.close()  # Close the file for memory reduction
    for i in range(0, len(todo)):
        response += "number " + str(i + 1) + " - " + todo[i]  # Save each line to response variable in order
    assistant_response(response)  # Lucy speaks out loud the response variable


def ClearToDo(todolistdir):
   
    # Clears to-do list
    assistant_response("Clearing to do list")  # Notifying user
    file = open(todolistdir, "w")  # Opening txt file in writing format
    file.write('')  # Overwriting the whole to-do list with an empty string
    file.close()  # Closing the file to reduce memory


def GetDelToDo(text):
    # Parses the text to extract which entry of the to-do list is going to be deleted
    fstr = "delete entry number {} from to-do list"
    entry = extract_word(text, fstr)
    if entry == 0:
        fstr = "delete entry number {} from to do list"
        entry = extract_word(text, fstr)
        if entry == 0:
            assistant_response("Sorry, try again.")
            return False
    return entry

def DeleteToDo(todolistdir,entry_number):
    # Deletes the entry specified with number n from to do list
    
    if entry_number != False:
        try:
            line = int(entry_number) - 1  # -1 added because indexes start from 0
        except ValueError:
            line = int(text_to_number(entry_number)) - 1  # Using a function to transform the pronunciation
                                    # of the number to the number itself
                                    # Necessary due to speech recognition returns number or pronunciation of the number
        file = open(todolistdir, "r")  # Open to-do.txt in reading format
        todo = file.readlines()  # Saves each line in a separate element of the list called todo
        file.close()  # Closes file after reading to reduce memory
        try:
            todo.__delitem__(line)  # Deletes the element specified with the variable called line that was defined above
            file = open(todolistdir, "w")  # Opens the same txt file in writing format
            file.writelines(todo)  # Writes the elements of the list back at the txt file except the deleted line above
            file.close()  # Closing file to reduce memory
            assistant_response("entry deleted")  # Notify the user for a successful deletion
        except IndexError:
            print("that entry is non-existent, try again")
