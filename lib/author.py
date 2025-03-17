from article import Article 

class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name should be a non-empty string")
        self._name = name

    @property
    def name(self):
        return self._name

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def articles(self):
        return [article for article in Article.all_articles if article.author == self] 

    def add_magazine(self, name, category):
        from magazine import Magazine
        return Magazine(name, category)
    
    def add_article(self, magazine, title):
        from article import Article
        return Article(self, magazine, title)

    def topics(self):
        if not self.articles():
            return None
        return list(set(magazine.category for magazine in self.magazines()))
