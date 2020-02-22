import sqlite3, math
from collections import defaultdict
def date_retrieve(inp):
    conn = sqlite3.connect('requests.db')
    c = conn.cursor()
    c.execute('''SELECT date,playcnt,followers FROM requests WHERE songname = ?''',(inp,))
    resp = c.fetchall()
    conn.commit()
    conn.close()
    d = defaultdict(list)
    dates = []
    for i, x, y in resp:
        myitem = dict(date=i,playcnt=x,followers=y)
        dates.append(myitem)
    print(dates[2])
    return dates

