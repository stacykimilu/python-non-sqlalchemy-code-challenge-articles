class ImmutablePropertyError(Exception):
    """Exception raised when attempting to modify an immutable property."""
    pass


class Article:
    all = []

    def __init__(self, author, magazine, title):
        self._validate_author(author)
        self._validate_magazine(magazine)
        self._validate_title(title)

        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)

    def _validate_title(self, title):
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        if not (5 <= len(title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters")

    def _validate_author(self, author):
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of Author")

    def _validate_magazine(self, magazine):
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be an instance of Magazine")

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise ImmutablePropertyError("Title cannot be changed")

    @property
    def author(self):
        return self._author

    @classmethod
    def articles(cls):
        return cls.all

    @author.setter
    def author(self, value):
        self._validate_author(value)
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        self._validate_magazine(value)
        self._magazine = value


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise ImmutablePropertyError("Name is immutable")

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.articles():
            return None
        return list(set(magazine.category for magazine in self.magazines()))


class Magazine:
    _all_magazines = []

    def __init__(self, name, category):
        self._validate_name(name)
        self._validate_category(category)

        self._name = name
        self._category = category
        Magazine._all_magazines.append(self)

    def _validate_name(self, name):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")

    def _validate_category(self, category):
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._validate_name(value)
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._validate_category(value)
        self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        articles = self.articles()
        return [article.title for article in articles] if articles else None

    def contributing_authors(self):
        # Find all contributing authors (regardless of number of articles)
        return list(set(article.author for article in self.articles()))

    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        # Find magazines with the most articles
        top_count = max(len(magazine.articles()) for magazine in cls._all_magazines)
        return next(magazine for magazine in cls._all_magazines if len(magazine.articles()) == top_count)
