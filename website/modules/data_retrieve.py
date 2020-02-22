import sqlite3

def data_retrieve(inp):
    conn = sqlite3.connect('requests.db')
    c = conn.cursor()
    c.execute('''SELECT playcnt, total_plays, followers, songname, album_name, artistname, artistpfp, duration, rating, artisturl FROM requests WHERE songname=?''',(inp,))
    resp = c.fetchall()
    conn.commit()
    conn.close()
    return resp

