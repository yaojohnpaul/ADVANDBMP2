#Import statements
import nltk #Natural Language Processing

#Which file to use
#   1 - metromanila
#   2 - Yolanda Meier
#   3 - Pablo Meier
#   4 - elections
fileNumber = 1

#Choose whether to show the table or the graph
#   True - table
#   False - graph
isTable = False

#Global variable containing swear words and their corresponding variations.
swear_words = [
    'fuck', 'fuk', 'fvck', 
    'shit', 'shet', 'sht', 
    'damn',
    'putangina', 'putang ina', 'tang ina', 'tangina', 'tngina', 'taena',
    'gago', 'gag0', 'g@go',
    'bobo', 'b0b0',
    'putris', 'putres',
    'kapal ng mukha', 'kapal ng muka', 'kpl ng mkha'
]

#Global variable conatining hate words and their corresponding variations.
hate_words = [
    'annoy',
    'fml', 'stfu',
    'not funny',
    'hate',
    'frustrate',
    'pathetic',
    'stupid',
    'shut up',
    'kurakot', 'kurakut', 'korakot', 'korakut',
    'pisti', 'peste', 'piste',
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
    '-.-', '-_-', '-__-'
]

#Global variable containing hateful sentence terminators and their corresponding variations.
hate_terminators = [
    '?!', '!?'
]

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
