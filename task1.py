import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Advanced To-Do List")
app.geometry("900x550")

tasks = []

# ---------------- FILE HANDLING ---------------- #

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                task = line.strip()
                tasks.append(task)
        refresh_tasks()
    except:
        pass

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# ---------------- FUNCTIONS ---------------- #

def refresh_tasks(filtered=None):
    task_box.delete("1.0", "end")
    display_list = filtered if filtered is not None else tasks
    for task in display_list:
        task_box.insert("end", f"• {task}\n")
    counter_label.configure(text=f"Total Tasks: {len(display_list)}")

def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        save_tasks()
        refresh_tasks()
        task_entry.delete(0, "end")
    else:
        messagebox.showwarning("Warning", "Enter a task!")

def delete_task():
    selected = task_entry.get()
    if selected in tasks:
        tasks.remove(selected)
        save_tasks()
        refresh_tasks()
        task_entry.delete(0, "end")
    else:
        messagebox.showwarning("Warning", "Type exact task name to delete")

def search_task():
    keyword = search_entry.get()
    filtered = [task for task in tasks if keyword.lower() in task.lower()]
    refresh_tasks(filtered)

# ---------------- UI DESIGN ---------------- #

# Sidebar
sidebar = ctk.CTkFrame(app, width=200)
sidebar.pack(side="left", fill="y")

logo = ctk.CTkLabel(sidebar, text="📝 TO-DO\nMANAGER",
                    font=("Arial", 20, "bold"))
logo.pack(pady=30)

counter_label = ctk.CTkLabel(sidebar, text="Total Tasks: 0",
                             font=("Arial", 14))
counter_label.pack(pady=10)

# Main Area
main_frame = ctk.CTkFrame(app)
main_frame.pack(side="right", expand=True, fill="both", padx=20, pady=20)

task_entry = ctk.CTkEntry(main_frame, width=400, height=40,
                          placeholder_text="Enter new task...")
task_entry.pack(pady=10)

btn_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
btn_frame.pack(pady=10)

add_btn = ctk.CTkButton(btn_frame, text="Add Task",
                        width=140, command=add_task)
add_btn.grid(row=0, column=0, padx=10)

delete_btn = ctk.CTkButton(btn_frame, text="Delete Task",
                           width=140, fg_color="#e74c3c",
                           hover_color="#c0392b",
                           command=delete_task)
delete_btn.grid(row=0, column=1, padx=10)

search_entry = ctk.CTkEntry(main_frame, width=300,
                            placeholder_text="Search task...")
search_entry.pack(pady=10)

search_btn = ctk.CTkButton(main_frame, text="Search",
                           width=120, command=search_task)
search_btn.pack(pady=5)

task_box = ctk.CTkTextbox(main_frame, width=600, height=250)
task_box.pack(pady=20)

load_tasks()
app.mainloop()