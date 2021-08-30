from library.misc import *
from library.Responses import *
from library.VoiceIO import *
import webbrowser as wb
import os
def get_program_name(text):
    # Using a parsing procedure to extract program name from text
    fstr = "open up {} okay"
    program_name = extract_word(text, fstr)
    if program_name == 0:
        fstr = "open up {},"
        program_name = extract_word(text, fstr)
        if program_name == 0:
            return False
    return program_name

def find_open_app(dir, app):
    AppList = os.listdir(dir)
    app = app.strip()
    if AppList == []:
        return False
    for i in range(0, len(AppList)):
        if app in AppList[i]:
            os.startfile(dir + AppList[i])
            return True
    return False

def run_program(web_path,programdir,app):
    # Using the app parameter, runs the specified app
    #Games
    sub_folder = programdir + "Games/"  # Games sub folder, dot operator didn't work
    if find_open_app(sub_folder, app):
        assistant_response(pickRandom(games))
        return app
    #Production
    sub_folder = programdir + "Production/"  
    if find_open_app(sub_folder, app):
        assistant_response(pickRandom(production))
        return app
    #Softwares
    sub_folder = programdir + "Softwares/"
    if find_open_app(sub_folder, app):
        return app
    #Special cases
    if app == "youtube":
        wb.get(web_path).open_new_tab("www.youtube.com")
        return app
    assistant_response("Sorry, I couldn't find what you are looking for.")
    return False
