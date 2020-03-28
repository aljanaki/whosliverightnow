
from app import db
from app.models import Artist
import csv

youtubers = open("youtube_channels.csv")
youtubeIDs = set()
youtreader = csv.reader(youtubers, delimiter=';', quotechar='"')
count = 0
for row in youtreader:
    if row[0] not in youtubeIDs:
        youtubeIDs.add(row[0])
        a = Artist(youtube_ID=row[0], youtube_name=row[1], youtube_subscribers = row[2])
        #db.session.add(a)
        count+=1

print("{} unique artists inserted in database".format(count))
db.session.commit()