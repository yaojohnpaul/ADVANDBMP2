#Import statements
from tkinter import *

#Class for the GUI
class TopicGUI:
    def __init__(self, master, topic):
        canvas = topic
        canvas.pack(side = "top", fill = "x")

#GUI Class for Tweet Data Graph
#Based on code from:
#https://www.daniweb.com/software-development/python/code/216816/draw-a-bar-graph-python
class tweetTopic(Canvas):
    #Constructor
    def __init__(self, master, entries, header):
        canvas_width = 1134
        canvas_height = 400
        Canvas.__init__(self, master, width = canvas_width, height = canvas_height, bg = "white")

        self.populateTopic(entries, canvas_width, canvas_height, header) 

    #Populate graph
    def populateTopic(self, entries, width, height, header):
        x_gap = 130 #gap between left edge and y axis
        x_text_gap = 20 #gap between left edge and text beside y axis
        y_header_gap = 30 #gap between top edge and upper x axis
        y_gap = 20 #gap between lower edge and x axis
        x_max = width - x_gap * 2 #maximum width of bar
        for ctr in range(int(len(entries)/2)):
            entry_date = entries[ctr * 2]
            entry_topics = entries[(ctr * 2) + 1]
            x0 = x_gap
            y1 = (ctr + 1) * 20 + y_header_gap
            self.create_text(x_text_gap, y1, anchor = SW, text = entry_date)   
            self.create_text(x0 - 40, y1, anchor = SW, text = entry_topics)
            self.create_text(x_text_gap, y_gap, anchor = SW, text = header)
        
