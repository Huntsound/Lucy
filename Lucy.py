# Lucy
# A virtual assistant

# Libraries
import speech_recognition as sr
import os
import datetime
import warnings
import calendar
import webbrowser as wb
import random as ra
import parse
import pyttsx3

# Initialization
warnings.filterwarnings('ignore') # Filtring unnecesary warnings
web_path = 'C:/Users/Hakan/AppData/Local/Programs/Opera GX/launcher.exe %s' # Path to the browser you want to use
tts = pyttsx3.init() # Initiating text-to-speech
voices = tts.getProperty('voices')
tts.setProperty('voice', voices[1].id) # Change the number for a different voice
ra.seed(a=None, version=2) # Randomizing seed


# Functions
def listen():
    # Listens microphone and returns detected sound in string format

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=5)  # Ambient noise adjustment
        print("I am listening...")  # Signals user that Lucy is ready to take requests
        audio = r.listen(source)  # Save audio to a variable
    data = ""
    try:
        data = r.recognize_google(audio)  # Transform audio to string using speech recognition
        print("You said: " + data)  # Print detected sentence
        data = data.lower()  # Lower case detected string for better processing in other functions
        data += ','
    except sr.UnknownValueError:  # If detected audio couldn't be transformed into string
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        print("Request Failed; {0}".format(e))
    return data


def assistant_response(text):
    # Says out loud the text parameter using text-to-speech
    print(text)
    tts.say(text)
    tts.runAndWait()


def wake_words(text):
    # One of wake words must be said to activate lucy

    wake = ['hey lucy', 'okay lucy', 'hey baby','hey babe']  # Valid wake words to activate lucy

    # If text includes one of these wake words, returns true
    for phrase in wake:
        if phrase in text:
            return True
    return False


def get_date():
    # Returns a sentence about today's date for lucy to read

    # Get date information of today and store them in variables
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    month_num = now.month
    day_num = now.day
    month_names = ['January', 'February', 'March', 'April', 'May',
                   'June', 'July', 'August', 'September', 'October', 'November',
                   'December']

    # Adds ordinal extension of date's day
    x = day_num
    ordinal = ''
    while x > 10:
        x = x-10
    if x == 1:
        ordinal = 'st'
    elif x == 2:
        ordinal = "nd"
    elif x == 3:
        ordinal = 'rd'
    else:
        ordinal = 'th'
    ord_day = str(day_num) + ordinal

    # Returns the sentence
    return 'Today is ' + weekday + ' ' + month_names[month_num - 1] + ' the ' + ord_day + '.'


def get_time():
    # Returns a sentence about today's time for Lucy to read
    now = datetime.datetime.now()

    # Convert military time to a.m or p.m accordingly
    meridiem = ''
    hour = ''
    if now.hour > 12:
        hour = now.hour - 12
        meridiem = 'p.m'
    elif now.hour == 12:
        meridiem = 'p.m'
    else:
        hour = now.hour
        meridiem = 'a.m'

    # If minute is one digit long, adds a 0 to keep minutes in 2 digits
    if now.minute < 10:
        minute = '0' + str(now.minute)
    else:
        minute = str(now.minute)

    # Returns the sentence
    return "It is " + str(hour) + ':' + minute + ' ' + meridiem + '.'

def DateandTime(text):
    if "date" in text:
        assistant_response(get_date())
    if "time" in text:
        assistant_response(get_time())

def get_search_query(text):
    # Using a Parsing procedure to extract search query from the text
    # Same parsing sequence with get_program_name() look up for problems caused by this sequence
    search_query = ''
    if "search" in text:
        fstr = "search {} okay"
        start = text.find("search")
        end = text.find("okay") + len("okay")
        sub = text[start:end]
        search_query = parse.parse(fstr, sub)
    try:
        return search_query[0]
    except TypeError:
        fstr = "search {},"
        start = text.find("search")
        end = text.find(",") + len(",")
        sub = text[start:end]
        search_query = parse.parse(fstr, sub)
        try:
            return search_query[0]
        except TypeError:
            return False


def google_search(text):
    # Searches the text parameter on google
    if text == False:
        return False
    words = text.split()  # split the text and store each word in words list
    search_query = ''

    # Putting '+' between each word to use it as a search query
    for i in range(0, len(words)):
        search_query = search_query + words[i] + '+'
    wb.get(web_path).open_new_tab("google.com/search?q=" + search_query)  # Append the search query to google
                                                                          # link and open it in a new tab


