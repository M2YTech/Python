class Book:
    def __init__(self,title, author, year):
        self.title = title
        self.author = author 
        self.year = year

    def display_info(self):
        print(f"The Book {self.title} was written by {self.author} in the {self.year}")

data = Book("Stillness is key", "Ryan Holiday", 2020)
data2 = Book("Ego is the Enemy", "Ryan Holiday", 2015)
data.display_info()