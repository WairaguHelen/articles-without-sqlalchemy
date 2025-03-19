import pytest
from article import Article
from author import Author
from magazine import Magazine

def test_author_initialization():
    author = Author("Helen Wairagu")
    assert author.name == "Helen Wairagu"

def test_author_name_validation():
    with pytest.raises(ValueError):
        Author("") 
    with pytest.raises(ValueError):  
        Author(123)  


def test_author_articles():
    author = Author("Helen Wairagu")
    mag1 = Magazine("Marketing", "Marketing")
    mag2 = Magazine("Tech Insider", "Tech")
    
    article1 = Article(author, mag1, "Emerging Tech News")
    article2 = Article(author, mag2, "The Tech Baddie Interview")
    article3 = Article(author, mag1, "What is the Future of Technology?")
    
    assert set(author.articles()) == {article1, article2, article3}

def test_author_magazines():
    author = Author("Helen Wairagu")
    mag1 = Magazine("Marketing", "Marketing")
    mag2 = Magazine("Tech Insider", "Tech")
    
    Article(author, mag1, "Emerging Tech News")
    Article(author, mag2, "The Tech Baddie Interview")
    Article(author, mag1, "What is the Future of Technology?")
    
    assert set(author.magazines()) == {mag1, mag2}

def test_author_add_article():
    author = Author("Helen Wairagu")
    mag = Magazine("Tech Insider", "Tech")
    article = author.add_article(mag, "AI Trends in 2025")

    assert article.title == "AI Trends in 2025"
    assert article.magazine == mag
    assert article in author.articles()

def test_author_topic_areas():
    author = Author("Helen Wairagu")
    mag1 = Magazine("Marketing", "Marketing")
    mag2 = Magazine("Tech Insider", "Tech")
    
    Article(author, mag1, "Emerging Tech News")
    Article(author, mag2, "The Tech Baddie Interview")
    Article(author, mag1, "What is the Future of Technology?")
    
    assert set(author.topic_areas()) == {"Marketing", "Tech"}

