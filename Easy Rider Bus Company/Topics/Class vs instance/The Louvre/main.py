class Painting:
    museum = "Louvre"

    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year

    def __str__(self):
        return f'"{self.title}" by {self.artist} ({self.year}) hangs in the {Painting.museum}.'


title = input()
artist = input()
year = input()
painting = Painting(title, artist, year)
print(painting)
