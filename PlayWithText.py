import os
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import tkinter.messagebox as tmsg

class PlayWithText:

    # FUNCTIONS ARE HERE 
    def capitalizeEachWord(self, text):
        textr = text.split(" ")
        returnText = ""
        for i in range(len(textr)):
            returnText += textr[i].capitalize() + " "
        return returnText 
            
    
    # MENUBAR FUNCTIONS ARE HERE 
    # FUNCTION FOR CHANGE THEME 
    def shiftMode(self, event):
        mode = event.widget.cget("text")
        if mode == "Enable Relax Mode":
            self.theme(bgColor='#3b2664', textAreaColor='#664a9d', textColor='white', titleColor='white')
        elif mode == "Enable Light Mode":
            self.theme(bgColor='white', titleColor='#3e1d7e', textColor='black', textAreaColor='white')

    # FUNCTION FOR OPEN A NEW BLANK FILE
    def newFile(self):
        if len(userTextResult.get(1.0, END)) != len(userText.get(1.0, END)):
                newVal = str(userText.get(1.0, END)).replace(str(userTextResult.get(1.0, END)), "")
                userTextResult.delete(1.0, END)
                userText.delete(1.0, END)

    # FUNCTION TO OPEN AN EXISTING FILE 
    def openFile(self):
        global file
        file  = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if file=="":
            file=None
        else:
            root.title(os.path.basename(file)+" - Notepad")
            userText.delete(1.0, END)
            f = open(file, 'r')
            userText.insert(1.0, f.read())
            userTextResult.delete(1.0, END)
            f.close()

    # FUNCTION FOR OPEN A FILE 
    def saveFile(self):
        global file
        if file == None:
            if file=="":
                file = None
            if len(userTextResult.get(1.0, END)) > 1:
                file = asksaveasfilename(initialfile="Untitled.txt", defaultextension='.txt', filetypes=[("All Files", "*.*"), ("Text Documents","*.txt")])
                #  SAVE AS NEW FILE 
                f = open(file, 'w')
                f.write(userTextResult.get(1.0, END))
                f.close()
                root.title(os.path.basename(file) + " - Notepad")
            else:
                msg = tmsg.askokcancel(title="Actions Box Was Empty", message="Action Box was Empty You want to save you origional content")
                if msg == True:
                    file = asksaveasfilename(initialfile="Untitled.txt", defaultextension='.txt', filetypes=[("All Files", "*.*"), ("Text Documents","*.txt")])
                    #  SAVE AS NEW FILE 
                    f = open(file, 'w')
                    f.write(userText.get(1.0, END))
                    root.title(os.path.basename(file) + " - Notepad")
                    f.close()
        else:
            # SAVE THE FILE  
            f = open(file, 'w')
            f.write(userTextResult.get(1.0, END))
            f.close()
        

    # FUNCTION FOR CUT 
    def cut(self):
        userText.event_generate('<<Cut>>')

    # FUNCTION TO COPY 
    def copy(self):
        userText.event_generate('<<Copy>>')

    # FUNCTION TO PASTE 
    def paste(self):
        userText.event_generate('<<Paste>>')

    # FUNCTION TO UNDO 
    def undo(self):
        userText.event_generate('<<Undo>>')

    # FUNCTION FOR REDO 
    def redo(self):
        userText.event_generate('<<Redo>>')

    # FUNCTION FOR PURPLE THEME 
    def purpleTheme(self):
        global btnColor
        btnColor = '#3b2664'
        root.configure(background="#3b2664")
        heading.configure(background='#3b2664', fg='white')
        modeBtnsFrame.config(bg='#3b2664')
        screenFrame.config(bg='#3b2664')
        userText.configure(background='#664a9d', fg='white')
        userTextResult.configure(background='#664a9d', fg='white')
        buttonFrame.config(bg='#3b2664')

    # FUNCTION FOR LIGHT THEME 
    def lightTheme(self):
        root.configure(background="white")
        heading.configure(background='white', fg='#3e1d7e')
        modeBtnsFrame.config(bg='white')
        screenFrame.config(bg='white')
        userText.configure(background='white', fg='black')
        userTextResult.configure(background='white', fg='black')
        buttonFrame.config(bg='white')

    # FUNCTION FOR DARK THEME 
    def darkTheme(self):
        global btnColor
        btnColor = 'black'
        root.configure(background="black")
        heading.configure(background='black', fg='white')
        modeBtnsFrame.config(bg='black')
        screenFrame.config(bg='black')
        userText.configure(background='grey', fg='white')
        userTextResult.configure(background='grey', fg='white')
        buttonFrame.config(bg='black')

    # FUNCTION FOR RED THEME 
    def redTheme(self):
        global btnColor
        btnColor = '#870000'
        root.configure(background="#870000")
        heading.configure(background='#870000', fg='white')
        modeBtnsFrame.config(bg='#870000')
        screenFrame.config(bg='#870000')
        userText.configure(background='#b51f1f', fg='white')
        userTextResult.configure(background='#b51f1f', fg='white')
        buttonFrame.config(bg='#870000')

    # FUNCTION FOR ABOUT IN HELP MENU 
    def about(self):
        tmsg.showinfo(title="About Software", message="You can use this software for manipuating text in between your work sometimes you have to manipulate text like convert all text into lowercase and uppercase etc and you can do this manually and you also know it is a big headech to you can use this software to do these thing perfectly and in a good manner. Thanks for using my software")

    def click(self, event):
        global userText, userTextResult, file
        text = event.widget.cget("text")
        val = 'empty'

        if len(userTextResult.get(1.0, END)) != len(userText.get(1.0, END)):
            newVal = str(userText.get(1.0, END)).replace(str(userTextResult.get(1.0, END)), " ")

        if text == "Capitalize":
            userTextResult.delete(1.0, END)
            val = newVal.capitalize() + ''
            userTextResult.insert(0.0, val )

        elif text == "Upper Case":
            userTextResult.delete(1.0, END)
            val =  newVal.upper()+''
            userTextResult.insert(0.0, val)

        elif text == "Lower Case":
            userTextResult.delete(1.0, END)
            val = newVal.lower()+''
            userTextResult.insert(0.0, val)

        elif text == "Cap Each Word":
            userTextResult.delete(1.0, END)
            val =  self.capitalizeEachWord(newVal) + ''
            userTextResult.insert(0.0, val)

        elif text == "Copy":
            self.copy()

        elif text == "Cut":
            self.cut()

        elif text == "Paste":
            self.paste()

        elif text == "Delete":
                if len(userTextResult.get(1.0, END)) != len(userText.get(1.0, END)):
                    newVal = str(userText.get(1.0, END)).replace(str(userTextResult.get(1.0, END)), "")
                    userTextResult.delete(1.0, END)
                    userText.delete(1.0, END)
        elif text == "Save":
            self.saveFile()

        elif text == "Open":
            self.openFile()

    def theme(self, bgColor='white', textColor="black", titleColor="#3b2664", textAreaColor='black'):
        root.configure(background=f"{bgColor}")
        heading.configure(background=f'{bgColor}', fg=f'{titleColor}')
        modeBtnsFrame.config(bg=f"{bgColor}")
        screenFrame.config(bg=f"{bgColor}")
        userText.configure(background=f'{textAreaColor}', fg=f"{textColor}")
        userTextResult.configure(background=f'{textAreaColor}', fg=f"{textColor}")
        buttonFrame.config(bg=f"{bgColor}")


