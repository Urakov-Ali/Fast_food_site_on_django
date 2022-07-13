import requests


def telegram_bot_send_message(bot_message):
	bot_token ='YOUR TOKEN HERE'
	bot_chatID ='BOT CHAT ID HERE'
	send_text ='https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode =Markdown&text=' + bot_message 
	response =requests.get(send_text)
	return response.json()
