import tkinter as tk
from tkinter import messagebox, Toplevel
import vlc
import threading
import time

# VLC instance (global so it can be reused)
instance = vlc.Instance()

def play_video_in_popup(num):
    # Create a new pop-up window
    popup = Toplevel(root)
    popup.title("Video Playing...")
    popup.geometry("640x360")
    popup.resizable(False, False)

    # Video frame inside the pop-up
    video_frame = tk.Frame(popup, width=640, height=360, bg="black")
    video_frame.pack()

    # VLC setup
    player = instance.media_player_new()
    media = instance.media_new("intro.mp4")
    player.set_media(media)
    player.set_hwnd(video_frame.winfo_id())
    player.play()

    # Wait for video to finish, then close pop-up and show table
    def wait_and_show():
        time.sleep(1)
        while player.is_playing():
            time.sleep(0.5)
        player.stop()
        popup.destroy()
        show_table(num)

    threading.Thread(target=wait_and_show).start()

def show_table(num):
    output_text.delete('1.0', tk.END)
    for i in range(1, 11):
        output_text.insert(tk.END, f"{num} x {i} = {num * i}\n")
    reset_button.pack(pady=5)

def play_and_process():
    try:
        num = int(entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
        return

    output_text.delete('1.0', tk.END)
    reset_button.pack_forget()
    play_video_in_popup(num)

def reset():
    entry.delete(0, tk.END)
    output_text.delete('1.0', tk.END)
    reset_button.pack_forget()

# Main GUI window
root = tk.Tk()
root.title("Multiplication Table App")
root.geometry("400x400")

tk.Label(root, text="Enter a number:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)
entry.bind("<Return>", lambda event: play_and_process())

tk.Button(root, text="Submit", command=play_and_process).pack(pady=5)

output_text = tk.Text(root, height=12, width=30)
output_text.pack(pady=10)

reset_button = tk.Button(root, text="Try Another Number", command=reset)
reset_button.pack_forget()

root.mainloop()
