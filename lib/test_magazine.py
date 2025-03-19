import pytest
from article import Article
from author import Author
from magazine import Magazine


def test_magazine_initialization():
    mag = Magazine("Marketing", "Marketing")
    assert mag.name == "Marketing"
    assert mag.category == "Marketing"

def test_magazine_name_validation():
    with pytest.raises(ValueError):
        Magazine("A", "Marketing") 
    with pytest.raises(ValueError):
        Magazine("ExtremelyLongName", "Marketing") 

def test_magazine_category_validation():
    with pytest.raises(ValueError):
        Magazine("Marketing", "")  
    with pytest.raises(ValueError):  
        Magazine("Marketing", 123)


def test_magazine_articles():
    author = Author("Helen Wairagu")
    mag1 = Magazine("Marketing", "Marketing")
    
    article1 = Article(author, mag1, "Emerging Tech News")
    article2 = Article(author, mag1, "What is the Future of Technology?")
    
    assert set(mag1.articles()) == {article1, article2}

def test_magazine_contributors():
    author = Author("Helen Wairagu")
    mag1 = Magazine("Marketing", "Marketing")
    mag2 = Magazine("Tech Insider", "Tech")
    
    Article(author, mag1, "Emerging Tech News")
    Article(author, mag2, "The Tech Baddie Interview")
    
    assert set(mag1.contributors()) == {author}

def test_magazine_article_titles():
    author = Author("Helen Wairagu")
    mag1 = Magazine("Marketing", "Marketing")
    
    Article(author, mag1, "Emerging Tech News")
    Article(author, mag1, "What is the Future of Technology?")
    
    assert set(mag1.article_titles()) == {"Emerging Tech News", "What is the Future of Technology?"}

def test_magazine_contributing_authors():
    author = Author("Helen Wairagu")
    mag1 = Magazine("Marketing", "Marketing")
    
    Article(author, mag1, "Emerging Tech News")
    Article(author, mag1, "What is the Future of Technology?")
    
    assert mag1.contributing_authors() == [author]
