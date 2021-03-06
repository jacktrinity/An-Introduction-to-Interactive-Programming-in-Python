"""
Week 3 Mini-Project of An Introduction to Interactive Programming

CodeSkulptor: https://py3.codeskulptor.org/#user305_GB7h7m0SYW_2.py
Written in Python 3
"""

# "Stopwatch: The Game"

import simplegui
import time

# define global variables
time_in_tenth = 0
is_running = False
success = 0
attempt = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    str_time = str(t)
    str_tenth_sec = str_time[-1:]
    
    second = t // 10
    minute = second // 60
    
    if (second % 60) < 10:
        str_second = "0{}".format(str(second % 60))
    else:
        str_second = str(second % 60)
        
    
    time = "{}:{}.{}".format(str(minute), str_second, str_tenth_sec)
    return time
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global timer, is_running
    
    timer.start()
    is_running = timer.is_running()


def stop():
    global timer, time_in_tenth, is_running
    global success, attempt
    
    timer.stop()
    
    str_time = str(time_in_tenth)
    check_dec = str_time[-1:]
    
    if is_running:
        attempt += 1
        if check_dec == "0":
            success += 1
            
    is_running = timer.is_running()


def restart():
    global timer, time_in_tenth, is_running
    global success, attempt
    
    timer.stop()
    is_running = timer.is_running()
    
    time_in_tenth = 0
    success = 0
    attempt = 0


# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time_in_tenth
    
    time_in_tenth += 1


timer = simplegui.create_timer(100, timer_handler)

# define draw handler
def draw_handler(canvas):
    global time_in_tenth, attempt, success
    
    canvas.draw_text(format(time_in_tenth), (90, 115), 50, "White")
    canvas.draw_text("{}/{}".format(str(success), str(attempt)), (225, 35), 35, "Green")

    
# create frame
f = simplegui.create_frame("Stopwatch: The Game", 300, 200)


# register event handlers
f.add_button("Start", start, 100)
f.add_button("Stop", stop, 100)
f.add_button("Reset", restart, 100)

f.set_draw_handler(draw_handler)

# start frame
f.start()

