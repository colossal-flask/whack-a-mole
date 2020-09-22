from tkinter import *
from time import *
from PIL import ImageTk, Image  
import os, random, threading

root = Tk()
root.resizable(width=False, height=False)
root.title('Whack-A-Mole')

score = 0
n_whacked = 0
d_whacked = 0 

game_time = 20

current_path = os.path.dirname(os.path.abspath(__file__))

#Load the images that will be used during the game
mole_head = ImageTk.PhotoImage(Image.open(current_path + "\\assets\\mole.png"))
hole = ImageTk.PhotoImage(Image.open(current_path + "\\assets\\hole.png"))
dog = ImageTk.PhotoImage(Image.open(current_path + "\\assets\\dog.png"))
gmole_head = ImageTk.PhotoImage(Image.open(current_path + "\\assets\\goldenmole.png"))

#Create the labels that will be used during the game
instruction_label = Label(root, text="Click on the mole's head before it disappears ... \nbut don't hit the dogs!")
space_label = Label(root, text=" ")
score_label = Label(root, text=" ")
stats_label = Label(root, text=" ")

#Define game functions.

#Initalizes the game by removing start button (if run for the first time) 
#and placing "score" label.
def start_game():
    start_button.grid_remove()
    score_label.grid(row=2, column=0, columnspan=3, padx=60, pady=10)
    
    game_thread = threading.Thread(target=game_running)
    game_thread.start()
    
#Resets the specified hole back to the default case. 
def reset_hole(num):
    if num == 1:
        b1.configure(image=hole, command=missed)
    elif num == 2:
        b2.configure(image=hole, command=missed)
    elif num == 3:
        b3.configure(image=hole, command=missed)
    elif num == 4:
        b4.configure(image=hole, command=missed)
    elif num == 5:
        b5.configure(image=hole, command=missed)
    elif num == 6:
        b6.configure(image=hole, command=missed)       
    elif num == 7:
        b7.configure(image=hole, command=missed) 
    elif num == 8:
        b8.configure(image=hole, command=missed) 
    elif num == 9:
        b9.configure(image=hole, command=missed)

#Causes either a mole or dog to "pop" out from the given hole.         
def set_hole(hole_num, dog_head, golden_mole):
    if dog_head == True:
        if hole_num == 1:
            b1.configure(image=dog, command=dog_whacked)
        elif hole_num == 2:
            b2.configure(image=dog, command=dog_whacked)
        elif hole_num == 3:
            b3.configure(image=dog, command=dog_whacked)
        elif hole_num == 4:
            b4.configure(image=dog, command=dog_whacked)
        elif hole_num == 5:
            b5.configure(image=dog, command=dog_whacked)
        elif hole_num == 6:
            b6.configure(image=dog, command=dog_whacked)
        elif hole_num == 7:
            b7.configure(image=dog, command=dog_whacked)
        elif hole_num == 8:
            b8.configure(image=dog, command=dog_whacked)
        elif hole_num == 9:
            b9.configure(image=dog, command=dog_whacked)
    elif golden_mole == True:
        if hole_num == 1:
            b1.configure(image=gmole_head, command=gmole_whacked)
        elif hole_num == 2:
            b2.configure(image=gmole_head, command=gmole_whacked)
        elif hole_num == 3:
            b3.configure(image=gmole_head, command=gmole_whacked)
        elif hole_num == 4:
            b4.configure(image=gmole_head, command=gmole_whacked)
        elif hole_num == 5:
            b5.configure(image=gmole_head, command=gmole_whacked)
        elif hole_num == 6:
            b6.configure(image=gmole_head, command=gmole_whacked)
        elif hole_num == 7:
            b7.configure(image=gmole_head, command=gmole_whacked)
        elif hole_num == 8:
            b8.configure(image=gmole_head, command=gmole_whacked)
        elif hole_num == 9:
            b9.configure(image=gmole_head, command=gmole_whacked)
    else:
        if hole_num == 1:
            b1.configure(image=mole_head, command=whacked)
        elif hole_num == 2:
            b2.configure(image=mole_head, command=whacked)
        elif hole_num == 3:
            b3.configure(image=mole_head, command=whacked)
        elif hole_num == 4:
            b4.configure(image=mole_head, command=whacked)
        elif hole_num == 5:
            b5.configure(image=mole_head, command=whacked)
        elif hole_num == 6:
            b6.configure(image=mole_head, command=whacked)
        elif hole_num == 7:
            b7.configure(image=mole_head, command=whacked)
        elif hole_num == 8:
            b8.configure(image=mole_head, command=whacked)
        elif hole_num == 9:
            b9.configure(image=mole_head, command=whacked)
    
