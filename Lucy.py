import speech_recognition as sr
import os
import datetime
import warnings
import calendar
import webbrowser as wb
import random as ra
import parse
import time
import pyttsx3
warnings.filterwarnings('ignore')
web_path = 'C:/Users/Hakan/AppData/Local/Programs/Opera GX/launcher.exe %s'
s_actv = True
p_actv = False

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=5)
        print("I am listening...")
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said: " + data)
        data = data.lower()
    except sr.UnknownValueError:
        print("Google Speech Recognition did not understand audio")
    except sr.RequestError as e:
        print("Request Failed; {0}".format(e))
    return data

def assistant_response(text):
    print(text)
    #text = "client=" + text
    tts = pyttsx3.init()
    voices = tts.getProperty('voices')
    tts.setProperty('voice', voices[1].id)
    tts.say(text)
    tts.runAndWait()

def wake_words(text):
    wake = ['hey lucy', 'okay lucy']
    text = text.lower()

    for phrase in wake:
        if phrase in text:
            return True
        else:
            return False

def get_date():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    month_num = now.month
    day_num = now.day
    month_names = ['January', 'February', 'March', 'April', 'May',
                   'June', 'July', 'August', 'September', 'October', 'November',
                   'December']
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
    return 'Today is ' + weekday + ' ' + month_names[month_num - 1] + ' the ' + ord_day + '.'

def get_time():
    now = datetime.datetime.now()
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

    if now.minute < 10:
        minute = '0' + str(now.minute)
    else:
        minute = str(now.minute)
    return "It is " + str(hour) + ':' + minute + ' ' + meridiem + ' .'

def get_search_query(text):
    words = text.split()
    search_query = ''
    limit = 5
    b = 0
    for i in range(0, len(words)):
        a = i + 1
        if words[i] == "search":
                while b < limit and a != len(words):
                    if words[a] != "okay":
                        search_query = search_query + words[a] + ' '
                        a = a + 1
                        b = b + 1
                    else:
                        break
    return search_query

def google_search(text):
    text = text.lower()
    words = text.split()
    search_query = ''
    for i in range(0, len(words)):
        search_query = search_query + words[i] + '+'
    wb.get(web_path).open_new_tab("google.com/search?q=" + search_query)

def GameSalute():
    SaluteRsp = ["Good Choice.",
                 "Happy Hunting.",
                 "I hope your grind will end soon.",
                 "Happy grinding.",
                 "Don't spend too much time. It's bad for your eyes",
                 "Go and do some exercise. Your spine needs it.",
                 "It's a great day to play some games.",
                 "If snacks are ready, let's get started."]
    x = ra.randint(0, len(SaluteRsp))
    return SaluteRsp[x]

def run_program(text):
    text = text.lower()
    words = text.split()
    app = ''
    for i in range(0, len(words)):
        if words[i] == "open" and words[i + 1] == "up":
            if words[i + 2] == words[len(words) - 1]:
                app = words[i + 2]
            else:
                app = words[i + 2] + ' ' + words[i + 3]

    folder = os.path.dirname(__file__)
    #Games
    sub_folder = folder + "/Shortcuts/Games/"
    AppList = os.listdir(sub_folder)
    for i in range(0, len(AppList)):
        if app in AppList[i]:
            os.startfile(sub_folder + AppList[i])
            assistant_response(GameSalute())
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

def goodbye(text):
    text = text.lower()
    return "goodbye" in text

def getsalute(text):
    text = text.lower()
    if "what's up" in text:
        return True
    elif "how are you" in text:
        return True
    elif "how is it going" in text:
        return True
    return False

def responseSalute():
    SaluteRsp = ["Good.",
                 "Not bad.",
                 "Been better.",
                 "Excellent.",
                 "Like shit.",
                 "I'm feeling wonderful.",
                 "It's a great day to do some work.",
                 "I feel better, thanks."]
    x = ra.randint(0,len(SaluteRsp))
    return SaluteRsp[x]

def playRandomMusic(List):
    if List != 0:
        YTprefix = "https://www.youtube.com/watch?v="
        try:
            x = ra.randint(0, len(List))
            wb.get(web_path).open_new_tab(YTprefix + List[x])
        except IndexError:
            assistant_response("Sorry, can you say that again.")

def getMusicList(Type):
    SongL = []
    try:
        Songs = open("./Songs/" + Type + ".txt", 'r')
    except FileNotFoundError:
        assistant_response("sorry, i couldn't find that type of song")
        return 0
    temp = Songs.readlines()
    Songs.close()
    for i in range(0, len(temp)):
        temp[i] = temp[i].replace("\n", "")
        SongL.append(temp[i])
    return SongL

def getMusicRequest(text):
    text = text.lower()
    parsed = ''
    if "play" in text:
        if "song" in text:
            fstr = "play a {} song"
            start = text.find("play")
            end = text.find("song") + len("song")
            sub = text[start:end]
            parsed = parse.parse(fstr, sub)
        if "music" in text:
            fstr = "play a {} music"
            start = text.find("play")
            end = text.find("music") + len("music")
            sub = text[start:end]
            parsed = parse.parse(fstr, sub)
    return parsed[0]

