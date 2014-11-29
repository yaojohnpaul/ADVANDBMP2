#Import statements
import csv #CSV Library
import algo #Our tweet evaluation algo python file
import graphgui #Our gui classes
import datetime #Library for date and time

class GraphGen:
    def __init__(self, master, number):
        if number == 1:
            self.create_graph(master, 'metromanila.csv',
                                   [2, 3], 2, True)
        elif number == 2:
            self.create_graph(master, 'Yolanda Meier.csv',
                                   [1, 0], 1, False)
        elif number == 3:
            self.create_graph(master, 'Pablo Meier.csv',
                                   [2, 0], 2, True)
        elif number == 4:
            self.create_graph(master, 'filtered-may1-onwards.csv',
                                   [2, 3], 2, True)
    
    #Function for collecting numerical data on frustrated tweets from a .csv file.
    def getTweetData(self, csv_reader, col_list, check_col, isLongDate):
        tweet_list = []
        tweet_date = []
        data_date = []
        data_count = []
        tweet_data = [] #Format: Date, Number of Frustrated Tweets
        
        isHeader = True #Variable to check if the row being read is a header
        for row in csv_reader: #For every row in the .csv file
            if isHeader == True: #If we are checking the first row
                isHeader = False
            else: #Get tweet list and date
                if algo.evaluateTweet(row[check_col]): #If tweet is a frustrated tweet, add to list.
                    tweet_list.append(row[col_list[0]])
                    tweet_date.append(row[col_list[1]])

        #Populate data_date and data_count
        for ctr in range(len(tweet_date)):
            temp_date = tweet_date[ctr]
            temp_val = ""
            #Date parsing found at:
            #http://stackoverflow.com/questions/4053924/python-parse-date-format-ignore-parts-of-string
            if isLongDate == True:
                temp_val = temp_date[4:11] + temp_date[len(temp_date)-4:len(temp_date)]
                temp_date = str(datetime.datetime.strptime(temp_val, '%b %d %Y'))
                temp_date = temp_date[:temp_date.find(" 00:00:00")]
            elif isLongDate == False:
                temp_val = temp_date[:temp_date.find(" ")]
                temp_date = str(datetime.datetime.strptime(temp_val, '%m/%d/%Y'))
                temp_date = temp_date[:temp_date.find(" 00:00:00")]
                
            found_date = False
            for check_ctr in range(len(data_date)):
                if temp_date == data_date[check_ctr]:
                   data_count[check_ctr] += 1
                   found_date = True
                   break
            if found_date == False:
                data_date.append(temp_date)
                data_count.append(1)
        
        #Populate tweet_data
        for ctr in range(len(data_date)):
            tweet_data.append(data_date[ctr])
            tweet_data.append(data_count[ctr])
        
        return tweet_data   

    #Create the table based on filename.csv
    def create_graph(self, master, filename, columns, col_eval, isLongDate):
        CSVfile = open(filename, 'r', encoding = 'latin1') #Open the filename.csv file
        Reader = csv.reader(CSVfile, dialect = 'excel') #Set filename.csv to a reader variable

        #Retrieve list of frustrated tweets from metromanila.csv
        tweet_data = self.getTweetData(Reader, columns, col_eval, isLongDate)

        CSVfile.close() #Close the filename.csv file

        #Create tweet table for GUI
        tweet_graph = graphgui.tweetGraph(master, tweet_data, filename + ' Frustrated Tweet Counts')

        #Set GUI element
        gui = graphgui.GraphGUI(master, tweet_graph)
