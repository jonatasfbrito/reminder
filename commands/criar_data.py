import sqlite3

class criarData(object):

    def credenciais_ok(data):
        if isinstance(data, str) and len(str(data)) == 4:
            return True
        else:
            return False

    def criar_data(data, descricao = "Não informou.. Problema teu pra saber.", chat = 0):
        con = sqlite3.connect('cadastros.db')
        c = con.cursor()
        info = f"INSERT INTO dates VALUES({data},'{descricao}',{chat});"
        c.execute(info)
        con.commit()
        con.close();