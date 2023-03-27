
# Reminder Bot

Um bot simples para Telegram que envia lembretes de acordo com a data determinada.

# Comandos




| Comando            | Descrição                                                                |
| ----------------- | ------------------- |
| remind | Adiciona um lembrete com data específica |
| help | Mostra os comandos disponíveis |
| search | Busca lembretes de uma data específica |



## Rodando localmente

Clone o projeto:

```bash
  git clone https://github.com/jonatasfbrito/reminder
```

Entre no diretório do projeto:

```bash
  cd reminder
```

instale a seguinte depêndencia usando o pip:

```bash
  pip install telebot python-dotenv
```

Entre no arquivo .env e troque as informações necessárias:

```bash
  BOT_TOKEN=<seuToken>
  ADMIN_ID=<seuId>
```

Inicie o bot com o comando:
```bash
  python3 main.py
```

## Autor

- Se quiser contribuir, faça um commmit! <3
- [Jônatas](https://t.me/kotlinux)
