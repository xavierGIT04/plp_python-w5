



class Publication:
    def __init__(self, title):
        self.title = title

    def display_info(self):
        print(f"Title: {self.title}")





class Book(Publication) :
    def __init__(self, title, author, isbn):
        super().__init__(title)
        self.author = author
        self.isbn = isbn

    def display_info(self):
        super().display_info()
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")


#initialisation
book1 = Book(title="The Hitchhiker's Guide to the Galaxy",
             author="Douglas Adams",
             isbn="978-0345391803")

book1.display_info()

