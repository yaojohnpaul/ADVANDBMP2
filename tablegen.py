#Import statements
import csv #CSV Library
import algo #Our tweet evaluation algo python file
import tablegui #Our gui classes
import datetime #Date and time

class TableGen:
    def __init__(self, master, number):
        if number == 1:
            self.create_table(master, 'metromanila.csv',
                                   [2, 3], 2,
                                   ['Tweet', 'Date'], True)
        elif number == 2:
            self.create_table(master, 'Yolanda Meier.csv',
                                   [1, 0], 1,
                                   ['Tweet', 'Date'], False)
        elif number == 3:
            self.create_table(master, 'Pablo Meier.csv',
                                   [2, 0], 2,
                                   ['Tweet', 'Date'], True)
        elif number == 4:
            self.create_table(master, 'filtered-may1-onwards.csv',
                                   [2, 3], 2,
                                   ['Tweet', 'Date'], True)
        elif number == 5:
            self.create_yolanda_table(master, ['Tweet', 'Date'])
    
    #Function for collecting frustrated tweets from a .csv file.
    def getTweets(self, csv_reader, col_list, check_col, isLongDate):
        tweet_list = []
        isHeader = True #Variable to check if the row being read is a header
        for row in csv_reader: #For every row in the .csv file
            if isHeader == True: #If we are checking the first row
                isHeader = False
            else: #Print out the tweet and the date
                if algo.evaluateTweet(row[check_col]): #If tweet is a frustrated tweet, add to list.
                    tweet_list.append(row[col_list[0]])
                    temp_date = row[col_list[1]]
                    temp_val = ""
                    #Date parsing found at:
                    #http://stackoverflow.com/questions/4053924/python-parse-date-format-ignore-parts-of-string
                    if isLongDate == True:
                        temp_val = temp_date[4:11] + temp_date[len(temp_date)-5:len(temp_date)]
                        if temp_val[0] == ' ':
                            temp_val = temp_val[1:]
                        temp_date = str(datetime.datetime.strptime(temp_val, '%b %d %Y'))
                        temp_date = temp_date[:temp_date.find(" 00:00:00")]
                    elif isLongDate == False:
                        temp_val = temp_date[:temp_date.find(" ")]
                        temp_date = str(datetime.datetime.strptime(temp_val, '%m/%d/%y'))
                        temp_date = temp_date[:temp_date.find(" 00:00:00")]
                    tweet_list.append(temp_date)
        return tweet_list   

    #Get data based on file name
    def getDataFromFile(self, filename, columns, col_eval, isLongDate):
        CSVfile = open(filename, 'r', encoding = 'latin1') #Open the filename.csv file
        Reader = csv.reader(CSVfile, dialect = 'excel') #Set filename.csv to a reader variable

        #Retrieve list of frustrated tweets from filename.csv
        tweet_list = self.getTweets(Reader, columns, col_eval, isLongDate)

        CSVfile.close() #Close the filename.csv file

        return tweet_list

    #Create the table based on filename.csv
    def create_table(self, master, filename, columns, col_eval, col_headers, isLongDate):
        #Create tweet table for GUI
        tweet_table = tablegui.tweetTable(master,
                                          self.getDataFromFile(filename, columns, col_eval, isLongDate),
                                          len(columns))
        for i, col_header in enumerate(col_headers):
            tweet_table.setHeader(i, col_header)

        #Set GUI element
        gui = tablegui.TableGUI(master, tweet_table)

    #Create the table based on all Yolanda.csvs
    def create_yolanda_table(self, master, col_headers):
        tweet_list = []

        tweet_list = self.getDataFromFile('Pablo Meier.csv', [2, 0], 2, True)
        tweet_list = tweet_list + self.getDataFromFile('Yolanda Meier.csv', [1, 0], 1, False)
        tweet_list = tweet_list + self.getDataFromFile('metromanila.csv', [2, 3], 2, True)
        
        #Create tweet table for GUI
        tweet_table = tablegui.tweetTable(master,
                                          tweet_list,
                                          2)
        for i, col_header in enumerate(col_headers):
            tweet_table.setHeader(i, col_header)

        #Set GUI element
        gui = tablegui.TableGUI(master, tweet_table)
