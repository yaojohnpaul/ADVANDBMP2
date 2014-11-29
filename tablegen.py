#Import statements
import csv #CSV Library
import algo #Our tweet evaluation algo python file
import tablegui #Our gui classes

class TableGen:
    def __init__(self, master, number):
        if number == 1:
            self.create_table(master, 'metromanila.csv',
                                   [2, 3], 2,
                                   ['Tweet', 'Date'])
        elif number == 2:
            self.create_table(master, 'Yolanda Meier.csv',
                                   [1, 0], 1,
                                   ['Tweet', 'Date'])
        elif number == 3:
            self.create_table(master, 'Pablo Meier.csv',
                                   [2, 0], 2,
                                   ['Tweet', 'Date'])
        elif number == 4:
            self.create_table(master, 'filtered-may1-onwards.csv',
                                   [2, 3], 2,
                                   ['Tweet', 'Date'])
    
    #Function for collecting frustrated tweets from a .csv file.
    def getTweets(self, csv_reader, col_list, check_col):
        tweet_list = []
        isHeader = True #Variable to check if the row being read is a header
        for row in csv_reader: #For every row in the .csv file
            if isHeader == True: #If we are checking the first row
                isHeader = False
            else: #Print out the tweet and the date
                if algo.evaluateTweet(row[check_col]): #If tweet is a frustrated tweet, add to list.
                    for ctr in col_list:
                        tweet_list.append(row[ctr])
        return tweet_list   

    #Create the table based on filename.csv
    def create_table(self, master, filename, columns, col_eval, col_headers):
        CSVfile = open(filename, 'r', encoding = 'latin1') #Open the filename.csv file
        Reader = csv.reader(CSVfile, dialect = 'excel') #Set filename.csv to a reader variable

        #Retrieve list of frustrated tweets from metromanila.csv
        tweet_list = self.getTweets(Reader, columns, col_eval)

        CSVfile.close() #Close the filename.csv file

        #Create tweet table for GUI
        tweet_table = tablegui.tweetTable(master, tweet_list, len(columns))
        for i, col_header in enumerate(col_headers):
            tweet_table.setHeader(i, col_header)

        #Set GUI element
        gui = tablegui.TableGUI(master, tweet_table)
