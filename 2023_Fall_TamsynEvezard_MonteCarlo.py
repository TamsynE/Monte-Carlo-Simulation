# Monte Carlo Simulation
# Throws darts randomly at a dart board and calculates the value of PI
# file: CSC314_2023_Fall_TamsynEvezard_MonteCarlo.py
# author: Tamsyn Evezard

import tkinter as tk
from tkinter import ttk
import random
import math
import time

class MonteCarlo:
    def __init__(self, root_frame):
        '''Sets up GUI window'''
        self.window = root_frame
        self.window.wm_title('Monte Carlo Simulation')
        self.window.resizable(False, False)
        self.totalDarts = 0
        self.dartsInCircle = 0
        self.dartsOutside = 0
        self.pi = tk.StringVar(value='')
        self.dart_count = tk.IntVar(value=50)
        self.hit_color = tk.StringVar(value='cornflowerblue')
        self.miss_color = tk.StringVar(value='darkseagreen')
        self.animate = tk.BooleanVar(value=True)

        self.cvs_drawing = tk.Canvas(self.window, width=300, height=300, highlightthickness=1, highlightbackground='steelblue', bg='white') 
        self.btn_clear = tk.Button(self.window, text='Clear Simulation', command=self.clear_handler) 
        self.btn_run = tk.Button(self.window, text='Run Simulation', command=self.run_handler) 

        self.lbl_dartcount = tk.Label(self.window, text='Dart count:') 
        self.scl_dartcount = tk.Scale(self.window, variable=self.dart_count, from_=10, to=1000, orient=tk.HORIZONTAL) 
        self.lbl_hitcolor = tk.Label(self.window, text='Hit color:') 
        self.lbl_misscolor = tk.Label(self.window, text='Miss color:')
        self.cmb_hitcolor = ttk.Combobox(self.window, textvariable=self.hit_color, state=['readonly'], values=['cornflowerblue', 'lightcoral', 'chartreuse'])
        self.cmb_misscolor = ttk.Combobox(self.window, textvariable=self.miss_color, state=['readonly'], values=['darkseagreen', 'chocolate', 'crimson'])
        self.chk_animate = ttk.Checkbutton(self.window, text='Animate Simulation', variable=self.animate, onvalue=True, offvalue=False)
        self.lbl_pi = tk.Label(self.window, text='Calculated pi:')
        self.pi_ = tk.Entry(self.window, textvariable=self.pi, state=['disabled'])
        self.cvs_drawing.create_oval(0, 0, 300, 300, fill='white')
        self.cvs_drawing.create_line(0, 150, 300, 150, fill='azure3')
        self.cvs_drawing.create_line(150, 0, 150, 300, fill='azure3')

        # Layout the different widgets in the window
        self.chk_animate.grid(row=2, column=3, padx=10)
        self.cvs_drawing.grid(row=2, column=1, rowspan=6, padx=10, pady=10) 
        self.btn_run.grid(row=6, column=2, padx=10, pady=10)
        self.btn_clear.grid(row=6, column=3, padx=10, pady=10) 
        self.lbl_dartcount.grid(row=3, column=2) 
        self.scl_dartcount.grid(row=3, column=3, pady=10, padx=10) 
        self.lbl_hitcolor.grid(row=4, column=2) 
        self.cmb_hitcolor.grid(row=4, column=3, padx=10)
        self.lbl_misscolor.grid(row=5, column=2)
        self.cmb_misscolor.grid(row=5, column=3, padx=10)
        self.lbl_pi.grid(row=7, column=2, padx=10, pady=10)
        self.pi_.grid(row=7, column=3, padx=10, pady=10)

        return

    def run_handler(self):
        ''' Handles the 'Run' button with or without animation'''
        def darts_with_delay(i):
            '''Throws darts randomly at the board one at a time with pi updating after each throw'''
            if i < self.dart_count.get():
                x = random.uniform(-1, 1) 
                y = random.uniform(-1, 1) 
                
                # Transform the coordinates from a -1,-1,1,1 world to the canvas size
                x_scale = (self.cvs_drawing.winfo_width()) / (2) 
                y_scale = (-self.cvs_drawing.winfo_height()) / (2)

                # Use the scaling factors to convert the old coords to the new coords
                x_new = (x + 1) * x_scale
                y_new = (y - 1) * y_scale

                distance = math.sqrt(x**2 + y**2)

                if abs(distance) <= 1: # inside circle
                    self.cvs_drawing.create_oval(x_new-2, y_new-2, x_new+2, y_new+2, fill=self.hit_color.get())
                    self.dartsInCircle = self.dartsInCircle +1
                else: #outside circle
                    self.cvs_drawing.create_oval(x_new-2, y_new-2, x_new+2, y_new+2, fill=self.miss_color.get())
                    self.dartsOutside = self.dartsOutside +1

                self.totalDarts = self.totalDarts +1

                # Calculate pi and directly update the Entry widget
                pi = 4 * self.dartsInCircle / self.totalDarts
                pi = round(pi, 2)
                self.pi.set(pi)

                # animate darts with sleep
                self.window.update()
                time.sleep(0.1)
                darts_with_delay(i+1)
            return
        
        def darts_no_delay():
            '''Throws darts randomly at the board and updates pi after all throws'''
            for i in range(self.dart_count.get()):
                x = random.uniform(-1, 1) 
                y = random.uniform(-1, 1) 

                x_scale = (self.cvs_drawing.winfo_width()) / (2) 
                y_scale = (-self.cvs_drawing.winfo_height()) / (2)

                x_new = (x + 1) * x_scale
                y_new = (y - 1) * y_scale

                distance = math.sqrt(x**2 + y**2)

                if abs(distance) <= 1:
                    self.cvs_drawing.create_oval(x_new-2, y_new-2, x_new+2, y_new+2, fill=self.hit_color.get())
                    self.dartsInCircle = self.dartsInCircle + 1
                else:
                    self.cvs_drawing.create_oval(x_new-2, y_new-2, x_new+2, y_new+2, fill=self.miss_color.get())
                    self.dartsOutside = self.dartsOutside +1
                    
            self.totalDarts = self.totalDarts + self.dart_count.get()

            pi = 4 * self.dartsInCircle / self.totalDarts
            pi = round(pi, 2)
            self.pi.set(pi)
            return
    
        # Handles animation
        if self.animate.get():
            darts_with_delay(0)
        else:
            darts_no_delay()
        return
    
    def clear_handler(self):
        ''' Handles the 'Clear' button by erasing all darts. '''
        self.cvs_drawing.delete('all')
        self.last_x = self.last_y = None
        self.totalDarts = 0
        self.dartsInCircle = 0
        self.dartsOutside = 0
        self.cvs_drawing.create_oval(0, 0, 300, 300, fill='white')
        self.cvs_drawing.create_line(0, 150, 300, 150, fill='azure3')
        self.cvs_drawing.create_line(150, 0, 150, 300, fill='azure3')
        print(f"CLEARED")
        return
    
# GUI window and enter main event loop
window = tk.Tk()
app = MonteCarlo(window)
window.mainloop()
        