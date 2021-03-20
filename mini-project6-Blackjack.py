"""
Week 6 Mini-Project of An Introduction to Interactive Programming

CodeSkulptor: http://www.codeskulptor.org/#user48_zh7mHUaQXM8ltu4.py
Written in Python 2
"""

# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
score = 0

player_bust = False
dealer_win = False
player_win = False

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []

    def __str__(self):
        str_hand = ""
        for i in self.hand:
            str_hand += str(i) + " "
            
        return str_hand

    def add_card(self, card):
        self.hand.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        global VALUES
        
        hand_value = 0
        ace_check = []
        for i in self.hand:
            ace_check.append(i.get_rank())
            hand_value += VALUES[i.get_rank()]
            
        if "A" not in ace_check:
            return hand_value
        else:
            if hand_value + 10 <= 21:
                return hand_value + 10
            else:
                return hand_value
            
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for i in self.hand:
            draw_hand = Card(i.get_suit(), i.get_rank())
            draw_hand.draw(canvas, pos)
            pos[0] += 95
        
# define deck class 
class Deck:
    def __init__(self):
        global SUITS, RANKS
        
        self.deck = []
        # create a Deck object
        for suit in SUITS: 
            for rank in RANKS:
                new_card = Card(suit, rank)
                self.deck.append(new_card)

    def shuffle(self):
        # shuffle the deck 
        # use random.shuffle()  
        random.shuffle(self.deck)

    def deal_card(self):
        # deal a card object from the deck
        dealt_card = self.deck[0]
        self.deck.remove(dealt_card)
        return dealt_card
    
    def __str__(self):
        # return a string representing the deck
        str_deck = ""
        for i in self.deck:
            str_deck += str(i) + " "
            
        return str_deck

#define event handlers for buttons
def deal():
    global in_play, score
    global game_deck, player_hand, cpu_hand
    global player_bust, dealer_win, player_win
    
    player_bust = False
    dealer_win = False
    player_win = False
    
    # If game is still in play: -1 to score
    if in_play:
        score -= 1

    # Setup deck, player and cpu hand.
    game_deck = Deck()
    player_hand = Hand()
    cpu_hand = Hand()
    
    # Player gets a card, then cpu gets a card until 2 card each.
    for i in range(2):
        game_deck.shuffle()
        player_hand.add_card(game_deck.deal_card())
    
        game_deck.shuffle()
        cpu_hand.add_card(game_deck.deal_card())
    
    in_play = True

def hit():
    global in_play, score
    global game_deck, player_hand
    global player_bust
    
    # if the hand is in play, hit the player
    if in_play:
        game_deck.shuffle()
        player_hand.add_card(game_deck.deal_card())
   
    # if busted, assign a message to outcome, update in_play and score
        if player_hand.get_value() > 21:
            score -= 1
            player_bust = True
            in_play = False 
       
def stand():
    global in_play, score
    global game_deck, player_hand, cpu_hand
    global player_bust, dealer_win, player_win
    
    if player_hand.get_value() > 21:
        if in_play:
            score -= 1
            player_bust = True
            in_play = False
    
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    else:
        if in_play:
            if cpu_hand.get_value() >= player_hand.get_value():
                score -= 1
                dealer_win = True
                in_play = False
            else:
                while cpu_hand.get_value() < player_hand.get_value():
                    game_deck.shuffle()
                    cpu_hand.add_card(game_deck.deal_card())
                    
                if cpu_hand.get_value() > 21:
                    score += 1
                    player_win = True
                elif cpu_hand.get_value() < player_hand.get_value() <= 21:
                    score += 1
                    player_win = True
                else:
                    score -= 1
                    dealer_win = True
                    
                in_play = False

# draw handler    
def draw(canvas):
    global score, in_play
    global player_hand, cpu_hand
    global player_bust, dealer_win, player_win
    
    # Title: Blackjack
    canvas.draw_text("Black", [25, 50], 55, "Black")
    canvas.draw_text("Jack", [105, 80], 55, "Red")
    
    # Cute Diamond
    pt1 = (50/2 + 65, 25/2 + 40)
    pt2 = (25/2 + 65, 50/2 + 40)
    pt3 = (75/2 + 65, 50/2 + 40)
    pt4 = (50/2 + 65, 75/2 + 40)
    canvas.draw_polygon([pt1, pt2], 3, 'Red')
    canvas.draw_polygon([pt1, pt3], 3, 'Red')
    canvas.draw_polygon([pt2, pt4], 3, 'Red')
    canvas.draw_polygon([pt3, pt4], 3, 'Red')
    
    # Score
    canvas.draw_text("Score: " + str(score), [410, 25], 25, "White")
    
    # Player Hand value
    if player_hand.get_value() <= 21:
        canvas.draw_text("Player value: " + str(player_hand.get_value()), [410, 55], 25, "White")
    else:
        canvas.draw_text("Player value: " + str(player_hand.get_value()), [410, 55], 25, "Red")
    
    
    # Player Hand display
    if player_hand.get_value() > 21:
        canvas.draw_text("Player Hand: Bust!", [25, 460], 25, "Red")
    else:
        canvas.draw_text("Player Hand:", [25, 460], 25, "White")
    player_hand.draw(canvas, [25, 475])
    
    # Dealer Hand display
    if cpu_hand.get_value() > 21:
        canvas.draw_text("Dealer Hand: Bust!", [25, 300], 25, "Red")
    else:
        canvas.draw_text("Dealer Hand:", [25, 300], 25, "White")
    cpu_hand.draw(canvas, [25, 315])
    
    # First Card: face down when in play
    if in_play:
        canvas.draw_image(card_back, [CARD_CENTER[0], CARD_CENTER[1]], CARD_SIZE, [60, 362], CARD_SIZE)
    # Dealer Hand Value: "?" when in play
        canvas.draw_text("Dealer value: ?", [410, 85], 25, "White")
    else:
        if cpu_hand.get_value() <= 21:
            canvas.draw_text("Dealer value: " + str(cpu_hand.get_value()), [410, 85], 25, "White")
        else:
            canvas.draw_text("Dealer value: " + str(cpu_hand.get_value()), [410, 85], 25, "Red")
    
    # In play message: Hit or Stand?
    if in_play:
        canvas.draw_text("Hit or Stand?", [200, 190], 40, "White")
    # If player bust
    if player_bust:
        canvas.draw_text("Bust!", [250, 175], 50, "Red")
        canvas.draw_text("New Deal?", [250, 210], 25, "White")
    # If the deal win, not by busting
    elif dealer_win:
        canvas.draw_text("Dealer Win!", [190, 175], 50, "Red")
        canvas.draw_text("New Deal?", [250, 210], 25, "White")
    # If the player win
    elif player_win:
        canvas.draw_text("Player Win!", [190, 175], 50, "Black")
        canvas.draw_text("New Deal?", [250, 210], 25, "White")
        

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()
