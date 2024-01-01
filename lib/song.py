class Song:

    all = []
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.all.append(self)
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count[self.artist] = 1

    def add_to_genres(genre):
        if not genre in Song.genres:
            Song.genres.append(genre)

    def add_to_artists(artist):
        if not artist in Song.artists:
            Song.artists.append(artist)