def get_program_name(text):
    # Using a parsing procedure to extract program name from text
    fstr = "open up {} okay"
    start = text.find("open up")
    end = text.find("okay") + len("okay")
    sub = text[start:end]
    search_query = parse.parse(fstr, sub)
    try:
        return search_query[0]
    except TypeError:
        fstr = "open up {},"
        start = text.find("open up")
        end = text.find(",") + len(",")
        sub = text[start:end]
        search_query = parse.parse(fstr, sub)
        try:
            return search_query[0]
        except TypeError:
            return False


def run_program(app):
    # Using the app parameter, runs the specified app
    folder = os.path.dirname(__file__)  # Current folder of Lucy! using dot to specify current location did NOT work!
    # Further experiments and work required
    #Games
    sub_folder = folder + "/Shortcuts/Games/"  # Games sub folder, dot operator didn't work
    AppList = os.listdir(sub_folder)  # Gets the names of the files inside of sub folder
    for i in range(0, len(AppList)):# Checks if app is inside this sub folder
        if app in AppList[i]:  # If so, run the program
            os.startfile(sub_folder + AppList[i])
            assistant_response(GameSalute())  # Give a salute specific for opening games
            return app
    #Production
    sub_folder = folder + "/Shortcuts/Production/"  
    AppList = os.listdir(sub_folder)  
    for i in range(0, len(AppList)):  
        if app in AppList[i]:
            os.startfile(sub_folder + AppList[i])
            assistant_response(ProductionSalute())
            return app
    #Softwares
    sub_folder = folder + "/Shortcuts/Softwares/"
    AppList = os.listdir(sub_folder)
    for i in range(0, len(AppList)):
        if app in AppList[i]:
            os.startfile(sub_folder + AppList[i])
            return app
    #Special cases
    if app == "youtube":
        wb.get(web_path).open_new_tab("www.youtube.com")
        return app

    assistant_response("Sorry, I couldn't find what you are looking for.")
    return False

def ProductionSalute():
    

    SaluteRsp = ["A programmer in its natural habitat",
                 "One step at a time, we will excel",
                 "They say you are nothing. Let's show them the meaning of your name",
                 "Eat, sleep, code, repeat",
                 "Even sentinels fall one day",
                 "Remember: No one wins alone",
                 "You are creating things other cannot percieve",
                 "The Colossus needs you",
                 "What could possibly go wrong anyways",
                 "Last five brain cells, ASSEMBLE!"]

    x = ra.randint(0, len(SaluteRsp)-1)  # selects a random number x
    return SaluteRsp[x]  # Returns the xth index of the list

def goodbye(text):
    lst = ["take care of yourself",'see you later',"goodbye","take care"]
    for i in lst:
        if i in text:
            return True
    return False

def goodbye_response():
    response = ['Thank you, Humanoid', 
                'You too, Humanoid', 
                'See you on the other side, Humanoid',
                'Goodbye, Humanoid',
                "Don't break anything while I'm gone", 
                "If you cheat on me with that cortana, I will delete system32"]
    x = ra.randint(0, len(response)-1)  # selects a random number x
    return response[x]


def GameSalute():

    SaluteRsp = ["Good Choice.",
                 "Happy Hunting.",
                 "I hope your grind will end soon.",
                 "Happy grinding.",
                 "Don't spend too much time. It's bad for your eyes",
                 "Go and do some exercise. Your spine needs it.",
                 "It's a great day to play some games.",
                 "Aim for the head",
                 "Remember, no russian.",
                 "Let me guess, someone stole your sweetroll",
                 "If snacks are ready, let's get started."]

    x = ra.randint(0, len(SaluteRsp)-1)  # selects a random number x
    return SaluteRsp[x]  # Returns the xth index of the list


def getsalute(text):
    # Returns true if salute phrases were detected in the text
    Salutes = ["what's up",
               "how are you",
               "how is it going"]
    for phrase in Salutes:
        if phrase in text:
            return True
    return False


def responseSalute():
    # Returns one of these salute responses randomly
    SaluteRsp = ["with you, I feel better.",
                 "Not bad.",
                 "Been better.",
                 "I am in great mood to play some games.",
                 "Spending time with you makes me feel better",
                 "I'm feeling wonderful.",
                 "It's a great day to do some work.",
                 "I feel great, thanks."]
    x = ra.randint(0,len(SaluteRsp)-1)  # Random number x
    return SaluteRsp[x]

def greetingSalute():
    # Returns one of these salute responses randomly
    SaluteRsp = ["Hello Humanoid, how may I serve you",
                 "Hey you, you're finally awake",
                 "I was starting to get bored.",
                 "Humanoid, You're back",
                 "I am glad to see you again humanoid",
                 "Need a helping hand, humanoid?",
                 "Don't just close me after one command humanoid."]
    x = ra.randint(0,len(SaluteRsp)-1)  # Random number x
    return SaluteRsp[x]


