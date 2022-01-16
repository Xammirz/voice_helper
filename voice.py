import re
from gtts import gTTS
import os
import speech_recognition as sr
import time
import random
import playsound
import webbrowser
import subprocess
import getpass
USER_NAME = getpass.getuser()


def command_listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        our_speech = r.recognize_google(audio, language='ru')
        print(f"Вы сказали: {our_speech}")
        return our_speech
    except sr.UnknownValueError:
        return 'Ошибка'
    except sr.RequestError as e:
        return 'ощибкаа 1'

def do_this_command(message):
    message = message.lower()
    
    if "открой telegram" in message:
        say_message('Выполняю, султан!')
        filename = 'Telegram.exe'
        for root, dirnames, filenames in os.walk('C:/Users/'):
            for file in filenames:
                if file == filename:
                    path = os.path.join(root, file)
        subprocess.call(f'{path}')
        say_message('что нибудь еще?')
    elif 'привет' in message:
        say_message('Приветствую ! Малика')
    elif 'не хочу говорить' in message:
        say_message('Как прикажете')
        exit()
    elif 'выключи компьютер' in message:
        say_message('Вы точно хотите выключить компьютер?')
    elif 'нет не выключай' in message:
        say_message('так точно')
    elif 'да выключай' in message:
        say_message('как прикажете!')
        os.system("shutdown /s /t 1")
    elif 'можешь идти' in message:
        say_message('как прикажете!')
        exit()
    elif 'спасибо' in message:
        say_message('что то еще пожелаете?')
    elif 'открой youtube' in message:
        say_message('как прикажете')
        webbrowser.open('https://www.youtube.com/', new=0, autoraise=True)
        say_message('что нибудь еще?')
    elif 'закрой яндекс' in message:
        say_message('Как прикажете')
        os.system("taskkill /im browser.exe /f")
    elif 'закрой telegram' in message:
        say_message('Как прикажете')
        os.system("taskkill /im Telegram.exe /f")
    elif 'поиск' in message:
        message = message[6:]
        user_query = f'{message}'         #имеется запрос
        blok_list = user_query.split()                        #разбиваем слова по пробелам
        url_query = '%20'.join(blok_list)                     #разделяем их через %20
        url = 'https://yandex.ru/search/?text=' + url_query + '&lr=213'   #подставляем
        webbrowser.open(f'{url}', new=0, autoraise=True)
    elif 'открой яндекс' in message:
        subprocess.call('C:/Users/ramza/AppData/Local/Yandex/YandexBrowser/Application/browser.exe')
        say_message('выполняю')
    else:
        say_message('Я тебя не понимаю')
def say_message(message):
    voice = gTTS(message, lang='ru')
    file_voice_name = '_auidio_'+str(time.time())+'_'+str(random.randint(0,1000))+'.mp3'
    voice.save(file_voice_name)
    playsound.playsound(file_voice_name)
    os.system(f'del {file_voice_name}')
    print('Ассистент: '+message)

if __name__ == '__main__':
    while True:
        command = command_listen()
        do_this_command(command)