import sqlite3
import json

def criar_tabela():
    con = sqlite3.connect('cadastros.db')
    c = con.cursor()
    info = "CREATE TABLE dates(data TEXT, descricao TEXT, chat INT);"
    c.execute(info)
    con.commit()
    con.close()

def buscar_data(date):
    con = sqlite3.connect('cadastros.db')
    c = con.cursor()
    info = f"SELECT * FROM dates WHERE data = {date};"
    retorno = c.execute(info).fetchall()
    if retorno == []:
        return "{'erro':'404'}"
    else:
        lista_data = []
        for i in retorno:
            dicionario = {}
            dicionario['chat'] = i[0]
            dicionario['descricao'] = i[1]
            dicionario['chat'] = i[2]
            lista_data.append(dicionario)
            js = json.dumps(lista_data)
        return js

def buscar_data_id(chat):
    con = sqlite3.connect('cadastros.db')
    c = con.cursor()
    info = f"SELECT * FROM dates WHERE chat = {chat};"
    retorno = c.execute(info).fetchall()
    if retorno == []:
        return "{'erro':'404'}"
    else:
        lista_data = []
        for descricoes in retorno:
            dicionario = {}
            dicionario['data'] = descricoes[0]
            dicionario['descricao'] = descricoes[1]
            dicionario['chat'] = descricoes[2]
            lista_data.append(dicionario)
            js = json.dumps(lista_data)
        return js