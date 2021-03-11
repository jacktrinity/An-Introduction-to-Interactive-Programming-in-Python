  
"""
Week 4 Mini-Project of An Introduction to Interactive Programming
CodeSkulptor: http://www.codeskulptor.org/#user47_yJ5nRUaLLk_2.py
Written in Python 2
"""

# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2

ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [1, 1]

paddle1_pos = HEIGHT / 2
paddle2_pos = HEIGHT / 2

paddle1_vel = 0
paddle2_vel = 0

score1 = 0
score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    
    if direction == "RIGHT":
        ball_vel[0] = random.randrange(120, 240) * 0.01
        ball_vel[1] = random.randrange(60, 180) * (-0.01)
    else:
        ball_vel[0] = random.randrange(120, 240) * (-0.01)
        ball_vel[1] = random.randrange(60, 180) * (-0.01)
    
    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    
    score1 = 0
    score2 = 0
    
    if random.randrange(0, 2) == 1:
        spawn_ball("LEFT")
    else:
        spawn_ball("RIGHT")

    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # Top collision and relfection
    if ball_pos[1] < 20:
        ball_vel[1] = ball_vel[1] * (-1)
    
    # Bottom collision and relfection
    if ball_pos[1] > HEIGHT - 20:
        ball_vel[1] = ball_vel[1] * (-1)
            
    # draw ball
    canvas.draw_circle([ball_pos[0], ball_pos[1]], BALL_RADIUS, 5, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    if HALF_PAD_HEIGHT <= paddle1_pos + paddle1_vel <= (HEIGHT - HALF_PAD_HEIGHT):
        paddle1_pos += paddle1_vel
        
    if HALF_PAD_HEIGHT <= paddle2_pos + paddle2_vel <= (HEIGHT - HALF_PAD_HEIGHT):
        paddle2_pos += paddle2_vel
    
    paddle1_top = [HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT]
    paddle1_bottom = [HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT]
    
    paddle2_top = [WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT]
    paddle2_bottom = [WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT]
    
    # draw paddles
    canvas.draw_line(paddle1_top, paddle1_bottom, PAD_WIDTH, "White")
    canvas.draw_line(paddle2_top, paddle2_bottom, PAD_WIDTH, "White")
    
    # determine whether paddle and ball collide 
    # Gutter: Left
    if ball_pos[0] < PAD_WIDTH + BALL_RADIUS:
        # Left Paddle Collide
        paddle1_top_col = paddle1_pos - HALF_PAD_HEIGHT - BALL_RADIUS
        paddle1_bottom_col = paddle1_pos + HALF_PAD_HEIGHT + BALL_RADIUS
        
        if paddle1_top_col <= ball_pos[1] <= paddle1_bottom_col:
            ball_vel[0] = ball_vel[0] * (-1.1)
        else:
            score2 += 1
            spawn_ball("RIGHT")  
        
    # Gutter: Right
    if ball_pos[0] > WIDTH - PAD_WIDTH - BALL_RADIUS:
        # Right Paddle Collide
        paddle2_top_col = paddle2_pos - HALF_PAD_HEIGHT - BALL_RADIUS
        paddle2_bottom_col = paddle2_pos + HALF_PAD_HEIGHT + BALL_RADIUS
        
        if paddle2_top_col <= ball_pos[1] <= paddle2_bottom_col:
            ball_vel[0] = ball_vel[0] * (-1.1)
        else:
            score1 += 1
            spawn_ball("LEFT")
    
    # draw scores
    canvas.draw_text(str(score1), (WIDTH / 4, HEIGHT / 4), 50, "White")
    canvas.draw_text(str(score2), ((3 * WIDTH) / 4, HEIGHT / 4), 50, "White")

    
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel += 4
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= 4

    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += 4
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= 4

        
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 100)


# start frame
new_game()
frame.start()
