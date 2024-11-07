import csv
import random
import tkinter as tk

# Dictionary to map single letters to color names
color_map = {
    'R': 'Red',
    'G': 'Green',
    'B': 'Blue',
    'Y': 'Yellow',
    'P': 'Purple',
    'O': 'Orange',
    'K': 'Pink',
    'A': 'Gray'
}

# Function to generate random RGB values
def generate_rgb():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

# Function to update the color display
def update_color():
    r, g, b = generate_rgb()
    color_display.config(bg=f'#{r:02x}{g:02x}{b:02x}')
    color_display.rgb = (r, g, b)
    color_label.config(text=f"RGB: ({r}, {g}, {b})")

# Function to get user input and write to CSV
def record_color(event=None):
    color_letter = color_entry.get().upper()
    if color_letter in color_map:
        color_name = color_map[color_letter]
        r, g, b = color_display.rgb
        with open('RGBSet.csv', 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([r, g, b, color_name])
        status_label.config(text=f"Recorded: {r},{g},{b},{color_name}")
        update_color()  # Generate a new color after recording
    else:
        status_label.config(text="Invalid input. Please enter a valid letter.")
    color_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("RGB Color Generator")

# Create a frame for the color display
color_display = tk.Frame(root, width=200, height=200)
color_display.pack(pady=20)
color_display.rgb = (0, 0, 0)

# Create a label to show the RGB values
color_label = tk.Label(root, text="RGB: (0, 0, 0)")
color_label.pack(pady=10)

# Create a button to generate a new color
generate_button = tk.Button(root, text="Generate Color", command=update_color)
generate_button.pack(pady=10)

# Create an entry box for user input
color_entry = tk.Entry(root)
color_entry.pack(pady=10)
color_entry.bind("<Return>", record_color)

# Create a label to show the status
status_label = tk.Label(root, text="")
status_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()
