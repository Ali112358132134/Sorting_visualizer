class Insertion_sort:
    def __init__(self, drawing_logic, array):
        self.drawing_logic = drawing_logic
        self.array = array

    def insertion_sort_step(self):
        for i in range(1, len(self.array)):
            key = self.array[i]
            j = i - 1
            while j >= 0:
                self.drawing_logic.draw_array(self.array)
                yield (j + 1, j, "yellow")
                if key > self.array[j]:
                    yield (j + 1, j, "green")
                    break
                yield (j, j + 1, "red")
                self.array[j + 1] = self.array[j]
                self.array[j] = key
                yield (j, j + 1, "green")
                j -= 1

    def generator(self, sort_generator):
        if sort_generator is None:
            sort_generator = self.insertion_sort_step()
        try:
            (i, j, color) = next(sort_generator)
            self.drawing_logic.draw_highlighted_squares(i, j, self.array, color)
            return (False, sort_generator)
        except StopIteration:
            print("Sorting Complete")
            return (True, None)