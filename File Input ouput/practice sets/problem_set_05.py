word = ["Donkey", "local", "heavy"]

with open("practice sets\Donkey.txt") as f:
    st = f.read().lower()

for i in word:
    st = st.replace(i.lower(), "####")

with open("practice sets\Donkey.txt", "w") as f:
    f.write(st)
