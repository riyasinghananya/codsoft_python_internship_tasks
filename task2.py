import tkinter as tk
import math
import matplotlib.pyplot as plt

memory = 0
dark_mode = True

root = tk.Tk()
root.title("Super Pro Scientific Calculator")
root.geometry("900x650")
root.configure(bg="#0f0f0f")
root.resizable(False, False)

# ---------------- ENTRY ---------------- #

entry = tk.Entry(root, font=("Segoe UI", 24),
                 bg="#1f1f1f", fg="white",
                 insertbackground="white",
                 bd=0, justify="right")
entry.place(x=20, y=20, width=550, height=70)

# ---------------- HISTORY ---------------- #

history = tk.Text(root, font=("Consolas", 12),
                  bg="#1f1f1f", fg="white", bd=0)
history.place(x=600, y=20, width=270, height=580)

# ---------------- BASIC FUNCTIONS ---------------- #

def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get().replace("^", "**")
        result = eval(expression)
        history.insert(tk.END, f"{expression} = {result}\n")
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# ---------------- SCIENTIFIC ---------------- #

def scientific(func):
    try:
        value = float(entry.get())
        result = func(value)
        history.insert(tk.END, f"{func._name_}({value}) = {result}\n")
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.insert(tk.END, "Error")

def factorial():
    try:
        value = int(entry.get())
        result = math.factorial(value)
        history.insert(tk.END, f"{value}! = {result}\n")
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.insert(tk.END, "Error")

# ---------------- MEMORY ---------------- #

def memory_add():
    global memory
    memory += float(entry.get())

def memory_sub():
    global memory
    memory -= float(entry.get())

def memory_recall():
    entry.delete(0, tk.END)
    entry.insert(tk.END, memory)

def memory_clear():
    global memory
    memory = 0

# ---------------- GRAPH ---------------- #

def plot_graph():
    try:
        expr = entry.get()
        x = list(range(-10, 11))
        y = [eval(expr.replace("^","**")) for x in x]
        plt.plot(x, y)
        plt.title(f"Graph of {expr}")
        plt.grid()
        plt.show()
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Graph Error")

# ---------------- MODE ---------------- #

def toggle_mode():
    global dark_mode
    dark_mode = not dark_mode
    if dark_mode:
        root.configure(bg="#0f0f0f")
        entry.configure(bg="#1f1f1f", fg="white")
        history.configure(bg="#1f1f1f", fg="white")
    else:
        root.configure(bg="#f2f2f2")
        entry.configure(bg="white", fg="black")
        history.configure(bg="white", fg="black")

# ---------------- BUTTON STYLE ---------------- #

def create_button(frame, text, cmd, r, c, neon="#00ffcc"):
    btn = tk.Button(frame, text=text, command=cmd,
                    font=("Segoe UI", 12, "bold"),
                    bg="#1f1f1f", fg=neon,
                    activebackground=neon,
                    activeforeground="black",
                    width=7, height=2, bd=0)
    btn.grid(row=r, column=c, padx=6, pady=6)

    def on_enter(e): btn.config(bg=neon, fg="black")
    def on_leave(e): btn.config(bg="#1f1f1f", fg=neon)

    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

# ---------------- MAIN BUTTONS ---------------- #

frame = tk.Frame(root, bg="#0f0f0f")
frame.place(x=20, y=110)

buttons = [
    ('7', lambda: click('7')), ('8', lambda: click('8')),
    ('9', lambda: click('9')), ('/', lambda: click('/')),
    ('4', lambda: click('4')), ('5', lambda: click('5')),
    ('6', lambda: click('6')), ('', lambda: click('')),
    ('1', lambda: click('1')), ('2', lambda: click('2')),
    ('3', lambda: click('3')), ('-', lambda: click('-')),
    ('0', lambda: click('0')), ('.', lambda: click('.')),
    ('^', lambda: click('^')), ('+', lambda: click('+')),
]

r = c = 0
for text, cmd in buttons:
    create_button(frame, text, cmd, r, c)
    c += 1
    if c > 3:
        c = 0
        r += 1

# ---------------- SCIENTIFIC FRAME ---------------- #

sci = tk.Frame(root, bg="#0f0f0f")
sci.place(x=20, y=420)

sci_buttons = [
    ('sin', lambda: scientific(lambda x: math.sin(math.radians(x)))),
    ('cos', lambda: scientific(lambda x: math.cos(math.radians(x)))),
    ('tan', lambda: scientific(lambda x: math.tan(math.radians(x)))),
    ('log', lambda: scientific(math.log10)),
    ('√', lambda: scientific(math.sqrt)),
    ('x²', lambda: scientific(lambda x: x**2)),
    ('!', factorial),
    ('π', lambda: click(str(math.pi))),
    ('e', lambda: click(str(math.e))),
    ('=', calculate),
    ('C', clear),
    ('📊', plot_graph),
    ('🌗', toggle_mode),
    ('M+', memory_add),
    ('M-', memory_sub),
    ('MR', memory_recall),
    ('MC', memory_clear),
]

r = c = 0
for text, cmd in sci_buttons:
    create_button(sci, text, cmd, r, c, "#ff00ff")
    c += 1
    if c > 5:
        c = 0
        r += 1

root.mainloop()