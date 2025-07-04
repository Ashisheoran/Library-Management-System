from abc import ABC,abstractmethod
from datetime import datetime

class LibraryItem(ABC):
    @property
    @abstractmethod
    def title(self):
        pass

    @property
    @abstractmethod
    def creator(self):
        pass
    
    @property
    @abstractmethod
    def copies(self):
        pass
    
    @abstractmethod
    def add_copy(self):
        pass
    
    @abstractmethod
    def remove_copy(self):
        pass

    def is_available(self):
        if self.copies > 0:
            return True
        else:
            return False

class Book(LibraryItem):
    def __init__(self,title,creator,copies):
        self.__title = title
        self.__creator = creator
        self.__copies = copies
    @property   
    def title(self):
        return self.__title 
    
    @property
    def creator(self):
        return self.__creator
    
    @property
    def copies(self):
        return self.__copies
    
    @copies.setter
    def add_copy(self):
        self.__copies += 1
        return "A copy of book added"
    
    @copies.setter
    def remove_copy(self):
        if self.__copies > 0:
            self.__copies -= 1

    def __str__(self):
        return f"Book: {self.__title}\n Author: {self.__creator} \n copies: {self.__copies}"

class Library:
    def __init__(self):
        self.item = []
    def display_item(self):
        for item in self.item:
            return item
        
class ManageItem:
    def add_item(self,lib:Library,item:LibraryItem):
        if item is None:
            return "No item selected"
        if lib is None:
            return "No library selected"
        lib.item.append(item)
        return "Item added successfully"
    
    def borrow_item(self,lib:Library,item:LibraryItem):
        if item is None:
            return "No item selected"
        if lib is None:
            return "No Library selected"
        if item in lib.item:
            if item.is_available():
                item.remove_copy()
                return "Item borrowed successfully"
            else:
                return "Item currently not available"
        else:
            return "This item is not in library"
    
    def return_item(self,lib:Library,item:LibraryItem):
        if item is None:
            return "No item selected"
        if lib is None:
            return "No Library selected"
        if item in lib.item:
            item.add_copy()
            return "Item returned successfully"
        else:
            return "Item is not of this library"

book1 = Book("Think Grow and Rich","Nepolean Hill",2)
library = Library()
manager = ManageItem()

print(manager.add_item(library,book1))
print(library.display_item())
