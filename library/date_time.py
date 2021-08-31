from library.VoiceIO import assistant_response
import datetime
import calendar

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