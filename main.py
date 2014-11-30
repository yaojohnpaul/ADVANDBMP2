#Import statements
import csv #CSV Library
import algo #Our tweet evaluation algo python file
import tablegen #Our table generator class
import graphgen #Our graph generator class
#GUI
from tkinter import *


#Create the global GUI root widget
root = Tk()

#Main Function
def mainFunction():
    if algo.isTable == True:
        newTable = tablegen.TableGen(root, algo.fileNumber)
        root.wm_title("ADVANDB MP2 - Table")
    elif algo.isTable == False:
        newGraph = graphgen.GraphGen(root, algo.fileNumber)
        root.wm_title("ADVANDB MP2 - Graph")

    #Display the GUI
    root.mainloop()

#Call the main function
mainFunction()
