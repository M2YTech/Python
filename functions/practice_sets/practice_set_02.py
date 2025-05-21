def cel_to_feh(n):
    return (n*9/5)+32

n = float(input("Enter temprature: "))
print(f"The temperature in fahrenheit is {cel_to_feh(n)} °F ")
    