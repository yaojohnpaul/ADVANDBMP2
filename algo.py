#Import statements
import nltk #Natural Language Processing

#Which file to use
#   1 - metromanila
#   2 - Yolanda Meier
#   3 - Pablo Meier
#   4 - elections
#   5 - All yolanda data
fileNumber = 1

#Global variable containing swear words and their corresponding variations.
swear_words = [
    'fuck', 'fuk', 'fvck', 
    'shit', 'shet',
    'damn',
    'putangina', 'putang ina', 'tang ina', 'tangina', 'tngina', 'taena',
    'gago', 'gag0', 'g@go',
    ' bobo ', 'b0b0',
    'putris', 'putres',
    'kapal ng mukha', 'kapal ng muka', 'kpl ng mkha',
    'kupal',
    'dumbass'
]

#Global variable conatining hate words and their corresponding variations.
hate_words = [
    'annoy',
    'stfu',
    'not funny',
    'hate',
    'frustrate',
    'pathetic',
    'stupid',
    'shut up',
    'kurakot', 'kurakut', 'korakot', 'korakut',
    'peste', 'piste',
    'grr',
    'bwisit', 'bwiset',
    'konsensya',
    'diyos ko', 'jusko', 'jus ko', 'diyosko',
    'hayst', 'hayyst',
    'grabe'
]

#Global variable containing hateful emoticons and their corresponding variations.
hate_emoticons = [
    '>:(', 'D:<', '>:-(', 'D-:<', '>: (', 'D :<',
    '-.-', '-_-', '-__-', '>.<', '>_<'
]

#Global variable containing hateful sentence terminators and their corresponding variations.
hate_terminators = [
    '?!', '!?'
]

ff = open('functionwords/fil-function-words.txt', 'r')
fil_function = ff.read().split()

ef = open('functionwords/eng-function-words.txt', 'r')
eng_function = ef.read().split()

#Function to evaluate a tweet with regards to
#whether it is frustrated or not.
def evaluateTweet(tweet):
    for swear in swear_words: #For all the swear words
        if swear in tweet: #Check if the tweet contains a swear word
            return True
    for hate in hate_words: #For all the hate words
        if hate in tweet: #Check if the tweet contains a hate word
            return True
    for hate in hate_emoticons: #For all the hate emoticons
        if hate in tweet: #Check if the tweet contains a hate emoticon
            return True
    for hate in hate_terminators: #For all the hate terminators
        if hate in tweet: #Check if the tweet contains a hate terminators
            return True
    return False

#Process the word to either:
#1. remove special characters
#2. only get significant words (return "" if insignificant)
def processWord(word):
    pWord = word

    #For special words like &quot;
    if pWord[0] == '&' and pWord[len(pWord)-1] == ';':
        return ""

    #Remove special characters
    pWord = ''.join(s for s in word if s.isalnum())

    if "haha" in pWord.lower():
        return ""

    #Do not consider if it is a function word
    if pWord.upper() in eng_function:
        return ""
    if pWord.lower() in fil_function:
        return ""

    #If remaining word is 3 characters or below
    if len(pWord) <= 3:
        return ""
    else:
        return pWord
