class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        
class Author:
    def __init__(self, name):
        self.name = name
        self.articles = []

    def name(self):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Author name must be a string")
        return self.name
        pass

    def articles(self):
        return self.articles
        pass

    def magazines(self):
        return list(set(article.magazine for article in self.articles))
        pass

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self.articles.append(article)
        return article
        pass

    def topic_areas(self):
        if not self.articles
            return None
        return list(set(article.magazine.category for article in self.articles))
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.articles = []
        

    def articles(self):
        return self.articles
        pass

    def contributors(self):
        return list(set(article.author for article in self.articles))
        pass

    def article_titles(self):
        if not title in self.articles:
            return None
        return list(set(article.title for article in self.articles))
        pass

    def contributing_authors(self):
        authors_counter = {}
        for article in self.articles():
            author = article.author
            authors_counter[author] = authors_counter.get(author, 0) + 1

        contributing_authors = [author for author, count in authors_counter.items() if count > 2]
        return contributing_authors if contributing_authors else None

        pass