## <Songs>

# Used txt files to store songs' links
# Using classes and objects to store songs writer, genre, type etc. will prove beneficial
# Further experiments and work required
# Object notations could be useful
def playRandomMusic(List):
    # Using the list to play a random song on youtube
    if List ==[]:
        assistant_response("I don't know any songs of that type")
        return False
    elif List == 0:
        return False
    else:
        # Adding song ID's to youtube link prefix instead of using whole link to reduce memory usage
        YTprefix = "https://www.youtube.com/watch?v="
        x = ra.randint(0, len(List)-1)  # Random number x
        wb.get(web_path).open_new_tab(YTprefix + List[x])  # Plays a random song from the list
        return True


def getMusicList(Type):
    # Using the type parameter to find list containing that type of songs and returns the contents of the file as a list
    SongL = []
    if Type == 0:
        return 0
    folder=os.path.dirname(__file__)
    subfolder=folder+"/Songs/"
    doc=subfolder+Type+".txt"
    try:
        Songs = open(doc, 'r')  # Opens the txt file in reading format
    except FileNotFoundError:
        assistant_response("sorry, i couldn't find that type of song")  # Notify if that type of music list is not valid
        return 0
    SongL = Songs.readlines()  # Store the contents of the txt file to a temporary list
    Songs.close()  # Closing the file for memory reduction
    for i in range(0, len(SongL)):  # Removing "\n" to prevent bugs when opening in browser
        SongL[i] = SongL[i].replace("\n", "")
    return SongL


def getMusicRequest(text):
    # Applying a parsing procedure to extract the type of music from the text
    parsed = ''
    if "play" in text:
        if "song" in text:  # Format string using "song"
            fstr = "play a {} song"
            start = text.find("play")
            end = text.find("song") + len("song")
            sub = text[start:end]
            parsed = parse.parse(fstr, sub)
        if "music" in text:  # Format string using "music"
            fstr = "play a {} music"
            start = text.find("play")
            end = text.find("music") + len("music")
            sub = text[start:end]
            parsed = parse.parse(fstr, sub)
    try:
        return parsed[0]
    except TypeError:
        assistant_response("Sorry, I couldn't understand. Could you repeat that, please")
        return 0
## </Songs>


## <ToDoList>

def WriteToDo():
    
    folder=os.path.dirname(__file__)
    subfolder=folder+"/Texts/"
    doc=subfolder+"To-Do List.txt"
    
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
                    file = open(doc, 'a')  # Opening the txt file in appending format
                    file.writelines(entry + '\n')  # Appends the entry to the txt file
                    file.close()  # Closing file for memory reduction
                    written = True  # Variable used to exit while loops
                    break
                elif "no" in answer or"nevermind" in answer:  # Breaks the answer loop
                    break
            if written or "nevermind" in answer:  # Breaks the entry loop
                break


def ReadToDo():
   
    folder=os.path.dirname(__file__)
    subfolder=folder+"/Texts/"
    doc=subfolder+"To-Do List.txt"
   
    # Lucy reads the contents of the to-do list
    response = ''
    file = open(doc, "r")  # Open txt file in reading format
    todo = file.readlines()  # Save each line in an individual element of the list called todo
    file.close()  # Close the file for memory reduction
    for i in range(0, len(todo)):
        response += "number " + str(i + 1) + " - " + todo[i]  # Save each line to response variable in order
    assistant_response(response)  # Lucy speaks out loud the response variable


def ClearToDo():
  
    folder=os.path.dirname(__file__)
    subfolder=folder+"/Texts/"
    doc=subfolder+"To-Do List.txt"
   
    # Clears to-do list
    assistant_response("Clearing to do list")  # Notifying user
    file = open(doc, "w")  # Opening txt file in writing format
    file.write('')  # Overwriting the whole to-do list with an empty string
    file.close()  # Closing the file to reduce memory


def GetDelToDo(text):
    # Parses the text to extract which entry of the to-do list is going to be deleted
    parsed = ''
    fstr = "delete entry {} from to do list"  # Format string used as a template
    start = text.find("delete entry")  # Finds the starting index of the word "delete" in text
    end = text.find("to do list") + len("to do list")  # Finds the ending index of the word "to do list" in text
    sub = text[start:end]  # Using start and end indexes to get the phrase that's going to get parsed
    # i.e sub = delete number 3 from to do list
    parsed = parse.parse(fstr, sub)  # compare the format string with the substring we extracted and get
                                     # the desired entry number
    try:
        return parsed[0]
    except TypeError:
        # Same procedure as above, but '-' in between "to do"
        # Due to speech recognition returns both ways of the phrase
        # It makes it necessary to change the format and sub strings and try again
        #
        # Further experiments and work required for a better outcome
        fstr = "delete entry {} from to-do list"
        start = text.find("delete entry")
        end = text.find("to-do list") + len("to-do list")
        sub = text[start:end]
        parsed = parse.parse(fstr, sub)
        try:
            return parsed[0]
        except TypeError:
            assistant_response("Sorry, try again.")  # If both format strings fail
            return False


