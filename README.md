# P3 Code Challenge: Articles

## Description
This project models a simple domain for an Author-Magazine-Article relationship using Python classes. The goal is to establish clear relationships where:
- **Authors** write multiple **Articles**.
- **Articles** belong to a single **Magazine**.
- **Magazines** contain multiple **Articles** from different **Authors**.

## Features
- Create **Authors**, **Magazines**, and **Articles**.
- Retrieve all articles by an **Author**.
- Retrieve all magazines an **Author** has contributed to.
- Retrieve all articles in a **Magazine**.
- Get unique contributing **Authors** for a **Magazine**.
- Enforce constraints (e.g., magazine names between 2 and 16 characters).

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/P3_Code_Challenge_Articles.git
   ```
2. Navigate to the project folder:
   ```sh
   cd P3_Code_Challenge_Articles
   ```
3. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
4. Install dependencies (if any):
   ```sh
   pip install -r requirements.txt
   ```

## Usage
Run the debug script to test functionality:
```sh
python debug.py
```

### Example
```python
# Creating an author, magazine, and articles
author = Author("Helen Wairagu")
magazine = Magazine("Marketing", "Marketing")
article1 = Article(author, mag1, "Emerging Tech News")
article2 = Article(author, mag2, "The Tech Baddie Interview")

# Getting articles by an author
print(author.articles())  # [Article1, Article2]

# Getting magazines an author has contributed to
print(author.magazines())  # [Magazine]

# Getting article titles in a magazine
print(magazine.article_titles())  # ['The Wonders of Space', 'New Discoveries in Space']
```

## Project Structure
```
P3_Code_Challenge_Articles/
│-- lib/
│   ├── author.py      # Author class
│   ├── magazine.py    # Magazine class
│   ├── article.py     # Article class
│-- debug.py          # Script to test functionality
│-- README.md         # Project documentation
```

## Troubleshooting
If you encounter module import errors, ensure you're running the script from the project root:
```sh
python debug.py
```
If circular imports occur, check your import statements and consider using **importing inside methods** instead of at the top.

## Contributing
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit changes (`git commit -m 'Added feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## License
This project is licensed under the MIT License.

