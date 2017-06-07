from Parser import *
import csv
import telebot
from telebot import types



#https://api.telegram.org/bot357504554:AAFI1yK_0n8ksIpUdhyTuSzMFzYdQ7GcnJc/sendmessage?chat_id=372195655&text=/start
TOKEN = '357504554:AAFI1yK_0n8ksIpUdhyTuSzMFzYdQ7GcnJc'
URL = 'https://api.telegram.org/bot' + TOKEN + '/'
bot = telebot.TeleBot(TOKEN)

global last_update_id
last_update_id = 0





def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()


def get_message():
    data = get_updates()
    last_object = data['result'][-1]
    current_update_id = last_object['update_id']
    global last_update_id
    if last_update_id != current_update_id:
        last_update_id = current_update_id

        chat_id = last_object['message']['chat']['id']
        message_text = last_object['message']['text']

        message = {'chat_id': chat_id,
                   'text': message_text}

        return message
    return None


def send_message(chat_id, text='Wait a second, please...'):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id,text)
    requests.get(url)


def main():
    while True:
        answer = get_message()
        if answer != None:
            chat_id = answer['chat_id']
            text = answer['text']

            FILENAME = "Films.csv"
            with open(FILENAME, "r", encoding='utf-8',newline="") as file:
                reader = csv.reader(file)
           
                for row in reader:
                    if text in row[0] :
                        send_message(chat_id, row[1])
                        break
                    else:
                        if text in row[2] :
                            send_message(chat_id, row[1])
                            break
                        else:
                            if text in row[3] :
                                send_message(chat_id, row[1])
                                break
                            else:
                                continue
        else:
            continue


# with open(FILENAME, "r", encoding='utf-8',newline="") as file:
         #   reader = csv.reader(file)
           # for line in reader:
            #    if text == '/film':
             #       send_message(chat_id,line[1])







@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(True,False)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Drama', 'Comedy','Action', 'Adventure', 'Fantasy',
                                                        'Romance', 'Family', 'Music', 'Thriller', 'Crime',
                                                        'Horror', 'Science']])
    bot.send_message(message.from_user.id, 'Which genre do you prefer?', reply_markup=keyboard)
bot.polling(none_stop=True)


if __name__ == '__main__':
    main()


















