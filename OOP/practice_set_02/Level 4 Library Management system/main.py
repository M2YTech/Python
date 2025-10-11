class Library:
    def __init__(self):
        self.__private_list = []
    def add_book(self,item):
        self.__private_list.append(item)
        print(f"Book successfully added in the list.")
    def remove_book(self,item):
        self.__private_list.remove(item)
        print(f"Book successfully rmeoved from the list.")
    def display_books(self):
        return self.__private_list

obj = Library()
obj.add_book("Think and grow Rich")
obj.add_book("Psychology of money")
print(obj.display_books())
obj.remove_book("Psychology of money")
print(obj.display_books())