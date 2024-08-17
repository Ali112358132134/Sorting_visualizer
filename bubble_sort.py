class Bubble_sort:
    def __init__(self, drawing_logic, array):
        self.drawing_logic = drawing_logic
        self.array = array

    def bubble_sort_step(self):
        n = len(self.array)
        for i in range(n):
            for j in range(0, n - i - 1):
                self.drawing_logic.draw_array(self.array)
                yield (j, j + 1, "yellow")
                if self.array[j] > self.array[j + 1]:
                    yield (j, j + 1, "red")
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    yield (j, j + 1, "green")
                else:
                    yield (j, j + 1, "green")

    def generator(self, sort_generator):
        if sort_generator is None:
            sort_generator = self.bubble_sort_step(self.array)
        try:
            (i, j, color) = next(sort_generator)
            self.drawing_logic.draw_highlighted_squares(i, j, self.array, color)
            return (False, sort_generator)
        except StopIteration:
            print("Sorting Complete")
            return (True, None)