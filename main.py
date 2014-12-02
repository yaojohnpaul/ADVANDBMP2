#Import statements
import csv #CSV Library
import algo #Our tweet evaluation algo python file
import tablegen #Our table generator class
import graphgen #Our graph generator class
import topicgen #Our topic generator class
#GUI
from tkinter import *


#Create the global GUI root widget
root = Tk()
root2 = Tk()
root3 = Tk()

#Main Function
def mainFunction():
    newTopic = topicgen.TopicGen(root, algo.fileNumber)
    root.wm_title("ADVANDB MP2 - Top Topics")
    newGraph = graphgen.GraphGen(root2, algo.fileNumber)
    root2.wm_title("ADVANDB MP2 - Graph")
    newTable = tablegen.TableGen(root3, algo.fileNumber)
    root3.wm_title("ADVANDB MP2 - Table")

    #Display the GUI
    root.mainloop()
    root2.mainloop()
    root3.mainloop()

#Call the main function
mainFunction()
