import telebot
import os
from threading import Thread
import sys
import json
sys.path.insert(1, './commands')
import buscar_data, criar_data, deletar_data, verificar_data
from criar_data import criarData
from buscar_data import buscar_data
from verificar_data import verificar
from dotenv import load_dotenv
load_dotenv()

t = Thread(target=verificar, args=()).start()

admin = os.getenv("ADMIN_ID")

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"), parse_mode='markdown')

@bot.message_handler(commands=['start'])
def start(message):
	bot.reply_to(message, "Bem-vindo ao reminder bot. Aqui você pode definir lembretes e de acordo com a data irei enviar-lhe o mesmo.")

@bot.message_handler(commands=['help'])
def help(message):
	h = '''
/remind -> Define um lembrete. (/remind <MesDia> <DescricaoLembrete>)
/search -> Filtra lembretes de acordo com a data (/search <MesDia>)
/help -> Mostra essa mensagem :)
	'''
	bot.reply_to(message, h)

@bot.message_handler(commands=['search'])
def search(message):
	date = message.text.split()[1]
	result = buscar_data(date)
	if result == "{'erro':'404'}":
		bot.reply_to(message, "*Não há lembretes para esse dia*")
	else:
		result = json.loads(result)
		sendms = ""
		for itens in result:
			desc = itens['descricao']
			sendms += str(desc) + '\n'
		bot.reply_to(message, f'LEMBRETES ENCONTRADOS:\n\n*{sendms}*')

@bot.message_handler(commands=['remind'])
def main(message):
	try:
		cmd = message.text.split()
		data = cmd[1]
		desc = " ".join(cmd[2:])
		print(data, desc)
		print(message.chat.id)
		cad_test = criarData.criar_data(data, desc, message.chat.id)
		bot.reply_to(message, "✅ Lembrete definido com sucesso.")
	except:
		bot.reply_to(message, 'Ocorreu um erro.')

bot.infinity_polling()