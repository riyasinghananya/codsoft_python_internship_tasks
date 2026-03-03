import customtkinter as ctk
import secrets
import string

# ================= APP SETUP =================
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Pro Password Generator")
app.geometry("650x700")
app.resizable(False, False)

# ================= TITLE =================
title = ctk.CTkLabel(app,
                     text="Password Generator Pro",
                     font=("Segoe UI", 28, "bold"))
title.pack(pady=(30, 10))

subtitle = ctk.CTkLabel(app,
                        text="Generate secure and professional passwords instantly",
                        font=("Segoe UI", 14))
subtitle.pack(pady=(0, 20))

# ================= CARD FRAME =================
card = ctk.CTkFrame(app,
                    corner_radius=20,
                    fg_color=("#1f1f1f", "#1f1f1f"))
card.pack(padx=40, pady=10, fill="both", expand=True)

# ================= PASSWORD ENTRY =================
password_entry = ctk.CTkEntry(card,
                              height=55,
                              font=("Segoe UI", 20),
                              justify="center")
password_entry.pack(pady=25, padx=40, fill="x")
password_entry.configure(show="*")

# ================= SHOW/HIDE =================
show_var = ctk.BooleanVar()

def toggle_password():
    password_entry.configure(show="" if show_var.get() else "*")

ctk.CTkCheckBox(card,
                text="Show Password",
                variable=show_var,
                command=toggle_password).pack()

# ================= LENGTH =================
length_label = ctk.CTkLabel(card,
                            text="Password Length: 12",
                            font=("Segoe UI", 14))
length_label.pack(pady=(20, 5))

def update_length(value):
    length_label.configure(text=f"Password Length: {int(value)}")

length_slider = ctk.CTkSlider(card,
                              from_=6,
                              to=40,
                              command=update_length)
length_slider.set(12)
length_slider.pack(padx=60)

# ================= OPTIONS =================
options_frame = ctk.CTkFrame(card, fg_color="transparent")
options_frame.pack(pady=20)

upper_var = ctk.BooleanVar(value=True)
lower_var = ctk.BooleanVar(value=True)
number_var = ctk.BooleanVar(value=True)
symbol_var = ctk.BooleanVar(value=True)

ctk.CTkCheckBox(options_frame, text="Uppercase (A-Z)", variable=upper_var).grid(row=0, column=0, padx=20, pady=8)
ctk.CTkCheckBox(options_frame, text="Lowercase (a-z)", variable=lower_var).grid(row=0, column=1, padx=20, pady=8)
ctk.CTkCheckBox(options_frame, text="Numbers (0-9)", variable=number_var).grid(row=1, column=0, padx=20, pady=8)
ctk.CTkCheckBox(options_frame, text="Symbols (!@#$)", variable=symbol_var).grid(row=1, column=1, padx=20, pady=8)

# ================= STRENGTH =================
strength_bar = ctk.CTkProgressBar(card, width=400)
strength_bar.pack(pady=(10, 5))
strength_bar.set(0)

strength_label = ctk.CTkLabel(card, text="Strength: -")
strength_label.pack()

# ================= GENERATE =================
def generate_password():
    length = int(length_slider.get())
    characters = ""

    if upper_var.get():
        characters += string.ascii_uppercase
    if lower_var.get():
        characters += string.ascii_lowercase
    if number_var.get():
        characters += string.digits
    if symbol_var.get():
        characters += "!@#$%^&*()_+"

    if characters == "":
        password_entry.delete(0, "end")
        password_entry.insert(0, "Select at least one option")
        return

    password = ''.join(secrets.choice(characters) for _ in range(length))

    password_entry.delete(0, "end")
    password_entry.insert(0, password)

    # Smart Strength Logic
    score = 0
    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if upper_var.get() and lower_var.get():
        score += 1
    if number_var.get():
        score += 1
    if symbol_var.get():
        score += 1

    strength = score / 5
    strength_bar.set(strength)

    if strength < 0.4:
        strength_label.configure(text="Strength: Weak 🔴")
    elif strength < 0.8:
        strength_label.configure(text="Strength: Medium 🟡")
    else:
        strength_label.configure(text="Strength: Strong 🟢")

# ================= COPY =================
def copy_password():
    app.clipboard_clear()
    app.clipboard_append(password_entry.get())

# ================= BUTTONS =================
button_frame = ctk.CTkFrame(card, fg_color="transparent")
button_frame.pack(pady=25)

ctk.CTkButton(button_frame,
              text="Generate",
              width=180,
              height=45,
              font=("Segoe UI", 14, "bold"),
              command=generate_password).grid(row=0, column=0, padx=15)

ctk.CTkButton(button_frame,
              text="Copy",
              width=180,
              height=45,
              font=("Segoe UI", 14),
              command=copy_password).grid(row=0, column=1, padx=15)

app.mainloop()