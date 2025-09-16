class Snake:
    def __init__(self, canvas, body_parts, snake_color, space_size):
        # Initialize the snake's body size and coordinates
        self.body_size = body_parts # Initial body size
        self.coordinates = [] # List to store the coordinates of each body part
        self.squares = [] # List to store canvas squares
        
        # Create initial body parts
        for i in range(0, body_parts):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y , x + space_size, y + space_size, fill=snake_color , tags="snake")
            self.squares.append(square)