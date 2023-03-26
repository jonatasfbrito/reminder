import sqlite3
import time
import datetime
import os
import sys
sys.path.append('../commands/')
from buscar_data import buscar_data, buscar_data_id
import deletar_data
import json
from deletar_data import delete_data
import telebot
from dotenv import load_dotenv
load_dotenv()

adm = os.getenv("ADMIN_ID")
bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))

data_atual = datetime.datetime.now()
data_formatada = data_atual.strftime('%d/%m')

def verificar():
    while True:
        time.sleep(5)
        array = buscar_data(data_formatada)
        if array == "{'erro':'404'}":
            print('[Nenhuma da enviada.]')
        else:
            js = json.loads(array)
            sendms = ""
            for itens in js:
                desc = itens['descricao']
                chat = itens['chat']
                sendms += str(desc) + '\n'
            bot.send_message(chat, sendms)
            delete_data(data_formatada)
            print("Deleted Data - [OK]")