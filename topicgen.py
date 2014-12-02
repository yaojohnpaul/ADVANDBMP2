#Import statements
import csv #CSV Library
import algo #Our tweet evaluation algo python file
import topicgui #Our gui classes
import datetime #Library for date and time

class TopicGen:
    def __init__(self, master, number):
        if number == 1:
            self.create_topics(master, 'metromanila.csv',
                                   [2, 3], 2, True)
        elif number == 2:
            self.create_topics(master, 'Yolanda Meier.csv',
                                   [1, 0], 1, False)
        elif number == 3:
            self.create_topics(master, 'Pablo Meier.csv',
                                   [2, 0], 2, True)
        elif number == 4:
            self.create_topics(master, 'filtered-may1-onwards.csv',
                                   [2, 3], 2, True)
        elif number == 5:
            self.create_yolanda_topics(master)
    
    #Function for collecting the topics of the frustrated tweets from a .csv file.
    def getTweetData(self, csv_reader, col_list, check_col, isLongDate):
        tweet_list = []
        tweet_date = []
        data_date = []
        data_topic = []
        tweet_data = [] #Format: Date, Top Topics
        
        isHeader = True #Variable to check if the row being read is a header
        for row in csv_reader: #For every row in the .csv file
            if isHeader == True: #If we are checking the first row
                isHeader = False
            else: #Get tweet list and date
                if algo.evaluateTweet(row[check_col]): #If tweet is a frustrated tweet, add to list.
                    tweet_list.append(row[col_list[0]])
                    tweet_date.append(row[col_list[1]])

        temp_topics = [[], []]
        #Populate data_date and data_topic
        for ctr in range(len(tweet_date)):
            temp_date = tweet_date[ctr]
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

            if (not(temp_date in data_date) and ctr != 0) or ctr == len(tweet_date)-1:
                temp_topics_list = []
                top_five = [-1, -1, -1, -1, -1]
                top_five_index = [0, 0, 0, 0, 0]
                for list_ctr in range(len(temp_topics[1])):
                    for list_ctr_2 in range(len(top_five)):
                        if temp_topics[1][list_ctr] > top_five[list_ctr_2] or top_five[list_ctr_2] == -1:
                            top_five[list_ctr_2] = temp_topics[1][list_ctr]
                            top_five_index[list_ctr_2] = list_ctr
                            break
                for list_ctr in range(len(top_five)):
                    if len(temp_topics[0]) > 4:
                        temp_topics_list.append(temp_topics[0][top_five_index[list_ctr]])
                data_topic.append(temp_topics_list)
                temp_topics = [[], []]
            if not(temp_date in data_date):
                data_date.append(temp_date)
                    
            #add current tweet to temp_topics
            temp_string = tweet_list[ctr].split()
            for string_ctr in range(len(temp_string)):
                if algo.processWord(temp_string[string_ctr]) in temp_topics[0]:
                    temp_topics[1][temp_topics[0].index(algo.processWord(temp_string[string_ctr]))] += 1
                else:
                    if algo.processWord(temp_string[string_ctr]) != "":
                        temp_topics[0].append(algo.processWord(temp_string[string_ctr]))
                        temp_topics[1].append(1)
        
        #Populate tweet_data
        for ctr in range(len(data_date)):
            tweet_data.append(data_date[ctr])
            tweet_data.append(data_topic[ctr])
        
        return tweet_data   

    #Get data based on file name
    def getDataFromFile(self, filename, columns, col_eval, isLongDate):
        CSVfile = open(filename, 'r', encoding = 'latin1') #Open the filename.csv file
        Reader = csv.reader(CSVfile, dialect = 'excel') #Set filename.csv to a reader variable

        #Retrieve list of frustrated tweets from filename.csv
        tweet_data = self.getTweetData(Reader, columns, col_eval, isLongDate)

        CSVfile.close() #Close the filename.csv file

        return tweet_data

    #Create the graph based on filename.csv
    def create_topics(self, master, filename, columns, col_eval, isLongDate):
        #Create tweet table for GUI
        tweet_topic = topicgui.tweetTopic(master,
                                          self.getDataFromFile(filename, columns, col_eval, isLongDate),
                                          filename + ' Frustrated Tweet Top Topics')

        #Set GUI element
        gui = topicgui.TopicGUI(master, tweet_topic)

    #Create the graph based on all Yolanda .csvs
    def create_yolanda_topics(self, master):
        tweet_data = []

        tweet_data = self.getDataFromFile('Pablo Meier.csv', [2, 0], 2, True)
        tweet_data = tweet_data + self.getDataFromFile('Yolanda Meier.csv', [1, 0], 1, False)
        tweet_data = tweet_data + self.getDataFromFile('metromanila.csv', [2, 3], 2, True)

        #Create tweet table for GUI
        tweet_topic = topicgui.tweetTopic(master,
                                          tweet_data,
                                          'All Yolanda Files Frustrated Tweet Counts')

        #Set GUI element
        gui = topicgui.TopicGUI(master, tweet_topic)
