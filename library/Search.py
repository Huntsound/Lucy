from library.misc import *
import webbrowser as wb

def get_search_query(text):
    # Using a Parsing procedure to extract search query from the text
    # Same parsing sequence with get_program_name() look up for problems caused by this sequence
    fstr = "search {} okay"
    search_query = extract_word(text, fstr)
    if search_query == 0:
        fstr = "search {},"
        search_query = extract_word(text, fstr)
        if search_query == 0:
            return False
    return search_query


def google_search(text, web_path):
    # Searches the text parameter on google
    if text == False:
        return False
    search_query = text.replace(' ','+')
    wb.get(web_path).open_new_tab("google.com/search?q=" + search_query)  # Append the search query to google
                                                                          # link and open it in a new tab
