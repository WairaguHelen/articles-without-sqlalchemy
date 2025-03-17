class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name should have 2 and 16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category should be a non-empty string")

        self.name = name
        self.category = category

    def articles(self):
        from article import Article
        return [article for article in Article.all_articles if article.magazine == self]

    def article_titles(self):
        articles = self.articles()
        if not articles:
            return None
        return [article.title for article in articles]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def contributing_authors(self):
        author_counts = {}

        for article in self.articles():
            author = article.author
            author_counts[author] = author_counts.get(author, 0) + 1

        print("Author counts", self.name, ":", author_counts)

        return [author for author, count in author_counts.items() if count > 2]