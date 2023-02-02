import requests
import json
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

updater = Updater(token='5913636955:AAEchD7S4YWwFM0Q9QF7Mb2LxHn3qw56CH4', use_context=True)

dispatcher = updater.dispatcher

''' def hello(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = " Hello, World! ")

hello_handler = CommandHandler('hello', hello)
dispatcher.add_handler(hello_handler) '''

updater.start_polling()

def summary(update, context):
    response = requests.get('https://api.covid19api.com/summary')
    if(response.status_code == 200): # everything went fine, we have gotten the data
        data = response.json() # storing the json data in a variable
        date = data['Date'][:10]  # extracting date from JSON data
        ans = f"Covid 19 Summary (as of {date}): \n";

        for attribute, value in data['Global'].items():
            # we ignore the new confirmed, new deaths and new recovered data from the JSON
            if attribute not in['NewConfirmed', 'NewDeaths', 'NewRecovered']:
                # in the ans variable, adding total + attribute name(in lowercase) + value of  that attribute
                    ans += ' Total ' + attribute[5::].lower() + " : " + str(value) + "\n"
    
        print(ans)
         # sending ans through the bot 
        context.bot.send_message(chat_id = update.effective_chat.id, text = ans)

    else:
        # if we dont recieve the data or something goes wrong
        context.bot.send_message(chat_id = update.effective_chat.id, text = " Error, something went wrong. ")

summary_handler = CommandHandler('summary', summary)
dispatcher.add_handler(summary_handler)

