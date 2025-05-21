import base64

video_path = "video.mp4"
output_py_file = "video_blob.py"

with open(video_path, "rb") as video_file:
    encoded_string = base64.b64encode(video_file.read()).decode('utf-8')

with open(output_py_file, "w") as f:
    f.write("video_data = '''{}'''".format(encoded_string))
