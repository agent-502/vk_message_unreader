import vk_api
import random

logo = ('''

█████████████████████████████████████▀████████████████████████████████████████████████████████████
█▄─▀█▀─▄█▄─▄▄─█─▄▄▄▄█─▄▄▄▄██▀▄─██─▄▄▄▄█▄─▄▄─███▄─██─▄█▄─▀█▄─▄█▄─▄▄▀█▄─▄▄─██▀▄─██▄─▄▄▀█▄─▄▄─█▄─▄▄▀█
██─█▄█─███─▄█▀█▄▄▄▄─█▄▄▄▄─██─▀─██─██▄─██─▄█▀████─██─███─█▄▀─███─▄─▄██─▄█▀██─▀─███─██─██─▄█▀██─▄─▄█
█▄▄▄█▄▄▄█▄▄▄▄▄█▄▄▄▄▄█▄▄▄▄▄█▄▄█▄▄█▄▄▄▄▄█▄▄▄▄▄████▄▄▄▄██▄▄▄██▄▄█▄▄█▄▄█▄▄▄▄▄█▄▄█▄▄█▄▄▄▄██▄▄▄▄▄█▄▄█▄▄█ by- Agent502 \n''')

logo2 = ('''

                                                                                 .-.           
                                                                                 : :           
,-.,-.,-. .--.  .--.  .--.  .--.   .--.  .--.   .-..-.,-.,-..--.  .--.  .--.   .-' : .--. .--. 
: ,. ,. :' '_.'`._-.'`._-.'' .; ; ' .; :' '_.'  : :; :: ,. :: ..'' '_.'' .; ; ' .; :' '_.': ..'
:_;:_;:_;`.__.'`.__.'`.__.'`.__,_;`._. ;`.__.'  `.__.':_;:_;:_;  `.__.'`.__,_;`.__.'`.__.':_;  
                                   .-. :                                                       
                                   `._.'                                                       by- Agent502 \n''')

logo3 = ('''
┊┊╭╮╭╮┊┊┊┊┊┊┊┊
┊┊┊┃┃┃┃┊┊┊┊┊┊┊
┊┊┊┃┃┃┃┊┊┊╭━━━
┊┊╭┛┗┛┗╮┊╭╯Message
┊┊┃┈▆┈▆┃┊┃unreader! by- Agent502
┊┊┃┈┈▅┈┃┊╰┳━━━
┊┊┃┈╰┻╯┃━━╯┊┊┊ \n''')

logo4 = ('''

• ▌ ▄ ·. ▄▄▄ ..▄▄ · .▄▄ ·  ▄▄▄·  ▄▄ • ▄▄▄ .    ▄• ▄▌ ▐ ▄ ▄▄▄  ▄▄▄ . ▄▄▄· ·▄▄▄▄  ▄▄▄ .▄▄▄  
·██ ▐███▪▀▄.▀·▐█ ▀. ▐█ ▀. ▐█ ▀█ ▐█ ▀ ▪▀▄.▀·    █▪██▌•█▌▐█▀▄ █·▀▄.▀·▐█ ▀█ ██▪ ██ ▀▄.▀·▀▄ █·
▐█ ▌▐▌▐█·▐▀▀▪▄▄▀▀▀█▄▄▀▀▀█▄▄█▀▀█ ▄█ ▀█▄▐▀▀▪▄    █▌▐█▌▐█▐▐▌▐▀▀▄ ▐▀▀▪▄▄█▀▀█ ▐█· ▐█▌▐▀▀▪▄▐▀▀▄ 
██ ██▌▐█▌▐█▄▄▌▐█▄▪▐█▐█▄▪▐█▐█ ▪▐▌▐█▄▪▐█▐█▄▄▌    ▐█▄█▌██▐█▌▐█•█▌▐█▄▄▌▐█ ▪▐▌██. ██ ▐█▄▄▌▐█•█▌
▀▀  █▪▀▀▀ ▀▀▀  ▀▀▀▀  ▀▀▀▀  ▀  ▀ ·▀▀▀▀  ▀▀▀      ▀▀▀ ▀▀ █▪.▀  ▀ ▀▀▀  ▀  ▀ ▀▀▀▀▀•  ▀▀▀ .▀  ▀ by- Agent502 \n''')

logo5 = ('''

                                                                           _           
 _ __ ___   ___  ___ ___  __ _  __ _  ___   _   _ _ __  _ __ ___  __ _  __| | ___ _ __ 
| '_ ` _ \ / _ \/ __/ __|/ _` |/ _` |/ _ \ | | | | '_ \| '__/ _ \/ _` |/ _` |/ _ \ '__|
| | | | | |  __/\__ \__ \ (_| | (_| |  __/ | |_| | | | | | |  __/ (_| | (_| |  __/ |   
|_| |_| |_|\___||___/___/\__,_|\__, |\___|  \__,_|_| |_|_|  \___|\__,_|\__,_|\___|_|   
                               |___/                                                   by- Agent502 \n''')

banner = random.choice([logo2, logo, logo3, logo4, logo5])
print(banner)

TOKEN = input('ваш токен: ')

vk_session = vk_api.VkApi(token=TOKEN)
vk = vk_session.get_api()

index = 0

print("\nЗапуск процесса накрутки...")
print("Обработка сообщений...\n")

while True:
    try:
        for msg in range(10):
            msgs = vk.execute(code='var offset =' + f'{index}' + ',chats=API.messages.getConversations({count:200,offset:offset}).items,i=0;while(i<chats.length){if(!chats[i].conversation.is_marked_unread){API.messages.markAsUnreadConversation({peer_id:chats[i].conversation.peer.id});}i=i+1;}return 1;')
        index += 100
        print(f'{index} сообщений обработано')
    except Exception as e:
        print(repr(e))