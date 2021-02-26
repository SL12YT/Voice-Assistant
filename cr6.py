#version 1.5.0a

from time import sleep
try:
    import speech_recognition as sr
except:
    print('#Ошибка 1 - Не удалось импортировать библиотеку "Speech Recognition"...\n\
           Проверьте корректность установки данной библиотеки...\n\
           Для завершения нажмите Enter')
    input()
    exit()
try:
    from fuzzywuzzy import fuzz
except:
    print('#Ошибка 2 - Не удалось импортировать библиотеку "FuzzyWuzzy"...\n\
           Проверьте корректность установки данной библиотеки...\n\
           Для завершения нажмите Enter')
    input()
    exit()
try:        
    import pyttsx3 as pt
except:
    print('#Ошибка 3 - Не удалось импортировать библиотеку "Pyttsx3"...\n\
           Проверьте корректность установки данной библиотеки...\n\
           Для завершения нажмите Enter')
    input()
    exit()
try:
    import coms as cm
except:
    print('#Ошибка 4 - Не удалось обнаружить файл "coms.py" в корневой папке программы... \n\
           Проверьте наличие данного файла в корневой папке, если его там не окажетс - переустановите программу...\n\
           Для завершения нажмите Enter')
    input()
    exit()

try:
    import strCalc as calc
except:
    print('#Ошибка 5 - Не удалось обнаружить файл "strCalc.py" в корневой папке программы... \n\
           Проверьте наличие данного файла в корневой папке, если его там не окажетс - переустановите программу...\n\
           Для завершения нажмите Enter')
    input()
    exit()
try:
    import weather as w
except:
    print('#Ошибка 6 - Не удалось обнаружить файл "weather.py" в корневой папке программы... \n\
           Проверьте наличие данного файла в корневой папке, если его там не окажетс - переустановите программу...\n\
           Для завершения нажмите Enter')
def spRecogn():
    with m as source:
        try:
            print('Я вас слушаю...')
            audio = r.listen(source)
            said = r.recognize_google(audio, language = "ru-RU")
            said = said.lower()
            print('Вы сказали: ' + said)
            
            cmdExecute(cmdRecogn(said), said)
        
        except sr.UnknownValueError:
            print('Не удалось распознать речь...')
        except sr.RequestError:
            print('Нет подключения к Интернету...')

def cmdRecogn(said):

    for i in options['remove']:
        said = said.replace(i,'').strip()

    recCom = {'cmd' : '', 'percent' : 0}
    for c,v in options['cmds'].items():
        for i in v:
            variety = fuzz.ratio(said, i)
            if variety > recCom['percent']:
                recCom['cmd'] = c
                recCom['percent'] = variety
                
    if recCom['percent'] < 33:
        recCom['cmd'] = 'unknown'

    return recCom['cmd']

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()
    engine.stop()
 
def cmdExecute(cmd, said):
    timer = 30
    
    if cmd == 'hello':
        speak(cm.hello())
    elif cmd == 'goodbye':
        speak(cm.goodBye())
    elif cmd == 'time':
        speak(cm.curTime())
    elif cmd == 'date':
        speak(cm.curDate())
    elif cmd == 'browStart':
        cm.browStart()
    elif cmd == 'cDeskFold':
        for i in options['cdfRem']:
            said = said.replace(i, '').strip()
        cm.cDeskFold(said)
    elif cmd == 'joke':
        speak(cm.joke())
    elif cmd == 'phil':
        speak(cm.philosophy())
    elif cmd == 'iSmart':
        speak(cm.iAmSmart())
    elif cmd == 'uSmart':
        speak(cm.usIsSmart())
    elif cmd == 'iStupid':
        speak(cm.iAmStupid())
    elif cmd == 'uStupid':
        speak(cm.usIsStupid())
    elif cmd == 'howAreU':
        speak(cm.howAreYou())
    elif cmd == 'calc':
        for i in options['calRem']:
            said = said.replace(i,'').strip()
        speak(calc.cmdRec(said))
    elif cmd == 'iGood':
        speak(cm.iAmGood())
    elif cmd == 'weather':
        for i in options['cmds']['weather']:
            said = said.replace(i, '').strip()
        print(said)
        speak(w.caser(said))
    elif cmd == 'shutdown':
        for i in list(map(str, said.split())):
            if i.isdigit():
                timer = int(i)
        for i in list(map(str, said.split())):
            if i == 'минут' or i == 'минуту' or i == 'минуты':
                timer *= 60
            elif i == 'час' or i == 'часов' or i == 'часа':
                timer *= 3600
        cm.shutdwn(timer)
    elif cmd == 'reboot':
        for i in list(map(str, said.split())):
            if i.isdigit():
                timer = int(i)
        for i in list(map(str, said.split())):
            if i == 'минут' or i == 'минуту' or i == 'минуты':
                timer *= 60
            elif i == 'час' or i == 'часов' or i == 'часа':
                timer *= 3600
        cm.rebt(timer)
    elif cmd == 'shutCanc':
        speak(cm.shutCanc())
    elif cmd == 'close':
        speak(cm.goodBye())
        exit(0)
    else:
        print('Я не поняла команду')
        
