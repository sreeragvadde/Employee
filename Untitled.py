#!/usr/bin/env python
# coding: utf-8

# In[3]:


import tkinter as tk
from tkinter import messagebox

class EmployeeDatabase:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Employee Database")

        # Create frames for input and output
        self.input_frame = tk.Frame(self.root, bg="gray")
        self.input_frame.pack(fill="x")

        self.output_frame = tk.Frame(self.root, bg="gray")
        self.output_frame.pack(fill="both", expand=True)

        # Create input fields
        self.name_label = tk.Label(self.input_frame, text="Name:")
        self.name_label.pack(side="left")

        self.name_entry = tk.Entry(self.input_frame, width=20)
        self.name_entry.pack(side="left")

        self.email_label = tk.Label(self.input_frame, text="Email:")
        self.email_label.pack(side="left")

        self.email_entry = tk.Entry(self.input_frame, width=20)
        self.email_entry.pack(side="left")

        self.department_label = tk.Label(self.input_frame, text="Department:")
        self.department_label.pack(side="left")

        self.department_entry = tk.Entry(self.input_frame, width=20)
        self.department_entry.pack(side="left")

        self.salary_label = tk.Label(self.input_frame, text="Salary:")
        self.salary_label.pack(side="left")

        self.salary_entry = tk.Entry(self.input_frame, width=20)
        self.salary_entry.pack(side="left")

        # Create buttons
        self.add_button = tk.Button(self.input_frame, text="Add Employee", command=self.add_employee)
        self.add_button.pack(side="left")

        self.search_button = tk.Button(self.input_frame, text="Search", command=self.search_employee)
        self.search_button.pack(side="left")

        self.clear_button = tk.Button(self.input_frame, text="Clear", command=self.clear_fields)
        self.clear_button.pack(side="left")

        # Create output area
        self.output_text = tk.Text(self.output_frame, width=40, height=10)
        self.output_text.pack(fill="both", expand=True)

        # Initialize employee database
        self.employees = {}

    def add_employee(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        department = self.department_entry.get()
        salary = self.salary_entry.get()

        if name and email and department and salary:
            self.employees[name] = {"email": email, "department": department, "salary": salary}
            self.output_text.insert("end", f"Added employee: {name}\n")
            self.clear_fields()
        else:
            messagebox.showerror("Error", "Please fill in all fields")

    def search_employee(self):
        name = self.name_entry.get()
        if name in self.employees:
            employee = self.employees[name]
            self.output_text.insert("end", f"Found employee: {name}\n")
            self.output_text.insert("end", f"Email: {employee['email']}\n")
            self.output_text.insert("end", f"Department: {employee['department']}\n")
            self.output_text.insert("end", f"Salary: {employee['salary']}\n")
        else:
            messagebox.showerror("Error", "Employee not found")

    def clear_fields(self):
        self.name_entry.delete(0, "end")
        self.email_entry.delete(0, "end")
        self.department_entry.delete(0, "end")
        self.salary_entry.delete(0, "end")

    def run(self):
        self.root.mainloop()

# Create an instance of the EmployeeDatabase class
db = EmployeeDatabase()

# Run the GUI
db.run()


# In[ ]:




