# control.python.helper  

A lightweight Python helper library for control engineering projects. This repository contains scripts for plotting, data analysis, and signal validation, making it easier to visualize and process control system outputs.  

## Features  
- 📊 **CSV Plotting Tool** – Easily select and visualize CSV data through a simple UI.  
- 🛠️ **Utilities for Control Systems** – Helper scripts for RL circuits, PID tuning, and motion profiling.  

## Requirements  
- Python 3.10+  
- Virtual environment (`venv`)  

## Installation  
```bash
# Clone the repository
git clone https://github.com/YOUR_GITHUB/control.python.helper.git

# Create and activate virtual environment
python -m venv plot-env
source plot-env/bin/activate  # On Windows: plot-env\Scripts\activate

# Install dependencies
pip install -r requirements.txt



# Some useful commands

##  Activate the Virtual Environment

Windows:
```bash
plot-env\Scripts\activate
```

## Execute
```bash
python plot_csv_ui.py
```


## Step 4: Save Requirements (Optional but Recommended)
To make the project reproducible, export the installed packages:

```bash
pip freeze > requirements.txt
```
## Step 5: Running the Script in the Virtual Environment
```bash
python plot_csv_ui.py
```


## Deactivate the Virtual Environment
Once done, deactivate the virtual environment:

```bash
deactivate
```