# Lucy
# A virtual assistant

# Libraries
from library.Responses import *
from library.misc import *
from library.VoiceIO import *
from library.Search import *
from library.To_Do import *
from library.Music import *
from library.Program import *
from library.date_time import *
from library.Answers import *
import os
import warnings
import random as ra 

# Initialization
warnings.filterwarnings('ignore') # Filtring unnecesary warnings
web_path = 'C:/Users/Hakan/AppData/Local/Programs/Opera GX/launcher.exe %s' # Path to the browser you want to use
ra.seed(a=None, version=2) # Randomizing seed
folder=os.path.dirname(__file__) # Current directary of this file
todolist = folder + "/Texts/To-Do List.txt"
songs = folder + "/Songs/"
programs = folder + "/Shortcuts/"

# Beginning
assistant_response(pickRandom(greeting))  # Greeting

# Main Loop
while True:
    text = listen()

    if list_in_text(wake_words,text):
        text = separator(comma_adder(func_list,text))
        for i in text:
            if 'search' in i:
                search_req = get_search_query(i)
                if search_req != '' and search_req != False:
                    google_search(search_req, web_path)
                    assistant_response('searching ' + search_req + '.')
                    continue
            if 'open up' in i:
                app = get_program_name(i)
                if app != False:
                    if run_program(web_path,programs,app) != False:
                        assistant_response("opening " + app + ".")
                        continue
            if list_in_text(salute,i):
                assistant_response(pickRandom(salute_response))
                continue
            if "tell me" in i:
                DateandTime(i)
            if 'play a' in i:
                req = getMusicRequest(i)
                if req != '':
                    if playRandomMusic(web_path,getMusicList(songs,req)):
                        assistant_response('playing a {} song.'.format(req))
                        continue
# To-Do List
            if "to-do list" in i or "to do list" in i:
                if "write" in i:
                    WriteToDo(todolist)
                    continue
                if "read" in i:
                    ReadToDo(todolist)
                    continue
                if "clear" in i:
                    ClearToDo(todolist)
                    continue
                if "delete" in i:
                    DeleteToDo(todolist,GetDelToDo(i))
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
            if list_in_text(goodbye,i): # Goodbye gives the user a randomised response for more realism
                assistant_response(pickRandom(goodbye_response))
                exit()