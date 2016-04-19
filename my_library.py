

#define a class which has the most common attributes of all your Library items.
class LibraryItem():
    def __init__(self, author, title, year_published, central_theme, item_keywords):
        self.author = author
        self.title = title
        self.year_published = year_published
        self.central_theme = central_theme
        self.item_keywords = item_keywords
    def readed(self):
        if item_readed == "Y":
            print("You have readed this book.")
        else:
            print("You haven't readed the book.")


#define a book
class BookItem(LibraryItem):
    def __init__(self, author, title, year_published, central_theme, item_keywords, rating):
        LibraryItem.__init__(self, author, title, year_published, central_theme, item_keywords)
        self.rating = rating

#define an article
class ArticleItem(LibraryItem):
    def __init__(self, author, title, year_published, central_theme, item_keywords, book_coordonator, book_title):
        LibraryItem.__init__(self, author, title, year_published, central_theme, item_keywords)
        self.book_coordonator = book_coordonator
        self.book_title = book_title

book1 = BookItem("Alexander Schmemann", "Dead, where is thy sting?", 2009, "resurrection", ["resurrection", "dead", "christian"], 10)
book2 = BookItem("Thierry Jansen", "The inner solution.", 2013, "")
