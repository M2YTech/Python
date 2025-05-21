import tkinter as tk
import vlc
import time
import threading
from tkinter import messagebox

# VLC setup
instance = vlc.Instance()
player = instance.media_player_new()

# Function to play video and then show table
def play_video_and_show_table(event=None):
    try:
        num = int(entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
        return

    # Play video
    media = instance.media_new("intro.mp4")
    player.set_media(media)
    player.set_hwnd(video_frame.winfo_id())
    player.play()

    # Start wait and show logic in separate thread
    threading.Thread(target=wait_for_video_and_show_table, args=(num,)).start()

# Wait for video to finish, then show table
def wait_for_video_and_show_table(num):
    time.sleep(1)  # Ensure video starts
    while player.is_playing():
        time.sleep(0.5)

    player.stop()

    # Switch view from video to table
    video_frame.pack_forget()
    table_output.pack(pady=10)
    reset_button.pack(pady=5)

    # Show multiplication table
    table_output.delete('1.0', tk.END)
    for i in range(1, 11):
        table_output.insert(tk.END, f"{num} x {i} = {num * i}\n")

# Reset everything to allow another number
def reset_app():
    table_output.pack_forget()
    reset_button.pack_forget()
    entry.delete(0, tk.END)
    video_frame.pack(pady=10)

# GUI setup
root = tk.Tk()
root.title("Multiplication Table with Video")
root.geometry("640x500")

entry_label = tk.Label(root, text="Enter a number:")
entry_label.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)
entry.bind("<Return>", play_video_and_show_table)

play_button = tk.Button(root, text="Generate Table", command=play_video_and_show_table)
play_button.pack(pady=5)

video_frame = tk.Frame(root, width=640, height=360, bg="black")
video_frame.pack(pady=10)

table_output = tk.Text(root, height=12, width=40)
table_output.pack_forget()

reset_button = tk.Button(root, text="Try Another Number", command=reset_app)
reset_button.pack_forget()

root.mainloop()
