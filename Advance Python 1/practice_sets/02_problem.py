list = [1,2,34,43,54,35,643,3545]

for index, item in enumerate(list):
    if(index in [2,4,6]):
        print(f"The item number at index {index} is {item}")