def game_running():
    global hole_num
    
    score_label.configure(text="3...")
    sleep(1)
    score_label.configure(text="2...")
    sleep(1)    
    score_label.configure(text="1...")
    sleep(1)
    score_label.configure(text="Whack 'Em!")
        
    for button in buttons:
        button.configure(state='normal', command=missed)
    
    for x in range(0, game_time):
        hole_num = random.randint(1, 9)
        dog_num = random.randint(1, 6)
        golden_num = random.randint(1, 10)

        if dog_num == 1:
            set_hole(hole_num, True, False)
        elif golden_num == 1:
        #golden moles give more points but escape faster
            set_hole(hole_num, False, True)
            sleep(.600)
            reset_hole(hole_num)
            continue
        else:
            set_hole(hole_num, False, False)
            
        sleep(.800)
        reset_hole(hole_num)
        
    game_end()

#If a player clicks on an empty hole, they lose 1 point.
def missed():
    global score, n_whacked
    score -= 1
    score_label.configure(text="Current Score: " + str(score))
    reset_hole(hole_num)
    
#Whenever a mole is whacked, the player gains 1 point. 
def whacked():
    global score, n_whacked
    score += 1
    n_whacked += 1
    score_label.configure(text="Current Score: " + str(score))
    reset_hole(hole_num)

#Whenever a golden mole is whacked, the player gains 5 points.
def gmole_whacked():
    global score, n_whacked
    score += 5
    n_whacked += 1
    score_label.configure(text="Current Score: " + str(score))
    reset_hole(hole_num)   

#Whenever a dog is whacked, the player loses two points.
def dog_whacked():
    global score, d_whacked
    score -= 2
    d_whacked += 1
    score_label.configure(text="Current Score: " + str(score))
    reset_hole(hole_num)
    
#Locks holes, displays scores and offers a replay button.
def game_end():
    score_label.configure(text=" ")

    for button in buttons:
        button.configure(image=hole, state='disabled')
        
    instruction_label.configure(text="Game Over!")
    sleep(1.500)
    instruction_label.configure(text="Your final score: " + str(score))
    sleep(.800)
    space_label.configure(text="Moles Whacked: " + str(n_whacked) + "   Dogs Whacked: " + str(d_whacked))     
    sleep(.800)
    restart_button.grid(row=2, column=0, columnspan=3)
    
#resets game score/counters and starts a new game
def restart_game():
    global n_whacked, score, d_whacked
    n_whacked = 0
    score = 0 
    d_whacked = 0
    restart_button.grid_remove()
    instruction_label.configure(text="Click on the mole's head before it disappears ... \nbut don't hit the dogs!")
    space_label.configure(text=" ")
    start_game()
    

# Create the buttons needed for the game. 
start_button = Button(root, text="Start!", command=start_game, padx=60, pady=10)
restart_button = Button(root, text="Play Again!", command=restart_game)

b1 = Button(root, image=hole, state='disabled')
b2 = Button(root, image=hole, state='disabled')
b3 = Button(root, image=hole, state='disabled')
b4 = Button(root, image=hole, state='disabled')
b5 = Button(root, image=hole, state='disabled')
b6 = Button(root, image=hole, state='disabled')
b7 = Button(root, image=hole, state='disabled')
b8 = Button(root, image=hole, state='disabled')
b9 = Button(root, image=hole, state='disabled')

buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9] #used to make enabling/disabling easier

#Populate the GUI.
instruction_label.grid(row=0, column=0, columnspan=3)
space_label.grid(row=1, column=0, columnspan=3)

start_button.grid(row=2, column=0, columnspan=3)

b1.grid(row=4, column=0)
b2.grid(row=4, column=1)
b3.grid(row=4, column=2)

b4.grid(row=5, column=0)
b5.grid(row=5, column=1)
b6.grid(row=5, column=2)

b7.grid(row=6, column=0)
b8.grid(row=6, column=1)
b9.grid(row=6, column=2)

root.mainloop()