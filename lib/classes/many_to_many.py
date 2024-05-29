
class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        if not isinstance(new_title, str):
            raise TypeError("The title must be a string")
        if not (5 <= len(new_title) <= 50):
            raise ValueError("Title characters must be between 5 and 50")
        
        self._title = new_title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author
        else:
            raise TypeError("Author must be an instance of Author")

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine
        else:
            raise TypeError("Magazine must be an instance of Magazine")


class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("The name must be a string")
        if len(name) == 0:
            raise ValueError("Author's name cannot be empty")
        self.name = name

    def articles(self):
        return [article for article in Article.all if self == article.author]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        topic_areas = list({magazine.category for magazine in self.magazines()})
        if topic_areas:
            return topic_areas
        else:
            return None


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str):
            raise TypeError("Magazine name must be a string")
        if not (2 <= len(name) <= 16):
            raise ValueError("The name should be between 2 and 16 characters long")
        if not isinstance(category, str):
            raise TypeError("Magazine category must be a string")
        if len(category) == 0:
            raise ValueError("Magazine category must not be empty")
        
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Name must be a string")
        if not (2 <= len(new_name) <= 16):
            raise ValueError("Name must be between 2 and 16 characters")
        
        self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str):
            raise TypeError("Category must be a string")
        if len(new_category) == 0:
            raise ValueError("Category must not be empty")
        
        self._category = new_category

    def articles(self):
        return [article for article in Article.all if self == article.magazine]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        article_titles = [article.title for article in self.articles()]
        if article_titles:
            return article_titles
        else:
            return None

    def contributing_authors(self):
        authors = {}
        list_of_authors = []
        for article in self.articles():
            if article.author in authors:
                authors[article.author] += 1
            else:
                authors[article.author] = 1

        for author in authors:
            if authors[author] >= 2:
                list_of_authors.append(author)

        if list_of_authors:
            return list_of_authors
        else:
            return None


