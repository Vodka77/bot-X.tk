import telebot
from telebot import types
import requests
bot=telebot.TeleBot(input('Enter Token :'))
@bot.message_handler(commands=['start'])
def Start(message):
    if message.chat.type == 'private':
        maac = types.InlineKeyboardMarkup()
        addg = types.InlineKeyboardButton(text='Add To Group',url='https://telegram.me/TUV_7Bot?startgroup=start')
        about = types.InlineKeyboardButton(text='About',callback_data='about')
        commands = types.InlineKeyboardButton(text='Bot Commands',callback_data='comm')
        maac.row_width = 2
        maac.add(commands,about)
        maac.add(addg)
        bot.send_photo(message.chat.id,'https://www.google.com/imgres?imgurl=https%3A%2F%2Fthumbs.dreamstime.com%2Fb%2Frobot-logo-chatbot-bot-symbol-robot-logo-chatbot-bot-symbol-white-background-cute-robot-icon-support-service-bot-134937332.jpg&imgrefurl=https%3A%2F%2Fwww.dreamstime.com%2Frobot-logo-chatbot-bot-symbol-robot-logo-chatbot-bot-symbol-white-background-cute-robot-icon-support-service-bot-image134937332&tbnid=3ilIDfiRBtVpYM&vet=12ahUKEwiK8deGt4z2AhXt7rsIHZpZDpUQMygGegUIARDrAQ..i&docid=3toAaU3keYHr1M&w=800&h=554&q=Bot%20logo&hl=en-GB&ved=2ahUKEwiK8deGt4z2AhXt7rsIHZpZDpUQMygGegUIARDrAQ',caption=f'<b>Hi {message.from_user.first_name}\n- - - - - - - -\nWelcome To Telegram User Checker\nEnjoy From The Buttoms Here\n- - - - - - - -\nBY : @Vodka_Tools</b>',parse_mode='html',reply_to_message_id=message.message_id,reply_markup=maac)
        @bot.callback_query_handler(func=lambda call:True)   
        def xcall(call):
            if call.data=='about':
                back = types.InlineKeyboardMarkup()
                bac = types.InlineKeyboardButton(text='Back Home Page',callback_data='bac')
                back.row_width = 2
                back.add(bac)
                bot.edit_message_caption(chat_id=call.message.chat.id,caption='*This Bot Code By : @a_paa\nCoder Channel : @Vodka_Tools\nThis Bot Check Telegram\nIf The User Is Valid Or Not\n- - - - - - - -\nBY : @Vodka_Tools*',parse_mode='markdown',message_id=call.message.message_id,reply_markup=back)
            if call.data=='bac':
                maac = types.InlineKeyboardMarkup()
                addg = types.InlineKeyboardButton(text='Add To Group',url='https://telegram.me/TUV_7Bot?startgroup=start')
                about = types.InlineKeyboardButton(text='About',callback_data='about')
                commands = types.InlineKeyboardButton(text='Bot Commands',callback_data='comm')
                maac.row_width = 2
                maac.add(commands,about)
                maac.add(addg) 
                bot.edit_message_caption(chat_id=call.message.chat.id,caption=f'<b>Hi {message.from_user.first_name}\n- - - - - - - -\nWelcome To Telegram User Checker\nEnjoy From The Buttoms Here\n- - - - - - - -\nBY : @Vodka_Tools</b>',parse_mode='html',message_id=call.message.message_id,reply_markup=maac)
            if call.data == 'comm':
                back = types.InlineKeyboardMarkup()
                bac = types.InlineKeyboardButton(text='Back Home Page',callback_data='bac')
                back.row_width = 2
                back.add(bac)
                bot.edit_message_caption(chat_id=call.message.chat.id,caption='*Send Your Username To Check The User\n- - - - - - - -\nBY : @Vodka_Tools*',parse_mode='markdown',message_id=call.message.message_id,reply_markup=back)
    if message.chat.type == "group" or message.chat.type == "supergroup":
        bot.send_photo(message.chat.id,'https://www.google.com/imgres?imgurl=https%3A%2F%2Fthumbs.dreamstime.com%2Fb%2Frobot-logo-chatbot-bot-symbol-robot-logo-chatbot-bot-symbol-white-background-cute-robot-icon-support-service-bot-134937332.jpg&imgrefurl=https%3A%2F%2Fwww.dreamstime.com%2Frobot-logo-chatbot-bot-symbol-robot-logo-chatbot-bot-symbol-white-background-cute-robot-icon-support-service-bot-image134937332&tbnid=3ilIDfiRBtVpYM&vet=12ahUKEwiK8deGt4z2AhXt7rsIHZpZDpUQMygGegUIARDrAQ..i&docid=3toAaU3keYHr1M&w=800&h=554&q=Bot%20logo&hl=en-GB&ved=2ahUKEwiK8deGt4z2AhXt7rsIHZpZDpUQMygGegUIARDrAQ',caption=f'<b>Welcome To Telegram User Check\n- - - - - - - -\nSend Your Telegram User To Check\nEnjoy Our Bot\n- - - - - - - -\nBY : @Vodka_Tools</b>',parse_mode='html')
        @bot.message_handler(func=lambda m:True)
        def userX(message):
            msg = message.text
            url = requests.get(f'https://vodka-apis.herokuapp.com/Telegram/Check/?user={msg}').json()['data']
            if url == 'Taken User':
                bot.reply_to(message,f'<b>Taken User : @{msg}\n- - - - - - - -\nBy : @Vodka_Tools</b>',parse_mode='html')
            elif url == 'Valid User':
                bot.reply_to(message,f'<b>Valid User : @{msg}\n- - - - - - - -\nBy : @Vodka_Tools</b>',parse_mode='html')                                
bot.polling(True)  

