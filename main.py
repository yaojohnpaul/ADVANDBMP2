#Import statements
import nltk #Natural Language Processing
import csv #CSV Library
#GUI
from tkinter import *

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
    '?!', '? !', '! ?', '!?'
]


#Create the global GUI root widget
root = Tk()

#Class for the GUI
class GUI:
    def __init__(self, master, table):
        frame = table
        frame.pack(side = "top", fill = "x")

#GUI Class for Tweets Table
#Based on reply from:
#http://stackoverflow.com/questions/11047803/creating-a-table-look-a-like-tkinter 
class tweetTable(Frame):
    #Constructor
    def __init__(self, master, entries, col_no):
        #GUI Configuration found at:
        #http://stackoverflow.com/questions/3085696/adding-a-scrollbar-to-a-grid-of-widgets-in-tkinter

        #Super class - Frame constructor
        Frame.__init__(self, master, background = "black")

        #GUI Configuration
        self.canvas = Canvas(master, bg = "black", height = 600, width = 1134)
        self.frame = Frame(self.canvas, bg = "black")
        self.scrollbar = Scrollbar(master, orient = "vertical", command = self.canvas.yview)
        self.canvas.configure(yscrollcommand = self.scrollbar.set)

        self.scrollbar.pack(side = RIGHT, fill = Y)
        self.canvas.pack(side = LEFT, fill = "both", expand = True)
        self.canvas.create_window((0,0), window = self.frame, anchor = "nw")
        self.frame.bind("<Configure>", self.configureFrame)

        #MouseWheel Binding found at:
        #http://stackoverflow.com/questions/17355902/python-tkinter-binding-mousewheel-to-scrollbar
        self.canvas.bind_all("<MouseWheel>", self.mouseWheel)

        #Add information to table
        self.populateTable(entries, col_no)

    #Populate table with information from entries
    def populateTable(self, entries, col_no):
        self.frame.elements = [] #Contents of this GUI element
        entry_length = len(entries) #Number of entries for the table
        cell_width = int(160/col_no) #Width of cell
        cell_wrap_width = int(1134/col_no) #Wrap width

        #Initial entry: Header
        header_entry = []
        #Iterate col_no times
        for colctr in range(col_no):
            #Add a cell
            label = Label(self.frame, text = "Column " + str(colctr), borderwidth = 0, width = cell_width, wraplength = cell_wrap_width, bg = "black", fg = "white")
            label.grid(row = 0, column = colctr, sticky = "nsew", padx = 2, pady = 2)
            header_entry.append(label)
        #Add the column header to the table
        self.frame.elements.append(header_entry)

        #Iterate entry_length/col_no times.
        #Since entries is a list and we want to make it a table, 
        #we divide the number of entries by col_no in order to add
        #to the table by row and column, not linearly. 
        for ctr in range(int(entry_length/col_no)):
            #Current row
            current_entry = []
            #Iterate col_no times
            for colctr in range(col_no):
                #Add a cell to the row
                label = Label(self.frame, text = entries[colctr + (ctr * col_no)], borderwidth = 0, width = cell_width,
                              wraplength = cell_wrap_width, bg = "white")
                label.grid(row = ctr + 1, column = colctr, sticky = "nsew", padx = 1, pady = 1)
                current_entry.append(label)
            #Add the row to the table
            self.frame.elements.append(current_entry)

    #Function for setting the column headers
    def setHeader(self, column, value):
        element = self.frame.elements[0][column]
        element.configure(text = value)

    #Configure the frame based on scroll area
    def configureFrame(self, event):
        self.canvas.configure(scrollregion = self.canvas.bbox("all"))

    #Configure the mouse wheel to the scroll bar
    def mouseWheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

#Function for collecting frustrated tweets from a .csv file.
def printTweets(csv_reader, col_list, check_col):
    tweet_list = []
    isHeader = True #Variable to check if the row being read is a header
    for row in csv_reader: #For every row in the .csv file
        if isHeader == True: #If we are checking the first row
            isHeader = False
        else: #Print out the tweet and the date
            if evaluateTweet(row[check_col]): #If tweet is a frustrated tweet, add to list.
                for ctr in col_list:
                    tweet_list.append(row[ctr])
    return tweet_list

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

#Main Function
def mainFunction():
    #table_metromanila()
    #table_yolandameier()
    table_pablomeier()
    #table_elections()

    #Display the GUI
    root.wm_title("ADVANDB MP2")
    root.mainloop()

#Metro Manila CSV Reading
def table_metromanila():
    CSVfile = open('metromanila.csv', 'r', encoding = 'utf8') #Open the metromanila.csv file
    Reader = csv.reader(CSVfile, delimiter = ',') #Set metromanila.csv to a reader variable

    #Retrieve list of frustrated tweets from metromanila.csv
    tweet_list = printTweets(Reader, [2, 3], 2)

    CSVfile.close() #Close the metromanila.csv file

    #Create tweet table for GUI
    tweet_table = tweetTable(root, tweet_list, 2)
    tweet_table.setHeader(0, 'Tweet')
    tweet_table.setHeader(1, 'Date')

    #Set GUI element
    gui = GUI(root, tweet_table)

#Yolanda Meier CSV Reading
def table_yolandameier():
    CSVfile = open('Yolanda Meier.csv', 'r', encoding = 'utf8') #Open the Yolanda Meier.csv file
    Reader = csv.reader(CSVfile, delimiter = ',') #Set Yolanda Meier.csv to a reader variable

    #Retrieve list of frustrated tweets from Yolanda Meier.csv
    tweet_list = printTweets(Reader, [1, 0], 1)

    CSVfile.close() #Close the Yolanda Meier.csv file

    #Create tweet table for GUI
    tweet_table = tweetTable(root, tweet_list, 2)
    tweet_table.setHeader(0, 'Tweet')
    tweet_table.setHeader(1, 'Date')

    #Set GUI element
    gui = GUI(root, tweet_table)

#Yolanda Meier CSV Reading
def table_pablomeier():
    CSVfile = open('Pablo Meier.csv', 'r', encoding = 'utf8') #Open the Pablo Meier.csv file
    Reader = csv.reader(CSVfile, delimiter = ',') #Set Pablo Meier.csv to a reader variable

    #Retrieve list of frustrated tweets from Pablo Meier.csv
    tweet_list = printTweets(Reader, [2, 0], 2)

    CSVfile.close() #Close the Pablo Meier.csv file

    #Create tweet table for GUI
    tweet_table = tweetTable(root, tweet_list, 2)
    tweet_table.setHeader(0, 'Tweet')
    tweet_table.setHeader(1, 'Date')

    #Set GUI element
    gui = GUI(root, tweet_table)

#Yolanda Meier CSV Reading
def table_elections():
    CSVfile = open('filtered-may1-onwards.csv', 'r', encoding = 'utf8') #Open the filtered-may1-onwards.csv file
    Reader = csv.reader(CSVfile, delimiter = ',') #Set filtered-may1-onwards.csv to a reader variable

    #Retrieve list of frustrated tweets from filtered-may1-onwards.csv
    tweet_list = printTweets(Reader, [2, 3], 2)

    CSVfile.close() #Close the filtered-may1-onwards.csv file

    #Create tweet table for GUI
    tweet_table = tweetTable(root, tweet_list, 2)
    tweet_table.setHeader(0, 'Tweet')
    tweet_table.setHeader(1, 'Date')

    #Set GUI element
    gui = GUI(root, tweet_table)

#Call the main function
mainFunction()
