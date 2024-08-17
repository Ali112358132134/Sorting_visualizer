
class Drawing_logic:
    def __init__(self, sqaure_width, spacing, canvas_height, canvas_width, window, canvas):
        self.square_width = sqaure_width
        self.spacing = spacing
        self.canvas_height = canvas_height
        self.canvas_width = canvas_width
        self.window = window
        self.window.title('Sorting visualizer')
        self.canvas = canvas
        self.canvas.pack()

    def get_square_position(self, index, array):
        # Calculate total width of squares and spacing
        total_width = len(array) * self.square_width + (len(array) - 1) * self.spacing 
        # Calculate starting x-coordinate for centering
        start_x = (self.canvas_width - total_width) // 2
        x0 = start_x + index * (self.square_width + self.spacing)
        x1 = x0 + self.square_width
        return x0, x1

    def draw_highlighted_squares(self, index1, index2, array, color="lightblue"):
        self.draw_square(array[index1], index1, array, color)
        self.draw_square(array[index2], index2, array, color)
        
    def draw_square(self, value, index, array, color):
        x0, x1 = self.get_square_position(index, array)
        y0 = self.canvas_height//2 - self.square_width
        y1 = self.canvas_height//2
        self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
        self.canvas.create_text((x0 + x1)//2, (y0 + y1)//2, text=str(value))

    def draw_index(self, index_i, index_j, value_i, value_j, pivot, array, color="black"):
        self.canvas.delete("index_text")
        x0= self.canvas_width // len(array)
        y1 = self.canvas_height // 2
        self.canvas.create_text(x0, y1 + 15, text=f"index_i: {index_i}, value_i: {value_i}", fill=color, tags='index_text', anchor='w')
        self.canvas.create_text(x0, y1 + 30, text=f"index_j: {index_j}, value_j: {value_j}", fill=color, tags='index_text', anchor='w')
        self.canvas.create_text(x0, y1 + 45, text=f"pivot: {pivot}", fill=color, tags='index_text', anchor='w')

    def draw_array(self, array):
        for i, value in enumerate(array):
            self.draw_square(value, i, array, "lightblue")