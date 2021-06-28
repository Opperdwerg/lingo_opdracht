from tkinter.constants import CENTER
import Lingo
import tkinter as tk
import sqlite3
import random

conn = sqlite3.connect('lingo.sqlite3')

master = tk.Tk()
tekstFrame = tk.Frame(master)
lingoFrame = tk.Frame(master)
canvas = tk.Canvas(lingoFrame, width=300, height=300)
canvas.pack()

squaresize = 50
width = 250
height = 250

def select_woord():
    woorden = conn.execute('SELECT woord FROM vijfletters;')
    randomwoord = random.randrange(0, 3242)
    global lingo
    lingo = Lingo.Lingo(woorden.fetchall()[randomwoord][0])
    print(lingo.woord)


def reset():
    create_grid()
    select_woord()
    check_hint()
    button["state"] = "active"
    beurttekst["text"] = "Beurt 1/5"
    eindtekst["text"] = ""

def create_grid():
    for x in range(25, width, squaresize):
        for y in range(25, height, squaresize):
            canvas.create_rectangle(x, y, x+squaresize, y+squaresize, fill="light sky blue", outline="white", width=10)

def set_gridline():
    input = entry.get().upper()
    lingo.validate_input(input)

    check_woord(input)


def check_hint():
    print(lingo.hint)
    hint = lingo.hint.upper()
    beurt = (lingo.beurt+1)*50
    counter = 25
    counter2 = 0

    for ch in hint:
        if ch != "-":
            canvas.create_rectangle(counter, beurt-25, counter+50, beurt+25, fill="blue", outline="white", width=10)
            canvas.create_text(counter+25, beurt, text=ch)

        counter += 50
        counter2 += 1

def check_woord(woord):
    beurt = lingo.beurt*50
    counter = 25
    counter2 = 0
    square = "nergens"
    for ch in woord:
        square = lingo.check_letter(ch, counter2)
        if square == "goed":
            canvas.create_rectangle(counter, beurt-25, counter+50, beurt+25, fill="blue", outline="white", width=10)
        elif square == "ergens":
            canvas.create_rectangle(counter, beurt-25, counter+50, beurt+25, fill="yellow", outline="white", width=10)
        elif square == "nergens":
            canvas.create_rectangle(counter, beurt-25, counter+50, beurt+25, fill="red", outline="white", width=10)

        canvas.create_text(counter+25, beurt, text=ch)
        counter += 50
        counter2 += 1
    
    check_hint()

    beurttekst["text"] = f"Beurt {1+lingo.beurt}/5"
    if lingo.gewonnen == True:
        button["state"] = "disabled"
        eindtekst["text"] = "Je hebt gewonnen!"
        return
        
    if lingo.verloren == True:
        button["state"] = "disabled"
        eindtekst["text"] = "Je hebt verloren :("
        return
        

hoofdtekst = tk.Label(tekstFrame, text="Raad het woord van vijf letters in vijf beurten")
hoofdtekst.pack(pady=10, side="top")
beurttekst = tk.Label(tekstFrame, text="Beurt 1/5", justify=CENTER)
beurttekst.pack(pady=10)

entry = tk.Entry(tekstFrame)
entry.pack()

button = tk.Button(tekstFrame, command=set_gridline, text="Stuur")
button.pack()

resetbutton = tk.Button(tekstFrame, command=reset, text="Reset")
resetbutton.pack()

eindtekst = tk.Label(tekstFrame, text="")
eindtekst.pack(pady=10)



tekstFrame.pack()
lingoFrame.pack()

create_grid()
select_woord()
check_hint()

master.mainloop()
