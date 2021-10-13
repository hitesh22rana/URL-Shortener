import pyshorteners
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import font
import clipboard

final_result = ""

def CopyURL():
    global final_result
    try:
        clipboard.copy(final_result)
    except Exception as e:
        final_result = ""

def CreateURL():
    global final_result
    try:
        s = pyshorteners.Shortener()
        url = URLEntry.get()
        final_result = s.tinyurl.short(url)
        print(final_result)
        URLGenerated.config(text = final_result)
        URLGenerated.place(x = 90 , y = 220)
        URLEntry.delete(0 , END)


    except Exception as e:
        URLEntry.delete(0 , END)
        URLGenerated.config(text = "Enter Valid URL!")
        URLGenerated.place(x = 150 , y = 220)
        final_result = ""


if __name__ == "__main__":

    root = Tk()
    root.title("URL Shortener")
    root.geometry("450x350") #Set
    root.minsize(450,350)
    root.maxsize(450,350)
    root.columnconfigure(0 , weight=1) 
    root.configure(bg='#f1faee')

    #GUI
    URLlabel = Label(root , text = "Enter The URL" , font = ("calibri",25,"bold"), fg='#293241' , bg='#f1faee')
    URLlabel.place(x = 124 , y = 20)
    
    # Entry Box
    # URLEntryVar = StringVar()
    URLEntry = Entry(root , font = ("calibri",15) , fg= '#3d405b', bg= '#e9edc9')
    URLEntry.place(x = 72 , y = 100 , width=300 , height=30)
    
    #btn to create URL
    GenerateURL = Button(root, width=15,bg="#d62828",fg="white" , font=('calibri',10,"bold") ,text="Generate TinyURL" , activebackground='#e07a5f', command=CreateURL)
    GenerateURL.place(x = 165 , y = 165)
    
    # TinyURL is displayed here
    URLGenerated = Label(root , text = "Tiny URL will be Displayed Here!" , font = ("calibri",15,"bold"), fg='#52b788' , bg='#f1faee')
    URLGenerated.place(x = 85 , y = 220)

    # str_url = StringVar(root)
    #copy Button
    GenerateURL = Button(root, width=6,bg="#d62828",fg="white" , font=('calibri',10,"bold") ,text="Copy" , activebackground='#e07a5f', command=CopyURL)
    GenerateURL.place(x = 195 , y = 280)

    root.mainloop()