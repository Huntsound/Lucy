from library.Answers import *
import random as ra
import parse

func_list = ['search','open up', 'play a', 'tell me', "read my to", 'write my to','clear my to','delete entry',
             'shut down computer','sleep computer','restart computer']+goodbye+salute+["and"]
              #IMPORTANT:"and" word must be at the very end of this list

def pickRandom(List):
    # Returns one of these List members randomly
    try:
        return List[ra.randint(0,len(List)-1)]
    except IndexError:
        return False

def extract_word(text, fstring):
    start_phrase = fstring[:fstring.find("{")]
    start = text.find(start_phrase)
    end_phrase = fstring[fstring.find("}")+1:]
    end = text.find(end_phrase) + len(end_phrase)
    sub = text[start:end]
    word = parse.parse(fstring, sub)
    try:
        return word[0]
    except TypeError:
        return 0

def text_to_number(t):
    # Purpose of this function is explained above
    ttn = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(0, len(ttn)):
        if t == ttn[i]:
            return i
    return False

def string_insert(string, index, insert): # Inserts a string to another string in a specified index
    return string[:index]+insert+string[index:]

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

def list_in_text(List, text):
    for phrase in List:
        if phrase in text:
            return True
    return False

def comma_adder(func_list,text):
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