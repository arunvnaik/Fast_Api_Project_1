# Import List from typing to define a list of Book objects
from typing import List

# Import the Book Pydantic model (used to define the data structure)
from models import Book

# A fake database using a simple list that stores Book objects
# In real-world apps, this would be replaced by a real database like PostgreSQL
books_db: List[Book] = []
