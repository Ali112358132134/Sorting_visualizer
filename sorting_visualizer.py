import numpy as np
from tkinter import ttk
import tkinter as tk
from tkinter import Tk
from drawing_logic import Drawing_logic
from functools import partial
from quick_sort import Quick_sort
from bubble_sort import Bubble_sort
from selection_sort import Selection_sort
from insertion_sort import Insertion_sort


class Sorting_visualizer():
    def __init__(self):
        self.square_width = 20
        self.spacing = 5
        self.canvas_height = 10*self.square_width
        self.canvas_width = 30*self.square_width
        self.window = Tk()
        self.window.title('Sorting visualizer')
        self.canvas = tk.Canvas(self.window, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()
        self.array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
        self.sort_generator = None
        self.drawing_logic = Drawing_logic(self.square_width, self.spacing, self.canvas_height, self.canvas_width, self.window, self.canvas)


    def choose_algorithm(self, value):
        self.selection_frame.pack_forget()
        self.controls_frame.pack()

        self.step_button.config(state="normal")
        self.sort_button.config(state="normal")
        self.stop_button.config(state="normal")
        self.update_button.config(state="normal")

        if value == 1:
            self.sorting_algorithm = Insertion_sort(self.drawing_logic, self.array)
        elif value == 2:
            self.sorting_algorithm = Selection_sort(self.drawing_logic, self.array)
        elif value == 3:
            self.sorting_algorithm = Bubble_sort(self.drawing_logic, self.array)
        else:
            self.sorting_algorithm = Quick_sort(self.drawing_logic, self.array)
        
        self.drawing_logic.draw_array(self.array)

    def update_array(self):
        user_input = self.entry.get()
        try:
            self.array = list(map(int, user_input.replace(',', ' ').split()))
            if len(self.array) < 2:
                raise ValueError("Array too short.")
            self.canvas.delete("all")
            self.drawing_logic.draw_array(self.array)
            self.sort_generator = None
        except ValueError as e:
            print(f"Invalid input: {e}")

    def step_forward(self):
        (stopped, self.sort_generator) = self.sorting_algorithm.generator(self.sort_generator)
        self.window.update()
        if stopped:
            self.sort_button.config(state="normal")
            self.step_button.config(state="normal")
            self.sort_generator = None

    def stop(self):
        global stopped
        stopped = True
        self.sort_button.config(state="normal")
        self.step_button.config(state="normal")

    def run(self):
        global stopped
        stopped = False
        self.sort_button.config(state="disabled")
        self.step_button.config(state="disabled")
        self.window.after(0, self.sort_step)

    def sort_step(self):
        if stopped:
            return
        self.step_forward()
        self.window.after(50, self.sort_step)


    def create_initial_screen(self):
        self.selection_frame = tk.Frame(self.window)
        self.selection_frame.pack(pady=20)

        self.insertion_sort_button = ttk.Button(self.selection_frame, text="insertion sort", command=partial(self.choose_algorithm, 1))
        self.selection_sort_button = ttk.Button(self.selection_frame, text="selection sort", command=partial(self.choose_algorithm, 2))
        self.bubble_sort_button = ttk.Button(self.selection_frame, text="bubble sort", command=partial(self.choose_algorithm, 3))
        self.quick_sort_button = ttk.Button(self.selection_frame, text="quick sort", command=partial(self.choose_algorithm, 4))

        self.insertion_sort_button.pack()
        self.selection_sort_button.pack()
        self.bubble_sort_button.pack()
        self.quick_sort_button.pack()

        self.controls_frame = tk.Frame(self.window)
        
        self.step_button = ttk.Button(self.controls_frame, text="run", command=self.run, state="disabled")
        self.stop_button = ttk.Button(self.controls_frame, text="stop", command=self.stop, state="disabled")
        self.sort_button = ttk.Button(self.controls_frame, text="Step Forward", command=self.step_forward, state="disabled")
        self.entry = ttk.Entry(self.controls_frame, width=50)
        self.update_button = ttk.Button(self.controls_frame, text="Update Array", command=self.update_array, state="disabled")

        self.stop_button.pack(side=tk.LEFT, padx=10)
        self.step_button.pack(side=tk.LEFT, padx=10)
        self.sort_button.pack(side=tk.LEFT, padx=10)
        self.entry.pack(pady=10,side=tk.LEFT)
        self.update_button.pack(side=tk.LEFT, padx=10)





def __main__():
    sorting_visualizer = Sorting_visualizer()
    sorting_visualizer.create_initial_screen()
    np.random.shuffle(sorting_visualizer.array)
    sorting_visualizer.window.mainloop()

if __name__ == "__main__":
    __main__()