options = {
    "remove" : ("скажи", "покажи", "напомни", "укажи", "ты", "можешь", "ли","подскажи",
                "сказать", "показать", "напомнить", "указать","подсказать", "расскажи"),
    "calRem" : ("сколько будет", "посчитай", "вычисли", "расчитай"),
    "cdfRem" : ('создай папку на рабочем столе', 'папку на рабочем столе', 'с названием',
                'создай', 'создать', 'папку', 'папка', 'на' 'рабочем столе', 'рабочий стол',
                'с именем','назови её', 'и назови', 'назвать её', 'назвать','и '),
    "cmds" : {
        'hello' : ("привет", "добрый день", "здравствуй", "здравствуйте"),
        'goodbye' : ("пока", "прощай", "до завтра", "бывай"),
        'time' : ("какое сейчас время", "который час", "текущее время", "время"),
        'date' : ("какое сегодня число", "текущая дата", "какой сегодня день"),
        'joke' : ("расмеши меня", "пошути", "умеешь шутить", "хочу шутку","анекдот", "прикол"),
        'phil' : ("каков смысл жизни", "цитату", "мудрость", "мудрая"),
        'weather' : ('погода в', 'погода на', 'какая сейчас'),
        'shutdown' : ('выключи', 'выключи компьютер', 'выключи ноутбук', 'выключи через'),
        'reboot' : ('перезагрузи', 'перезагрузи компьютер', 'перезагрузи ноутбук', 'перезагрузи через'),
        'shutCanc' : ('отмени перезагрузку', 'отмени выключение', 'отмена'),
        'browStart' : ('браузер','открой браузер', 'запусти браузер'),
        'cDeskFold' : ('создай папку на рабочем столе', 'папку на рабочем столе'),
        'openProg' : ('открой', 'запусти', 'открыть', 'запустить'),
        'iSmart' : ("умная", "гений", "очень умная", "самая умная"),
        'uSmart' : ("я умён", "я умный", "я гений", "я очень умён", "я самый умный", "я очень умна",
                    "я очень умная", "я самая умная"),
        'iStupid' : ("тупая", "дура", "дурочка", "безмоглая"),
        'uStupid' : ("я тупой", "я туп", "я безмоглый", "я дегенерат", "меня назвали тупым",
                     "меня назвали безмозглым","я тупая", "я тупа", "я безмоглая", "меня назвали тупой"),
        'howAreU' : ("как у тебя дела", "как себя чувстуешь", "надеюсь у тебя все хорошо"),
        'iGood' : ('молодец', 'спасибо', 'благодарю', 'молодчина'),
        'calc' : ("посчитай", "сколько будет", "вычисли",'прибавь', 'плюс', 'сложить', 'вычти', 'вычесть',
                  'минус', 'умножь', 'умножить', 'произведение', 'раздели', 'разделить', 'делить', 'подели',
                  'в квадрате', 'квадрат', 'в кубе', 'куб', 'корень','вычти корень из', 'корень из', 'возведи в степень', 'в степени', '+', '-'),
        'close' : ("закрыть", "закройся", "умри")
            }
}
 
try:
    m = sr.Microphone(device_index = 2)
    r = sr.Recognizer()
except:
    print('#Ошибка 7 - Не удалось подключить микрофон. Возможно доступ к нему запрещён. \n\
           Включите доступ к микрофону и перезапустите программу. \n\
           Для завершения нажмите Enter')
    input()
    exit()
try:
    engine = pt.init()
except:
    print('#Ошибка 8 - Не удалось запустить движок для голосовых ответов... \n\
           Проверьте корректность установки библиотеки "pyttsx3",\n\
           Если библиотека установлена корректно, а ошибка присутствует - запустите программу без\n\
           голосовых ответов : cr6s.py или cr62s.py\n\
           Для завершения нажмите Enter')

while True:
    spRecogn()
    sleep(0.15)	

input()

