# Import BaseModel from pydantic to define data models
from pydantic import BaseModel

# Define a Book schema (data structure) using Pydantic
class Book(BaseModel):
    id: int            # Unique ID of the book (e.g., 1, 2, 3)
    title: str         # Title of the book (e.g., "Django Basics")
    author: str        # Author name (e.g., "Arun")
    year: int          # Year of publication (e.g., 2024)