if __name__ == '__main__':
    # GUI STARTS HERE
    root = Tk()
    root.title("Manisha - Play With Text") # GUI TITLE
    root.geometry("830x700") # GUI HEIGHT WIDTH
    root.minsize(500,400) # GUI MIN SIZE

    # HEADING OF THE APP 
    heading = Label(root, text="Welcome to Play With Text By Manisha", font="lucida 15 bold", fg='#3e1d7e')
    heading.pack(pady=5)

    # ALL FRAMES ARE HERE 
    # CREATING FRAMES FOR SWITCH THEMES 
    modeBtnsFrame = Frame(root, )
    modeBtnsFrame.pack()

    # CREATING SCREEN FRAME FOR TAKING USERS TEXT AND RETURNING TEXT 
    screenFrame = Frame(root)
    screenFrame.pack()

    # CREATING A BUTTON FRAME TO ALL ACTIONS 
    buttonFrame =Frame(root)
    buttonFrame.pack()

    # CREATING A INSTANCE OF PlayWithText CLASS TO USE FUNCTIONS 
    playWithText = PlayWithText()

    file = None

    # TEXT AREAS ARE HERE 
    # CREAING A TEXTAREA FOR USER TEXT 
    userText = Text(screenFrame, font="lucida 14", width=35, height=15)
    userText.pack(padx=10, side=LEFT)

    # CREATING A TEXTAREA FOR RESULT TEXT 
    userTextResult = Text(screenFrame, font="lucida 14", width=35, height=15)
    userTextResult.pack(padx=10, side=LEFT)


    # STORING ALL BUTTONS NAME IN AN ARRAY  
    modeBtns = ["Enable Relax Mode", "Enable Light Mode"]

    # CREATING ALL BUTTON USING FOR LOOP 
    for  i in range(len(modeBtns)):
        btnColor = '#656572'
        modeBtn = Button(modeBtnsFrame, text=f"{modeBtns[i]}", font="lucida 10 bold", bg=f'{btnColor}', fg='white')
        modeBtn.pack(pady=15, padx=10, side=LEFT)
        modeBtn.bind("<Button-1>", playWithText.shiftMode)




    # STORING ALL BUTTONS NAME IN A LIST 
    allBtns = ["Capitalize", "Upper Case", "Lower Case", "Cap Each Word" ,"Copy", "Cut", "Paste", "Save","Open", "Delete"]

    # CREAING ALL BUTTON USING FOR LOOP 
    for  i in range(len(allBtns)):
        btnColor = '#656572'
        capitalizeBtn = Button(buttonFrame, text=f"{allBtns[i]}", font="lucida 10 bold", bg=f'{btnColor}', fg='white')
        capitalizeBtn.pack(pady=30, padx=10, side=LEFT)
        capitalizeBtn.bind("<Button-1>", playWithText.click)


     # ADDING MENU BAR HERE 
    menuBar = Menu(root)
    # CREATING FILE MENU HERE WITH NEWFILE, OPENFILE, SAVEFILE FUNCTIONALITIES
    fileMenu = Menu(menuBar, tearoff=0)
    fileMenu.add_command(label="New", command=playWithText.newFile)
    fileMenu.add_command(label="Open", command=playWithText.openFile)
    fileMenu.add_command(label="Save", command=playWithText.saveFile)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=quit)

    # CREATING EDITMENU HERE WITH CUT, COPY, PASTE, UNDO, REDO FUNCTIONALITIES 
    editMenu = Menu(menuBar, tearoff=0)
    editMenu.add_command(label="Cut", command=playWithText.cut)
    editMenu.add_command(label="Copy", command=playWithText.copy)
    editMenu.add_command(label="Paste", command=playWithText.paste)
    editMenu.add_separator()
    editMenu.add_command(label="Undo", command=playWithText.undo)
    editMenu.add_command(label="Redo", command=playWithText.redo)

    # CREATING THEME MENU WITH SOME COLORED THEMES 
    themeMenu = Menu(menuBar, tearoff=0)
    themeMenu.add_command(label="Light Theme",  command=playWithText.lightTheme)
    themeMenu.add_command(label="Dark Theme", command=playWithText. darkTheme)
    themeMenu.add_command(label="Red Theme", command=playWithText. redTheme)
    themeMenu.add_command(label="Purple Theme", command=playWithText. purpleTheme)

    # CREATING HELP MENU WITH ABOUR APP 
    helpMenu = Menu(menuBar, tearoff=0)
    helpMenu.add_command(label="About", command=playWithText.about)

    # ADDING ALL CASCADES TO MAIN MANUBAR 
    menuBar.add_cascade(label="File", menu=fileMenu)
    menuBar.add_cascade(label="Edit", menu=editMenu)
    menuBar.add_cascade(label="Theme", menu=themeMenu)
    menuBar.add_cascade(label="Help", menu=helpMenu)

    # CONFIGURING MENUBAR FOR ROOT 
    root.config(menu=menuBar)

    # GUI MAIN LOOP HERE 
    root.mainloop()