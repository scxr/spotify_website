import sqlite3
conn = sqlite3.connect('requests.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS requests (id integer PRIMARY KEY,date string, trackid string, playcnt integer, total_plays integer, followers integer, songname string, album_name string, artistname string, artistpfp string, duration string, rating integer, artisturl string)''')
conn.commit()
conn.close()