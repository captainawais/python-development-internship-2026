import tkinter as tk
from PIL import Image, ImageTk
import random
import winsound
import os
import sys

# ================= RESOURCE PATH =================
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# ================= WINDOW =================
window = tk.Tk()
window.title("Dice Roller 🎲")
window.geometry("500x500")
window.configure(bg="#000814")  # dark bg

# ================= LOAD IMAGES =================
dice_images = []

for i in range(1, 7):
    path = resource_path(f"images/dice{i}.png")

    img = Image.open(path)
    img = img.resize((130, 130), Image.LANCZOS)

    dice_images.append(ImageTk.PhotoImage(img))

# ================= MAIN FRAME =================
main_frame = tk.Frame(window, bg="#000814")
main_frame.pack(expand=True)

# ================= DICE FRAME =================
dice_frame = tk.Frame(main_frame, bg="#000814")
dice_frame.pack(pady=40)

dice1_label = tk.Label(dice_frame, bg="white", bd=5, relief="ridge")
dice1_label.grid(row=0, column=0, padx=20)

dice2_label = tk.Label(dice_frame, bg="white", bd=5, relief="ridge")
dice2_label.grid(row=0, column=1, padx=20)

# ================= SOUND =================
def play_sound():
    try:
        winsound.PlaySound(
            resource_path("sound.wav"),
            winsound.SND_FILENAME | winsound.SND_ASYNC
        )
    except:
        print("Sound not working")

# ================= ANIMATION =================
def animate_roll(count=10):
    if count > 0:
        d1 = random.choice(dice_images)
        d2 = random.choice(dice_images)

        dice1_label.config(image=d1)
        dice2_label.config(image=d2)

        dice1_label.image = d1
        dice2_label.image = d2

        # slight bounce effect
        dice_frame.pack_configure(pady=40 + (10 - count))

        window.after(70, lambda: animate_roll(count - 1))
    else:
        dice_frame.pack_configure(pady=40)

# ================= ROLL FUNCTION =================
def roll_dice():
    play_sound()
    animate_roll()

# ================= BUTTON =================
roll_btn = tk.Button(
    main_frame,
    text="🎲 Roll Dice",
    command=roll_dice,
    font=("Segoe UI", 14, "bold"),
    bg="#4da3ff",
    fg="white",
    padx=25,
    pady=12,
    border=0,
    activebackground="#357bd8",
    cursor="hand2"
)

roll_btn.pack(pady=20)  # bottom padding

# ================= FOOTER =================
footer = tk.Label(
    window,
    text="Powered by TechFactOfficial • Developed by EngrAwais",
    bg="#000814",
    fg="white",
    font=("Segoe UI", 10)
)

footer.pack(side="bottom", pady=10)

# ================= INITIAL LOAD =================
roll_dice()

window.mainloop()