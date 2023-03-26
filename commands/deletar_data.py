import sqlite3

def delete_data(data):
    con = sqlite3.connect('cadastros.db')
    c = con.cursor()
    exe = c.execute(f"DELETE FROM dates WHERE data = {data};")
    con.commit()
    con.close();
