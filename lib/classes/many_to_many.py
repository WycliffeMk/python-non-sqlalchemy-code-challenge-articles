class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

    def title(self, title):
          if isinstance(title, str) and 5 <= len(title) <= 50:
            self.title = title
            raise ValueError("Title must be a string and between 5 and 50 characters")
    

    def author(self):
        return self.author
       
    def set_author(self, author):
        if isinstance(author, Author):
            self.author = author
        else:
            raise ValueError("Author must be an instance of Author class")
        
        
class Author():
    def __init__(self, name):
        self.name = name

    def articles(self):
        return self.articles

        pass

    def magazines(self):
        return list({article.magazine for article in self._articles})
        pass

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        self._articles.append(new_article)
        return new_article
        pass

    def topic_areas(self):
        if not self._articles:
            return None
        return list({article.magazine.category for article in self._articles})
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        return self.articles
        pass

    def contributors(self):
        return list({article.author for article in self._articles})
        pass

    def article_titles(self):
        if not self._articles:
            return None
        return list({article.title for article in self._articles})
        pass

    def contributing_authors(self):
        from collections import Counter
        author_counts = Counter(article.author for article in self._articles)
        return [author for author, count in author_counts.items() if count > 2] or None
        pass