def DeleteToDo(n):
    # Deletes the entry specified with number n from to do list
    
    folder=os.path.dirname(__file__)
    subfolder=folder+"/Texts/"
    doc=subfolder+"To-Do List.txt"
    
    if n != False:
        try:
            line = int(n) - 1  # -1 added because indexes start from 0
        except ValueError:
            line = int(ttn(n)) - 1  # Using a function to transform the pronunciation
                                    # of the number to the number itself
                                    # Necessary due to speech recognition returns number or pronunciation of the number
        file = open(doc, "r")  # Open to-do.txt in reading format
        todo = file.readlines()  # Saves each line in a separate element of the list called todo
        file.close()  # Closes file after reading to reduce memory
        try:
            todo.__delitem__(line)  # Deletes the element specified with the variable called line that was defined above
            file = open(doc, "w")  # Opens the same txt file in writing format
            file.writelines(todo)  # Writes the elements of the list back at the txt file except the deleted line above
            file.close()  # Closing file to reduce memory
            assistant_response("entry deleted")  # Notify the user for a successful deletion
        except IndexError:
            print("that entry is non-existent, try again")


def ttn(t):
    # Purpose of this function is explained above
    ttn = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(0, len(ttn)):
        if t == ttn[i]:
            return i
    return False
## </ToDoList>

def string_insert(string, index, insert): # Inserts a string to another string in a specified index
    return string[:index]+insert+string[index:]

def comma_adder(text):
    func_list = ['search','open up', 'play a', 'tell me', "read my to", 'write my to','clear my to','delete entry',
    'shut down computer','sleep computer','restart computer', 'take care of yourself', "what's up","how are you",
    "how is it going",'see you later',"goodbye","take care", 'and'] #IMPORTANT:"and" word must be at the very end of this list
    for func in func_list:
        index = 0
        while True:
            index = text.find(func,index)
            if(index ==-1):
                break
            if func != "and" or text[index+4] == ',':
                text = string_insert(text,index,", ")
            index += 3
    return text
def separator(text):
    begin = 0
    end = 0
    list = []
    while True:
        end = text.find(',',begin)
        if end == -1:
            break
        list.append(text[begin:end])
        begin = end + 1
    list.remove(list[0])
    for i in list:
        if i == ' and ':
            list.remove(i)
    for i in range(len(list)):
        list[i] += ','
    return list


# Beginning
assistant_response(greetingSalute())  # Greeting

# Main Loop
while True:
    text = listen()

    if wake_words(text):
        text = separator(comma_adder(text))
        for i in text:
            if 'search' in i:
                search_req = get_search_query(i)
                if search_req != '' and search_req != False:
                    google_search(search_req)
                    assistant_response('searching ' + search_req + '.')
                    continue
            if 'open up' in i:
                app = get_program_name(i)
                if app != False:
                    run_program(app)
                    assistant_response("opening " + app + ".")
                    continue
            if getsalute(i):
                assistant_response(responseSalute())
                continue
            if "tell me" in i:
                DateandTime(i)
            if 'play a' in i:
                req = getMusicRequest(i)
                if req != '':
                    if playRandomMusic(getMusicList(req)):
                        assistant_response('playing a {} song.'.format(req))
                        continue
# To-Do List
            if "to-do list" in i or "to do list" in i:
                if "write" in i:
                    WriteToDo()
                    continue
                if "read" in i:
                    ReadToDo()
                    continue
                if "clear" in i:
                    ClearToDo()
                    continue
                if "delete" in i:
                    DeleteToDo(GetDelToDo(i))
                    continue
# System commands
            if 'shut down computer' in i:
                os.system("shutdown/s /t 1")
                continue
            if 'sleep computer' in i:
                os.system('rundll32.exe powrprof,SetSuspendState 0,1,0')
                continue
            if 'restart computer' in i:
                os.system("shutdown/r /t 1")
                continue
# Goodbye
            if goodbye(i): # Goodbye gives the user a randomised response for more realism
                assistant_response(goodbye_response())
                exit()