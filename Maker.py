"""
=======================================
Training Data Builder
Author: Mir Ali Tohidi
Date: 2024.10.25
Description: Feel free to use and modify!
This code is released without any copyright claims.
=======================================
"""
import os
import tkinter as tk
import numpy as np

# Reading the dir. of the code
code_directory=os.path.dirname(os.path.abspath(__file__))
code_directory = "C:\\Users\\HP\\Documents\\py\\ANN" 
# Print code .dir
print(code_directory)

# changing dir.
os.chdir(code_directory)




"""
=======================================
Creating a Tkinter window name=tk_1 !!!
=======================================
"""

# Window
tk_1 = tk.Tk()
tk_1.title("ENTER!")

# List for selected celss
selected_cells=[]

# Using Frames
grid_frame = tk.Frame(tk_1)
# Place it in the window
grid_frame.pack()

# Generating the grids!
grid_button=[]
for row in range(10):
    temp_row=[] # Used temp. for each row
    for col in range(10):
        temp_button=tk.Button(grid_frame, width='4', height='2',  command=lambda r=row, c=col: cell_click(r, c))    # Using lambda function for cell clicking
        temp_button.grid(row=row,column=col)
        temp_row.append(temp_button)
    grid_button.append(temp_row)

# Selected Cells to Binary function
def binary(selected_cells):
    data = np.zeros(100, dtype=int)
    for num in selected_cells:
        data[num]=1
    return data
    
    
# Define saving to txt file selections.txt
def save_txt(selected_cells, x):      
    with open("selections.txt" , "a") as file:    # Open txt file with append mode
        input=binary(selected_cells)
        input_str=",".join(map(str, input))  # Comma seperated strings
        file.write(f'{x},{input_str}\n')
            

# Label assigning functions
def assign_label(x):
    global selected_cells   # Aquiring selected cells
    if not selected_cells:  # If it is empty
        print('No selected cells')
        return
    
    print(f"You selected cells {selected_cells} as {x}")
    
    # Save the selection and label to the text
    save_txt(selected_cells, x)
    
    # Reset buttons
    for col in range(10):
        for row in range(10):
            grid_button[row][col].config(bg='SystemButtonFace')
   
    # Cleaning the selected cells list
    selected_cells.clear() 
       
# Function when clicking on a cell
def cell_click(row, col):
    print(f"You pressed {row},{col}")        
    linearized_cell_index=linearize(row, col)
    if linearized_cell_index not in selected_cells:
        selected_cells.append(linearized_cell_index)
        grid_button[row][col].config(bg='blue') # Change the color to blue when selected  
    else:
        selected_cells.remove(linearized_cell_index)
        grid_button[row][col].config(bg='SystemButtonFace') # Change back the color
    
# Linearizer
def linearize(row, col):
    return row * 10 + col 




# Creating the X and O buttons
buttons_frame=tk.Frame(tk_1)
buttons_frame.pack(pady=25, padx=50)

# Button to label the selected as X
x_button=tk.Button(buttons_frame, text="X", height=2, width=10, bg='violet', command=lambda :assign_label('x'))
x_button.pack(side='left', padx=20)

# Button to label the selected as O
o_button=tk.Button(buttons_frame, text="O", height=2, width=10, bg='green', command= lambda :assign_label('o'))
o_button.pack(side='right', padx=20)


 
"""
=======================================
Run tk_1!!!
=======================================
"""

# Run the main loop
tk_1.mainloop()

