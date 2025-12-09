import speech_recognition as sr

print("Available audio input devices:")
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"{index}: {name}")
