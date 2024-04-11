# Task 1 - working with functions, modules, loops, IFs 

import tkinter, random
# create a possible list of colours
colors = ['Red', 'Blue', 'Green', 'Orange', 'Purple', 'Brown', 'Black', 'white', 'Yellow']

score = 0
timeleft = 30

#function that will start this game
def startGame(event):
    if timeleft ==30:
        # start the countdown
        countdown()
        #function call to choose the next color
    nextColor()
# function to choose and display the next color
def nextColor():
    global score
    global timeleft
    if timeleft > 0:
        e.focus_set()
        if e.get().lower()==colors[1].lower():
            score +=1
        e.delete(0,tkinter.END)
        random.shuffle(colors)
        label.config(fg=str(colors[1]), text =str(colors[0]))
        scoreLabel.config(text= "Score: "+ str(score))
        
def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timelabel.config(text = "Time Left: " + str(timeleft))
        timelabel.after(1000,countdown)
        
        
root = tkinter.Tk()
root.title("Color Game")
root.geometry("400x200")
instruction = tkinter.Label(root, text = "Type in the color of the word", font = ('Helvitica',12))
instruction.pack()

scoreLabel = tkinter.Label(root, text = "Press enter to start ", font = ('Helvitica',12))
scoreLabel.pack()

timelabel = tkinter.Label(root, text = "timeleft "  + str(timeleft), font = ('Helvitica',12))
timelabel.pack()

label = tkinter.Label(root, font = ('Helvitica',16))
label.pack()


e = tkinter.Entry(root)
root.bind('<Return>', startGame)
e.pack()
e.focus_set()
root.mainloop() 
    
