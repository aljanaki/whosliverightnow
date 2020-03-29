# whosliverightnow
This is the project created during a COVID-19 hackathon.

It is a mashup of music-related APIs, that allows a person to get notified about life-streams of his favourite artists.


### Installation guidelines

After cloning the repo run: 
```
python3 -m venv flaskaws
source flaskaws/bin/activate
pip install -r requirements.txt
```

In order to initialize a database configure the `.flaskenv` file to set your database location like so: 
DATABASE_URL=mysql://username:password@server/db
Then run: 

```
flask db init
flask db migrate -m "modify"
flask db upgrade
```
