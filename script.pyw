import pyglet
from pyglet import image
from pyglet.window import mouse
from pyglet import clock
import math

grid = [[0 for i in range(4)] for j in range(4)]
back_pic = image.load('imgs/back.png')
button_pic = image.load('imgs/button.png')
icon_pic = image.load('imgs/icon.png')
x_pic = image.load('imgs/x.png')
o_pic = image.load('imgs/o.png')
window = pyglet.window.Window(500,495, 'tic-tac-toe', fullscreen=False)
window.set_icon(icon_pic)
can_reset = False
ai,human = 1,2

@window.event
def on_close():
    quit()

@window.event
def on_mouse_press(x, y, button, modifiers):
    global can_reset
    if button == mouse.LEFT:
        if(x >= 43 and x <= 175 and y >= 350 and y <= 472 and grid[0][0] == 0 and can_reset == False):
            grid[0][0] = human; bestMove()
        elif(x >= 180 and x <= 312 and y >= 350 and y <= 472 and grid[0][1] == 0 and can_reset == False):
            grid[0][1] = human; bestMove()
        elif(x >= 317 and x <= 455 and y >= 350 and y <= 472 and grid[0][2] == 0 and can_reset == False):
            grid[0][2] = human; bestMove()
        elif(x >= 38 and x <= 175 and y >= 228 and y <= 346 and grid[1][0] == 0 and can_reset == False):
            grid[1][0] = human; bestMove()
        elif(x >= 182 and x <= 312 and y >= 228 and y <= 346 and grid[1][1] == 0 and can_reset == False):
            grid[1][1] = human; bestMove()
        elif(x >= 316 and x <= 456 and y >= 227 and y  <= 346 and grid[1][2] == 0 and can_reset == False):
            grid[1][2] = human; bestMove()
        elif(x >= 40 and x <= 175 and y >= 100 and y <= 222 and grid[2][0] == 0 and can_reset == False):
            grid[2][0] = human; bestMove()
        elif(x >= 18 and x <= 310 and y >= 100 and y <= 222 and grid[2][1] == 0 and can_reset == False):
            grid[2][1] = human; bestMove()
        elif(x >= 317 and x <= 455 and y >= 100 and y <= 222 and grid[2][2] == 0 and can_reset == False):
            grid[2][2] = human; bestMove()
        elif(x >= 320 and x <= 480 and y >= 25 and y <= 70 and can_reset == True):
            can_reset = False
            for i in range(3):
                for j in range(3):
                    grid[i][j] = 0
            grid[0][0] = ai

def bestMove():
    bestScore = -math.inf
    move_i,move_j = 0, 0
    for i in range(3):
        for j in range(3):
            if(grid[i][j] == 0):
                grid[i][j] = ai
                score = minimax(grid, 0, False)
                grid[i][j] = 0
                if(score > bestScore):
                    bestScore = score
                    move_i = i; move_j = j;
    grid[move_i][move_j] = ai

def checkWinner():
    result = None
    isFull = True
    for i in range(3):
        if(grid[0][i] != 0 and grid[0][i] == grid[1][i] and grid[1][i] == grid[2][i]):
            result = grid[0][i]
            break
        elif(grid[i][0] != 0 and grid[i][0] == grid[i][1] and grid[i][1] == grid[i][2]):
            result = grid[i][0]
            break
    if(grid[0][2] != 0 and grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0]):
        result = grid[0][2]
    if(grid[0][0] != 0 and grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2]):
        result = grid[0][0]
    for i in range(3):
        for j in range(3):
            if(grid[i][j] == 0):
                isFull = False
                break
    if(result != None and result == 1):
        return 'X'
    elif(result != None and result == 2):
        return 'O'
    elif(isFull == True):
        return 'tie'
    else:
        return None
    
scores = {
    'X': 10,
    'O': -10,
    'tie': 0
}

def minimax(board, depth, isMaximizing):
    result = checkWinner();
    if (result != None):
        return scores[result];
    if (isMaximizing):
        bestScore = -math.inf;
        for i in range(3):
          for j in range(3):
            if (board[i][j] == 0):
              board[i][j] = ai;
              score = minimax(board, depth + 1, False);
              board[i][j] = 0;
              bestScore = max(score, bestScore);
        return bestScore;
    else:
        bestScore = math.inf;
        for i in range(3):
          for j in range(3):
            if (board[i][j] == 0):
              board[i][j] = human;
              score = minimax(board, depth + 1, True);
              board[i][j] = 0;
              bestScore = min(score, bestScore);
        return bestScore;

@window.event
def on_draw():
    window.clear()
    back_pic.blit(0, 0, 0)
    x_offset = 350
    for i in range(3):
        y_offset = 45
        for j in range(3):
            if(grid[i][j] == 1):
                x_pic.blit(y_offset, x_offset, 0)
            elif(grid[i][j] == 2):
                o_pic.blit(y_offset, x_offset, 0)
            y_offset += 142
        x_offset -= 123
    if(can_reset == True):
        result = checkWinner()
        label = pyglet.text.Label(result,font_name='Times New Roman',font_size=36,color=(0,0,0, 255),x=window.width//2, y=55,anchor_x='center', anchor_y='center')
        label.draw()
        button_pic.blit(320, 25, 0)
        
def update(self):
    global can_reset
    result = checkWinner()
    if(result != None):
        can_reset = True

grid[0][0] = ai
pyglet.clock.schedule_interval(update, 1/60.0)
pyglet.app.run()
