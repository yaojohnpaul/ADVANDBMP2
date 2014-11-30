#Import statements
from tkinter import *

#Class for the GUI
class TableGUI:
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
