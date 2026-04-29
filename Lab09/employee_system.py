import tkinter as tk
from tkinter import ttk, messagebox
import re


# ================= MAIN WINDOW =================
root = tk.Tk()
root.title("Employee System")
root.geometry("750x520")
root.configure(bg=BG)

# ================= HEADER =================
header = tk.Frame(root, bg=PRIMARY, height=60)
header.pack(fill="x")

title = tk.Label(header,
                 text="Employee Registration & Salary System",
                 font=("Arial", 18, "bold"),
                 bg=PRIMARY,
                 fg="white")
title.pack(pady=15)

# ================= NOTEBOOK =================
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both", padx=15, pady=10)

# ================= TAB 1 =================
frame1 = tk.Frame(notebook, bg=BG)
notebook.add(frame1, text=" Registration ")

card1 = tk.Frame(frame1, bg=CARD, bd=0, highlightthickness=3, highlightbackground=ACCENT)
card1.pack(pady=20, padx=80, fill="both")

tk.Label(card1, text="Employee Registration",
         font=("Arial", 16, "bold"),
         bg=CARD, fg=PRIMARY).pack(pady=10)

form = tk.Frame(card1, bg=CARD)
form.pack(pady=10)

labels = ["First Name", "Last Name", "Email", "Department"]
for i, text in enumerate(labels):
    tk.Label(form, text=text,
             bg=CARD, fg=PRIMARY,
             font=("Arial", 10, "bold"))\
        .grid(row=i, column=0, sticky="w", pady=8, padx=10)

# Inputs with highlight background
first_name = tk.Entry(form, width=25, bg=HIGHLIGHT, relief="flat")
last_name = tk.Entry(form, width=25, bg=HIGHLIGHT, relief="flat")
email = tk.Entry(form, width=25, bg=HIGHLIGHT, relief="flat")

department = ttk.Combobox(form,
                          values=["HR", "IT", "Finance", "Marketing"],
                          width=22)
department.set("Select Department")

first_name.grid(row=0, column=1, pady=5)
last_name.grid(row=1, column=1, pady=5)
email.grid(row=2, column=1, pady=5)
department.grid(row=3, column=1, pady=5)

# VALIDATION
def validate():
    fn, ln, em, dept = first_name.get(), last_name.get(), email.get(), department.get()

    if fn == "" or ln == "" or em == "" or dept == "Select Department":
        messagebox.showerror("Error", "All fields are required!")
        return False

    if fn.isnumeric() or ln.isnumeric():
        messagebox.showerror("Error", "Names cannot contain numbers!")
        return False

    if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", em):
        messagebox.showerror("Error", "Invalid Email!")
        return False

    return True

# BUTTONS
btn_frame = tk.Frame(card1, bg=CARD)
btn_frame.pack(pady=15)

def submit():
    if validate():
        messagebox.showinfo("Success", "Employee Registered Successfully!")

def clear():
    first_name.delete(0, tk.END)
    last_name.delete(0, tk.END)
    email.delete(0, tk.END)
    department.set("Select Department")

tk.Button(btn_frame, text="Submit",
          bg=SUCCESS, fg="white",
          activebackground="#20a65a",
          font=("Arial", 10, "bold"),
          width=12, command=submit)\
    .grid(row=0, column=0, padx=10)

tk.Button(btn_frame, text="Clear",
          bg=WARNING, fg="white",
          activebackground="#e6892f",
          font=("Arial", 10, "bold"),
          width=12, command=clear)\
    .grid(row=0, column=1, padx=10)

# ================= TAB 2 =================
frame2 = tk.Frame(notebook, bg=BG)
notebook.add(frame2, text=" Salary ")

card2 = tk.Frame(frame2, bg=CARD, highlightthickness=3, highlightbackground=SUCCESS)
card2.pack(pady=40, padx=120, fill="both")

tk.Label(card2, text="Salary Calculator",
         font=("Arial", 16, "bold"),
         bg=CARD, fg=PRIMARY).pack(pady=15)

salary_form = tk.Frame(card2, bg=CARD)
salary_form.pack()

tk.Label(salary_form, text="Daily Wage", bg=CARD, fg=PRIMARY)\
    .grid(row=0, column=0, pady=10, padx=10)

tk.Label(salary_form, text="Working Days", bg=CARD, fg=PRIMARY)\
    .grid(row=1, column=0, pady=10, padx=10)

daily_wage = tk.Entry(salary_form, bg=HIGHLIGHT, relief="flat")
working_days = tk.Entry(salary_form, bg=HIGHLIGHT, relief="flat")

daily_wage.grid(row=0, column=1)
working_days.grid(row=1, column=1)

result = tk.Label(card2, text="Total Salary: ",
                  font=("Arial", 12, "bold"),
                  bg=CARD, fg=PRIMARY)
result.pack(pady=10)

def calculate():
    try:
        wage = float(daily_wage.get())
        days = int(working_days.get())

        if wage < 0 or days < 0:
            messagebox.showerror("Error", "Enter positive values!")
            return

        total = wage * days
        result.config(text=f"Total Salary: {total}")

    except:
        messagebox.showerror("Error", "Invalid input!")

def reset():
    daily_wage.delete(0, tk.END)
    working_days.delete(0, tk.END)
    result.config(text="Total Salary: ")

btn2 = tk.Frame(card2, bg=CARD)
btn2.pack(pady=10)

tk.Button(btn2, text="Calculate",
          bg=ACCENT, fg="white",
          activebackground="#357ABD",
          font=("Arial", 10, "bold"),
          width=12, command=calculate)\
    .grid(row=0, column=0, padx=10)

tk.Button(btn2, text="Reset",
          bg=WARNING, fg="white",
          activebackground="#e6892f",
          font=("Arial", 10, "bold"),
          width=12, command=reset)\
    .grid(row=0, column=1, padx=10)

tk.Button(card2, text="Exit",
          bg=DANGER, fg="white",
          activebackground="#c0392b",
          font=("Arial", 10, "bold"),
          width=15, command=root.quit)\
    .pack(pady=10)

# ================= RUN =================
root.mainloop()
