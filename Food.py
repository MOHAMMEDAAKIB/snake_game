
import random

class Food:
    def __init__(self, canvas, game_width, game_height, space_size, food_color):
        
        # Generate random food coordinates (fix float division issue)
        x = random.randint(0, int(game_width/space_size)-1) * space_size
        y = random.randint(0, int(game_height/space_size)-1) * space_size
        # Store the food coordinates
        self.coordinates = [x, y]
        # Create the food square on the canvas
        canvas.create_oval(x, y, x + space_size, y + space_size, fill=food_color, tag="food")
