import pytest
from article import Article
from author import Author
from magazine import Magazine


def test_article_initialization():
    author = Author("Helen Wairagu")
    mag1 = Magazine("Marketing", "Marketing")
    
    article = Article(author, mag1, "Emerging Tech News")
    
    assert article.author == author
    assert article.magazine == mag1
    assert article.title == "Emerging Tech News"

def test_article_title_validation():
    author = Author("Helen Wairagu")
    mag1 = Magazine("Marketing", "Marketing")
    
    with pytest.raises(ValueError):
        Article(author, mag1, "A")  
    with pytest.raises(ValueError):
        Article(author, mag1, "The title should be within the limit of 50 characters")

def test_article_author_assignment():
    author1 = Author("Helen Wairagu")
    author2 = Author("Roslyn Nelly")
    mag1 = Magazine("Marketing", "Marketing")
    
    article = Article(author1, mag1, "Emerging Tech News")
    
    article.author = author2 
    assert article.author == author2

def test_article_magazine_assignment():
    author = Author("Helen Wairagu")
    mag1 = Magazine("Marketing", "Marketing")
    mag2 = Magazine("Tech Insider", "Tech")
    
    article = Article(author, mag1, "Emerging Tech News")
    
    article.magazine = mag2
    assert article.magazine == mag2
