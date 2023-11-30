import tkinter as tk
from tkinter import ttk
from reglaCramer import cramer

def resolver_matriz():
    # Get matrix values from the entry widgets
    matrix_values = [
        [int(entry.get()) for entry in row] 
        for row in matrix_entries
    ]

    # Get X, Y, Z values
    x_value = int(x_entry.get())
    y_value = int(y_entry.get())
    z_value = int(z_entry.get())

    # Perform your matrix resolution or any other logic here
    # For demonstration, let's just print the values
    
    metodo_cramer = cramer(matrix_values[0][0],matrix_values[0][1],matrix_values[0][2],matrix_values[1][0],matrix_values[1][1],matrix_values[1][2],matrix_values[2][0],matrix_values[2][1],matrix_values[2][2],x_value,y_value,z_value)
    
    # Crea la etiqueta
    resultado_etiqueta1 = ttk.Label(root, text=metodo_cramer[0], justify="left", anchor="w")
    resultado_etiqueta2 = ttk.Label(root, text=metodo_cramer[1], justify="left", anchor="w")
    resultado_etiqueta3 = ttk.Label(root, text=metodo_cramer[2], justify="left", anchor="w")

    # Coloca la etiqueta en el grid
    resultado_etiqueta1.grid(row=0, column=6, padx=5, pady=5)
    resultado_etiqueta2.grid(row=1, column=6, padx=5, pady=5)
    resultado_etiqueta3.grid(row=2, column=6, padx=5, pady=5)


# Create the main window
root = tk.Tk()
root.title("Metodo de Cramer")

# Create matrix input
matrix_entries = [
    [ttk.Entry(root, width=5) for _ in range(3)] 
    for _ in range(3)
]

# Place matrix entries in the grid
for i, row in enumerate(matrix_entries):
    for j, entry in enumerate(row):
        entry.grid(row=i, column=j, padx=5, pady=5)

# Create X, Y, Z input entries
x_label = ttk.Label(root, text="X:")
x_entry = ttk.Entry(root, width=5)
y_label = ttk.Label(root, text="Y:")
y_entry = ttk.Entry(root, width=5)
z_label = ttk.Label(root, text="Z:")
z_entry = ttk.Entry(root, width=5)

# Place X, Y, Z entries in the grid
x_label.grid(row=3, column=0, padx=5, pady=5)
x_entry.grid(row=3, column=1, padx=5, pady=5)
y_label.grid(row=3, column=2, padx=5, pady=5)
y_entry.grid(row=3, column=3, padx=5, pady=5)
z_label.grid(row=3, column=4, padx=5, pady=5)
z_entry.grid(row=3, column=5, padx=5, pady=5)

# Create Resolver button
resolver_button = ttk.Button(root, text="Resolver", command=resolver_matriz)
resolver_button.grid(row=4, column=2, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()