from tkinter import Entry, Frame, Label, StringVar, messagebox, Button, Text
from tkinter.scrolledtext import ScrolledText
from tkinter.constants import *
from tkinter import Tk
import tkinter as tk
from inverted_index_words import *
from Author_tag_index import *
from positional_inverted_index import *
from PIL import ImageTk, Image

def search_menus():
    global query
    query=e1.get()
    print(query)
    if query=="":
        searchResult=["कृपया एक वैध सवाल दर्ज करें"]
        printResult(searchResult)
    else:
        decider=query.split()
        if decider[0]=="लेखक":
            query_string=' '.join(decider[1:])
            print(query_string)
            searchResult=author_search(query_string)
        elif decider[0]=="वर्ग":
            query_string=' '.join(decider[1:])
            print(query_string)
            searchResult=category_search(query_string)
        elif decider[0]=="pos":
            query_string=' '.join(decider[1:])
            searchResult=pos_term_search(query_string)

        elif decider[0]=="phrase":
            query_string=' '.join(decider[1:])
            searchResult=pos_phrase_search(query_string)
        else:
            searchResult=search_inv_idx(query)
        printResult(searchResult)
def printResult(searchResult):
    #Function to format the search results to be printed to the GUI
    global resultsFrame
    global text
    text.delete("1.0",END)
    for i in searchResult:
        text.insert(END,str(i)+'\n\n')
    text.pack(side=TOP)





#-----------------Tkinter root initialisation---------------------------------#
root = Tk()
topFrame = Frame(root,highlightbackground="cyan")
topFrame.pack(side = TOP)

topFrame2 = Frame(root)
topFrame2.pack(side = TOP)

root.wm_title("तलाश")
#setting the frame title

intro = Label(topFrame,text="तलाश में आपका स्वागत है \n\n चलो एक साथ खोज करते हैं",bg="black",fg="white", font="Times 14 bold")
intro.pack(fill=X)
print("\n\n\n\n")

intro2 = Label(topFrame,text="1. लेखक नाम से खोज करें: \t लेखक <name>\n\n 2. वर्ग के नाम से खोजें: \t वर्ग <category> \n\n 3. सामान्य खोज: \t \"सवाल\" \n\n 4. सामान्य खोज\
: (positional inverted index): pos <सवाल>\n\n 5. वाक्यांश खोज: phrase  \"सवाल\" ",bg="pink",fg="black",font="Helvetica 14 bold italic")
intro2.pack(fill=X)

Label(topFrame, text="सवाल",font="Times 14 bold").pack(side = LEFT)
e1 = Entry(topFrame,font="Times 14 bold")
e1.insert(0, "खोज करो")
e1.pack(side = RIGHT)
#the input bar


midFrame = Frame(root)
midFrame.pack(side=TOP)


bottomFrame = Frame(root)
bottomFrame.pack(side=TOP)
searchButton = Button(bottomFrame,text='खोजें', command=search_menus,fg="blue",font="Times 14 bold")
searchButton.pack(side = TOP)

resultsFrame = Frame(root,background="bisque")
resultsFrame.pack(side=TOP)
text = Text(resultsFrame,font='Helvetica 12 bold',fg='green')
#text=ScrolledText(resultsFrame, undo=True, font='Helvetica 12 bold',fg='green')
#text.pack(expand=True, fill='both')

root.mainloop()
