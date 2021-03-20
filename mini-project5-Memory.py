"""
Week 5 Mini-Project of An Introduction to Interactive Programming

CodeSkulptor: http://www.codeskulptor.org/#user47_Rc8UbXONeAeXC4r.py
Written in Python 2
"""

# implementation of card game - Memory

import simplegui
import random

number_range = []
number_list = []

exposed = []
state = 0
face1 = []
face2 = []
turns = 0


# helper function to initialize globals
def new_game():
    global number_range, number_list
    global exposed, state, face1, face2, turns
    
    number_range = range(8)
    number_list = number_range + number_range

    random.shuffle(number_list)

    exposed = []
    for i in range(16):
        exposed.append(False)
    
    state = 0
    face1 = []
    face2 = []
    turns = 0

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global number_list, exposed, state, turns
    global face1, face2  # To keep track of the face-up cards.
    
    click_pos = pos[0] // 50
    # To prevent double-clicking on already exposed cards.
    if exposed[click_pos] is False or None:
        if state == 0:
            exposed[click_pos] = True
            face1 = [click_pos, number_list[click_pos]]
            
            turns += 1
            state = 1
        elif state == 1:
            exposed[click_pos] = True
        
            # The two face-up card happens to be a match.
            if face1[1] == number_list[click_pos]:
                exposed[face1[0]] = None
                exposed[click_pos] = None
                state = 0
            else:
                face2 = face1
                face1 = [click_pos, number_list[click_pos]]
                state = 2
        else:
            exposed[face1[0]] = False
            exposed[face2[0]] = False
        
            exposed[click_pos] = True
            face1 = [click_pos, number_list[click_pos]]
            
            turns += 1
            state = 1
                         
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global number_list, exposed, label
    
    label.set_text("Turns = " + str(turns))
    
    center_width = 50
    for card_idx in range(len(number_list)):
        line_pos = center_width * card_idx
        card_pos = line_pos + 25
        
        if exposed[card_idx]:
            # Show cards that are exposed if True.
            canvas.draw_text(str(number_list[card_idx]), (card_pos - 10, 65), 50, "White")
        elif exposed[card_idx] is None:
            # Matched cards will remain exposed.
            canvas.draw_text(str(number_list[card_idx]), (card_pos - 10, 65), 50, "White")
        else:
            # Show green when card aren't exposed.
            canvas.draw_line((card_pos, 0), (card_pos, 100), 50, "Green")
        
        # Have lines dividing between each cards.
        canvas.draw_line((line_pos, 0), (line_pos, 100), 1, "Black")
            
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = " + str(turns))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

