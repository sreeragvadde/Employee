# Employee Database

This project is a simple graphical user interface (GUI) application for managing an employee database using the `tkinter` library in Python. The application allows you to add, search, and clear employee records.

## Features

- Add new employee records with name, email, department, and salary.
- Search for existing employee records by name.
- Clear input fields after adding or searching for an employee.
- Display employee information in a text area.

## Requirements

- Python 3.x
- `tkinter` library (usually included with Python)

## Usage

1. Save the script to a file, e.g., `EmployeeDatabase.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is saved.
4. Run the script using the following command:

    ```sh
    python EmployeeDatabase.py
    ```

5. The GUI window will open, allowing you to interact with the employee database.

## How to Use the GUI

1. **Add Employee**:
    - Enter the employee's name, email, department, and salary in the respective input fields.
    - Click the "Add Employee" button to add the employee to the database.
    - The employee's information will be displayed in the output area, and the input fields will be cleared.

2. **Search Employee**:
    - Enter the employee's name in the "Name" input field.
    - Click the "Search" button to search for the employee in the database.
    - If the employee is found, their information will be displayed in the output area. If not, an error message will be shown.

3. **Clear Fields**:
    - Click the "Clear" button to clear all input fields.

## Code Overview

The main components of the script are:

- **EmployeeDatabase Class**: Manages the GUI and employee database.
    - `__init__`: Initializes the GUI components and employee database.
    - `add_employee`: Adds a new employee to the database.
    - `search_employee`: Searches for an employee in the database.
    - `clear_fields`: Clears the input fields.
    - `run`: Runs the GUI main loop.
