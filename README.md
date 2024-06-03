# Monte-Carlo-Simulation
Individual Project

## Description
This Monte Carlo Simulation calculates the value of PI. The program was created as a TkInter GUI. When the user clicks the 'Run Simulation' button, a bunch of darts will be "thrown" at the target on the left side. After the darts have been drawn, the program will calculate an approximate value for PI.

<img width="617" alt="image" src="https://github.com/TamsynE/Monte-Carlo-Simulation/assets/93171379/7661d661-4cdb-4fbf-87a2-746f2d2d95ce">

## Details
The GUI App is built on TkInter and implemented using a simple Python class. 

### Important Components
- the constructor
- a handler for the "Run Simulation" button
- a handler for the "Clear Simulation" button.

### Configuration Settings
- ttk.Checkbutton that enables/disables animation (if animation is on, you'll see the darts appear one at a time; if animation is off, then the darts will all appear at once as soon as the 'Run Simulation" button is clicked).
- tk.Scale that allows the user to choose a range betwen 10 and 1000 darts to throw.
- ttkCombobox that provides a variety of colors to draw the hits with.
- ttkCombobox that provides a selection of colors to draw the misses with .
- tk.Button for running the simulation.
- tk.Button for clearing the dartboard and output box.
- tk.Entry that is readonly and displays the final calculated value for PI.
