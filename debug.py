import sys
import os

from author import Author
from magazine import Magazine
from article import Article

author = Author("Helen Wairagu")
mag1 = Magazine("Marketing", "Marketing")
mag2 = Magazine("Tech Insider", "Tech")

article1 = Article(author, mag1, "Emerging Tech News")
article2 = Article(author, mag2, "The Tech Baddie Interview")
article3 = Article(author, mag1, "What is the Future of Technology?")

print("Contributing Authors:", mag1.contributing_authors())  
print("Author's Articles:", author.articles())  
print("Author's Magazines:", author.magazines())  

print("Magazine 1 Articles:", mag1.articles())  
print("Magazine 1 Contributors:", mag1.contributors())  

new_article = author.add_article(mag1, "Love the article")
print("New Article Title:", new_article.title) 

print("Author's Topic Areas:", author.topic_areas())  
print("Magazine 1 Article Titles:", mag1.article_titles())  

print("Magazine 1 Contributing Authors:", mag1.contributing_authors())

