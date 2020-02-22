def data_input(date, trackid, playcnt, total_plays, followers, name, albumname, artistname, artistpfp, duration, rating, artisturl):
    import sqlite3
    conn = sqlite3.connect('requests.db')
    c = conn.cursor()
    c.execute('''INSERT INTO requests VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?)''',(date, trackid, playcnt, total_plays, followers, name, albumname, artistname, artistpfp, duration,rating,artisturl))
    conn.commit()
    conn.close()

