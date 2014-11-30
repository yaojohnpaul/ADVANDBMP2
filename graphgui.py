#Import statements
from tkinter import *

#Class for the GUI
class GraphGUI:
    def __init__(self, master, graph):
        canvas = graph
        canvas.pack(side = "top", fill = "x")

#GUI Class for Tweet Data Graph
#Based on code from:
#https://www.daniweb.com/software-development/python/code/216816/draw-a-bar-graph-python
class tweetGraph(Canvas):
    #Constructor
    def __init__(self, master, entries, header):
        canvas_width = 1134
        canvas_height = 400
        Canvas.__init__(self, master, width = canvas_width, height = canvas_height, bg = "white")
        max_entry = 0
        for ctr in range(int(len(entries)/2)):
            if entries[(ctr * 2) + 1] > max_entry:
                max_entry = entries[(ctr * 2) + 1]

        self.populateGraph(entries, max_entry, canvas_width, canvas_height, header) 

    #Populate graph
    def populateGraph(self, entries, max_entry, width, height, header):
        x_gap = 100 #gap between left edge and y axis
        x_text_gap = 20 #gap between left edge and text beside y axis
        y_header_gap = 30 #gap between top edge and upper x axis
        y_gap = 20 #gap between lower edge and x axis
        x_max = width - x_gap * 2 #maximum width of bar
        y_height = int(((height * 1.5) - (y_gap + y_header_gap))/len(entries)) #height of each bar        
        for ctr in range(int(len(entries)/2)):
            entry_date = entries[ctr * 2]
            entry_count = entries[(ctr * 2) + 1]
            x0 = x_gap
            y0 = (ctr * y_height) + y_header_gap
            x1 = ((entry_count / max_entry) * x_max) + x_gap
            y1 = ((ctr + 1) * y_height) + y_header_gap
            self.create_rectangle(x0, y0, x1, y1, fill = "red")
            self.create_text(x_text_gap, y1, anchor = SW, text = entry_date)
            self.create_text(x0 + 5, y1, anchor = SW, text = entry_count, fill = "white")
            self.create_text(x_text_gap, y_gap, anchor = SW, text = header)
        
