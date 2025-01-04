import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt


def open_file():
    # Open file dialog to select a CSV file
    file_path = filedialog.askopenfilename(
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )
    if file_path:
        plot_data(file_path)


def plot_data(file_path):
    # Read CSV file
    data = pd.read_csv(file_path)

    # Check for signal column and plot
    if 'Signal (V)' in data.columns:
        plt.plot(data['Signal (V)'], label='Step Response')
        plt.title("Step Response Signal")
        plt.xlabel("Time Steps")
        plt.ylabel("Signal (V)")
        plt.legend()
        plt.grid(True)
        plt.show()
    else:
        print("Error: 'Signal (V)' column not found in the CSV file.")


if __name__ == "__main__":
    # Create Tkinter root window
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Open file dialog and plot
    open_file()