def WriteToDo():
    assistant_response("I'm waiting for your entry")
    written = False
    while True:
        entry = listen()
        if entry != '':
            assistant_response(entry + "\nDo you wish to submit this entry?")
            time.sleep(5)
            while True:
                answer = listen()
                if answer == "yes i do":
                    assistant_response("writing entry")
                    file = open("./Texts/To-Do.txt", 'a')
                    file.writelines(entry + '\n')
                    file.close()
                    written = True
                    break
                elif answer == "no i don't":
                    break
            if written:
                break

def ReadToDo():
    response = ''
    file = open("./Texts/To-Do.txt")
    todo = file.readlines()
    file.close()
    for i in range(0, len(todo)):
        response += "number " + str(i + 1) + " - " + todo[i]
    assistant_response(response)

def ClearToDo():
    assistant_response("Clearing to do list")
    file = open("./Texts/To-Do.txt", "w")
    file.write('')
    file.close()

def GetDelToDo(text):
    parsed = ''
    fstr = "delete {} from to do list"
    start = text.find("delete")
    end = text.find("to do list") + len("to do list")
    sub = text[start:end]
    parsed = parse.parse(fstr,sub)
    try:
        return parsed[0]
    except TypeError:
        fstr = "delete {} from to-do list"
        start = text.find("delete")
        end = text.find("to-do list") + len("to-do list")
        sub = text[start:end]
        parsed = parse.parse(fstr, sub)
        try:
            return parsed[0]
        except TypeError:
            assistant_response("Sorry, try again.")
            return False

def DeleteToDo(n):

    if n != False:
        try:
            line = int(n) - 1
        except ValueError:
            line = int(ttn(n)) - 1
        file = open("./Texts/To-Do.txt", "r")
        todo = file.readlines()
        file.close()
        try:
            todo.__delitem__(line)
            file = open("./Texts/To-Do.txt", "w")
            file.writelines(todo)
            file.close()
            assistant_response("entry deleted")
        except IndexError:
            print("that entry is non-existent, try again")

def ttn(t):
    ttn = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(0, len(ttn)):
        if t == ttn[i]:
            return i
    return False

assistant_response('Hello Humanoid, How may I serve you')

while True:
    response = ''
    text = ''
    if s_actv:
        text = listen()
    if p_actv:
        file = open('./Texts/Phone.txt', 'r')
        lines = file.readlines()
        file.close()

        for i in range(0, len(lines)):
            lines[i] = lines[i].strip('\n')
            text = text + lines[i]

        file = open('./Texts/Phone.txt', 'w')
        file.write('')
        file.close()



    if wake_words(text):
        if getsalute(text):
            response = response + responseSalute()
        if 'date' in text:
            response = response + get_date()
        if 'time' in text:
            response = response + get_time()
        if get_search_query(text) != '':
            google_search(get_search_query(text))
            response = response + 'searching ' + get_search_query(text) + '.'
        if 'open up' in text:
            app = run_program(text)
            if app != False:
                response = response + 'opening ' + app + ' .'
        if 'play' in text:
            req = getMusicRequest(text)
            if req != '':
                playRandomMusic(getMusicList(req))
                response = response + 'playing a {} song. '.format(req)
#To-Do List
        if "to-do list" in text or "to do list" in text:
            if "write" in text:
                WriteToDo()
            if "read" in text:
                ReadToDo()
            if "clear" in text:
                ClearToDo()
            if "delete" in text:
                DeleteToDo(GetDelToDo(text))
#System commands
        if 'shut down computer' in text:
            os.system("shutdown/s /t 1")
#        if 'sleep computer' in text:
#            os.system('rundll32.exe powrprof,SetSuspendState 0,1,0')
        if 'restart computer' in text:
            os.system("shutdown/r /t 1")
        if goodbye(text):
            s_actv = False
            p_actv = False
            response = response + "Goodbye, Humanoid"
#Activation and deactivation sequence
        if 'disable speech activation' in text and s_actv:
            s_actv = False
            response = response + 'disabling speech activation'

        elif 'disable speech activation' in text and s_actv == False:
            response = response + 'Speech activation is already disabled'

        if 'enable speech activation' in text and s_actv == False:
            s_actv = True
            response = response + 'enabling speech activation'

        elif 'enable speech activation' in text and s_actv:
            response = response + 'Speech activation is already enabled'

        if 'disable phone activation' in text and p_actv:
            p_actv = False
            file = open('./Texts/Lucy.txt', 'w')
            file.write('disable phone activation')
            file.close()
            response = response + 'disabling phone activation'

        elif 'disable phone activation' in text and p_actv == False:
            response = response + 'Phone activation is already disabled'

        if 'enable phone activation' in text and p_actv == False:
            p_actv = True
            os.startfile("server.py")
            response = response + 'enabling phone activation'

        elif 'enable phone activation' in text and p_actv:
            response = response + 'Phone activation is already enabled'
        if response != '':
            assistant_response(response)
        if s_actv == False and p_actv == False:
            break
