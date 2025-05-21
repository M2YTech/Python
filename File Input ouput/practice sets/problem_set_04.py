word = "Donkey"
with open("practice sets\Donkey.txt") as f:
    st= f.read()
    new=st.lower().replace("donkey", "####")

with open("practice sets\Donkey.txt", "w") as f:
    f.write(new)

