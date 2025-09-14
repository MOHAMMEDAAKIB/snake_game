from tkinter import *
import random


GAME_WIDTH = 600
GAME_HEIGHT = 600
SPEED = 100
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#FF9100"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"


class Snake:
    def __init__(self):
        # Initialize the snake's body size and coordinates
        self.body_size = BODY_PARTS # Initial body size
        self.coordinates = [] # List to store the coordinates of each body part
        self.squares = [] # 
        
        # 
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y , x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR , tags="snake")
            self.squares.append(square)

class Food:
    def __init__(self):
        
        # Generate random food coordinates (fix float division issue)
        x = random.randint(0, int(GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, int(GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE
        # Store the food coordinates
        self.coordinates = [x, y]
        # Create the food square on the canvas
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

# Game Logic Functions
def Next_Turn(snake, food):
    x ,y = snake.coordinates[0]
    
    if direction == 'up':
        y -= SPACE_SIZE
    elif direction == 'down':
        y += SPACE_SIZE
    elif direction == 'left':
        x -= SPACE_SIZE
    elif direction == 'right':
        x += SPACE_SIZE
    
    # Wrap around boundaries - snake enters from opposite side
    if x < 0:
        x = GAME_WIDTH - SPACE_SIZE  # Left edge -> Right edge
    elif x >= GAME_WIDTH:
        x = 0  # Right edge -> Left edge
    
    if y < 0:
        y = GAME_HEIGHT - SPACE_SIZE  # Top edge -> Bottom edge
    elif y >= GAME_HEIGHT:
        y = 0  # Bottom edge -> Top edge
    
    snake.coordinates.insert(0, [x, y])
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tags="snake")
    snake.squares.insert(0,square)
    
    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score
        
        score += 1
        
        label.config(text="score : {}".format(score))
        
        canvas.delete("food")
        
        food = Food()
    
    else:
        del snake.coordinates[-1]
    
        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if Check_Collision(snake):
        Game_Over()
        
    else:
        window.after(SPEED, Next_Turn, snake, food)
            
            
# UI Functions
def Change_Direction(new_direction):
    
    global direction
    
    if new_direction == 'left':
        if  direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if  direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if  direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if  direction != 'up':
            direction = new_direction
            
# Collision Functions
def Check_Collision(snake):
    x, y = snake.coordinates[0]
    
    # Only check for self-collision (snake hitting its own body)
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            print("GAME OVER")
            return True
    return False
# Game Over Function
def Game_Over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                      font=('consolas', 70), text="GAME OVER", fill="red", tag="gameover")
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2 + 100,
                      font=('consolas', 20), text=f"Final Score: {score}", fill="white", tag="finalscore")



window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text="Score: {}".format(score), font=('consolas', 40))
label.pack()
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

# Center the window on the screen
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

# Set the geometry of the window
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: Change_Direction('left'))
window.bind('<Right>', lambda event: Change_Direction('right'))
window.bind('<Up>', lambda event: Change_Direction('up'))
window.bind('<Down>', lambda event: Change_Direction('down'))

# Bindings
snake = Snake()
food = Food()

Next_Turn(snake, food)

window.mainloop()