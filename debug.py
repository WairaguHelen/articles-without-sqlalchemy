import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'lib')))

from author import Author
from article import Article
from magazine import Magazine

author = Author("Helen Wairagu")
mag1 = Magazine("Marketing", "Marketing")
mag2 = Magazine("Tech Insider", "Tech")

article1 = Article(author, mag1, "Emerging Tech News")
article2 = Article(author, mag2, "The Tech Baddie Interview")
article3 = Article(author, mag1, "What is the Future of Technology?")
print(mag1.contributing_authors())


print(author.articles())
print(author.magazines()) 

print(mag1.articles()) 
print(mag1.contributors())

print(author.add_article(mag1, "Love the article"))
print(author.topics())
print(mag1.article_titles()) 
print(mag1.contributing_authors()) 