import csv
import tkinter as tk
from tkinter import messagebox

# Create the main window of the application
window = tk.Tk()
window.title("Attendance Management System")

# Create the labels and entry widgets for employee information
tk.Label(window, text="Employee ID:").grid(row=0, column=0, sticky='w')
employee_id_entry = tk.Entry(window)
employee_id_entry.grid(row=0, column=1)

tk.Label(window, text="Name:").grid(row=1, column=0, sticky='w')
name_entry = tk.Entry(window)
name_entry.grid(row=1, column=1)

tk.Label(window, text="Department:").grid(row=2, column=0, sticky='w')
department_entry = tk.Entry(window)
department_entry.grid(row=2, column=1)

# Create the buttons to register and input attendance
def register_employee():
    # Retrieve the employee information from the entry widgets
    employee_id = employee_id_entry.get()
    name = name_entry.get()
    department = department_entry.get()

    # Write the employee information to the CSV file
    with open('employee_records.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([employee_id, name, department])

    # Display a success message to the user
    messagebox.showinfo("Registration Successful", "Employee registered successfully!")

def input_attendance():
    # Retrieve the employee ID from the user
    employee_id = employee_id_entry.get()

    # Check if the employee ID is in the employee records file
    with open('employee_records.csv', mode='r') as file:
        reader = csv.reader(file)
        found = False
        for row in reader:
            if row[0] == employee_id:
                found = True
                break

    # If the employee ID is in the records file, update the attendance records
    if found:
        with open('attendance_records.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([employee_id])

        # Display a success message to the user
        messagebox.showinfo("Attendance Input Successful", "Attendance input successful!")
    else:
        # Display an error message to the user
        messagebox.showerror("Employee Not Found", "Employee ID not found in records!")

register_employee_button = tk.Button(window, text="Register Employee", command=register_employee)
register_employee_button.grid(row=3, column=0)

input_attendance_button = tk.Button(window, text="Input Attendance", command=input_attendance)
input_attendance_button.grid(row=3, column=1)

# Start the main loop of the application
window.mainloop()
