class Quick_sort:
    def __init__(self, drawing_logic, array):
        self.drawing_logic = drawing_logic
        self.array = array
    
    def swap(self, index1, index2):
        tmp = self.array[index1]
        self.array[index1] = self.array[index2]
        self.array[index2] = tmp

    def quick_sort_step(self, i, j):
        if i >= j:
            return self.array
        else:
            pivot_index = (i + j) // 2
            pivot = self.array[pivot_index]
            self.drawing_logic.draw_array(self.array)
            self.drawing_logic.draw_square(pivot, pivot_index, self.array, "orange")
            self.drawing_logic.draw_index(i, j, self.array[i], self.array[j], pivot, self.array)
            yield (i, j, "orange")
            self.drawing_logic.draw_square(self.array[i], i, self.array, "lightblue")
            yield (pivot_index, j, "yellow")
            self.swap(j, pivot_index)
            yield (pivot_index, j, "yellow")
            tmp_j, tmp_i = j - 1, i
            while tmp_i <= tmp_j:
                self.drawing_logic.draw_array(self.array)
                self.drawing_logic.draw_index(tmp_i, tmp_j, self.array[tmp_i], self.array[tmp_j], pivot, self.array)
                yield (tmp_i, tmp_j, "yellow")
                if self.array[tmp_i] > pivot and self.array[tmp_j] < pivot:
                    yield (tmp_i, tmp_j, "red")
                    self.swap(tmp_i, tmp_j)
                    yield (tmp_i, tmp_j, "green")
                    tmp_i += 1
                    tmp_j -= 1
                elif self.array[tmp_i] <= pivot:
                    tmp_i += 1
                elif self.array[tmp_j] >= pivot:
                    tmp_j -= 1
            self.drawing_logic.draw_array(self.array)
            self.drawing_logic.draw_index(tmp_i, tmp_j, self.array[tmp_i], self.array[tmp_j], pivot, self.array)
            yield (tmp_i, j, "yellow")
            self.swap(tmp_i, j)
            yield (tmp_i, j, "green")
            yield from self.quick_sort_step(i, tmp_i - 1)
            yield from self.quick_sort_step(tmp_i + 1, j)

    def generator(self, sort_generator):
        if sort_generator is None:
            sort_generator = self.quick_sort_step(0, len(self.array) - 1)
        try:
            (i, j, color) = next(sort_generator)
            self.drawing_logic.draw_highlighted_squares(i, j, self.array, color)
            return (False, sort_generator)
        except StopIteration:
            print("Sorting Complete")
            return (True, None)