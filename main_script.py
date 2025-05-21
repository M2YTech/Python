import os
import subprocess
import platform
import base64
import video_blob

def write_video():
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    video_path = os.path.join(desktop_path, "temp_video.mp4")
    with open(video_path, "wb") as f:
        f.write(base64.b64decode(video_blob.video_data))
    return video_path

def play_video(file_path):
    if platform.system() == "Windows":
        os.startfile(file_path)
    elif platform.system() == "Darwin":
        subprocess.call(["open", file_path])
    else:
        subprocess.call(["xdg-open", file_path])

if __name__ == "__main__":
    video_file = write_video()
    play_video(video_file)
