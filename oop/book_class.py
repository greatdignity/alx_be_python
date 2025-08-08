class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        """Initialize a Book instance."""
        self.title = title
        self.author = author
        self.year = int(year)

    def __str__(self) -> str:
        """Return a readable description of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __del__(self) -> None:
        """Called when the object is about to be destroyed."""
        print(f"Deleting {self.title}")

    def __repr__(self) -> str:
        """Return an unambiguous string that can be used to recreate the Book."""
        return f"Book({self.title!r}, {self.author!r}, {self.year})"
