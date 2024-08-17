class Selection_sort:
    def __init__(self, drawing_logic, array):
        self.drawing_logic = drawing_logic
        self.array = array

    def selection_sort_step(self):
        n = len(self.array)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                self.drawing_logic.draw_array(self.array)
                yield (min_index, j, "yellow")
                if self.array[j] < self.array[min_index]:
                    yield (min_index, j, "red")
                    min_index = j
            self.drawing_logic.draw_array(self.array)
            if(min_index != i) and i != n - 2:
                yield (min_index, i, "red")
            self.array[i], self.array[min_index] = self.array[min_index], self.array[i]
            yield (min_index, i, "green")

    def generator(self, sort_generator):
        if sort_generator is None:
            sort_generator = self.selection_sort_step()
        try:
            (i, j, color) = next(sort_generator)
            self.drawing_logic.draw_highlighted_squares(i, j, self.array, color)
            return (False, sort_generator)
        except StopIteration:
            print("Sorting Complete")
            return (True, None)