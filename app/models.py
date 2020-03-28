from app import db

class Artist(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    spotify_name = db.Column(db.String(64), index=True, unique=False)
    spotify_ID = db.Column(db.String(128), index=True, unique=True)
    youtube_name = db.Column(db.String(120)) #YouTube doesn't constrain them to be unique, for instance there are two very popular Bollywood Classics channels.
    youtube_ID = db.Column(db.String(120),  unique=True)
    facebook_ID = db.Column(db.String(128))
    twitch_ID = db.Column(db.String(128),  unique=True)
    genre = db.Column(db.String(30),  unique=True)
    youtube_subscribers = db.Column(db.Integer)
    def __repr__(self):
        return '<Artist {}>'.format(self.spotify_name)


class User(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), index=True, unique=True)
    spotify_ID = db.Column(db.String(120), index=True, unique=True)
    def __repr__(self):
        return '<User {}>'.format(self.email)

class UserGenres(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    user_ID = db.Column(db.Integer)
    genre = db.Column(db.String(30))
    def __repr__(self):
        return '<User {}>'.format(self.email)


class UserArtists(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    user_ID = db.Column(db.Integer)
    artist_ID = db.Column(db.String(128), db.ForeignKey('artist.ID'))

