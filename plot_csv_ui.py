import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
import os  # For directory handling


def open_file():
    # Open file dialog to select a CSV file, start in the current directory
    file_path = filedialog.askopenfilename(
        initialdir=os.getcwd(),  # Start in the current directory
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )
    if file_path:
        plot_data(file_path)


def plot_data(file_path):
    # Read CSV file
    data = pd.read_csv(file_path)

    # Check if the CSV is empty
    if data.empty:
        print("Error: The selected file is empty.")
        return

    # Check if the first column is 'Time' or similar
    x_column = data.columns[0]
    if 'time' in x_column.lower():
        x_data = data[x_column]
        y_columns = data.columns[1:]  # Exclude the first column
    else:
        x_data = data.index  # Use index if no 'Time' column
        y_columns = data.columns

    # Plot each column as a subplot in the same window
    num_columns = len(y_columns)
    fig, axes = plt.subplots(num_columns, 1, figsize=(10, 5 * num_columns), sharex=True)

    # If there is only one y-column, axes may not be iterable
    if num_columns == 1:
        axes = [axes]

    # Plot each column in its subplot
    for i, column in enumerate(y_columns):
        axes[i].plot(x_data, data[column], label=f"{column} Data")
        axes[i].set_title(f"{column}")
        axes[i].set_xlabel(x_column if 'time' in x_column.lower() else "Index / Time Steps")
        axes[i].set_ylabel(column)
        axes[i].legend()
        axes[i].grid(True)

    plt.tight_layout()  # Adjust layout to prevent overlap
    plt.show()  # Display all plots in one window


if __name__ == "__main__":
    # Create Tkinter root window
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Open file dialog and plot
    open_file()
