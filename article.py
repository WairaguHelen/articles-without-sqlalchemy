class Article:
    all_articles = []

    def __init__(self, author, magazine, title):
        self.author = author  
        self.magazine = magazine  
        self.title = title
        self.__class__.all_articles.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        from author import Author
        if isinstance(value, Author):
            self._author = value
        else:
            raise ValueError(f"Make author an instance of the Author class, {type(value)}")

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        from magazine import Magazine 
        if isinstance(value, Magazine):
            self._magazine = value
        else:
            raise ValueError(f"Make Magazine an instance of the Magazine class, {type(value)}")

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str) and 5 <= len(value) <= 50:
            self._title = value
        else:
            raise ValueError("Title needs to be between 5 and 50 characters")

    @classmethod
    def all(cls):
        return cls.all_articles
    
    def __repr__(self):
        return f"Article('{self.title}', Author: {self.author.name}, Magazine: {self.magazine.name})"
