class Article:
    all_articles = [] 

    def __init__(self, author, magazine, title):
        from author import Author
        from magazine import Magazine

        if not isinstance(author, Author):
            raise ValueError("author is not an instance of Author")
        if not isinstance(magazine, Magazine):
            raise ValueError("magazine is not an instance of Magazine")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title should have 5 and 50 characters")

        self._author = author 
        self._title = title
        self._magazine = magazine

        Article.all_articles.append(self)

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    @property
    def title(self):
        return self._title
