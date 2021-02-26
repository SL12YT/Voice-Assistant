#version 1.5.0a

from datetime import datetime as dt
from random import randint as r
from os import system as cmd
from pathlib import Path

def curTime():
    current = dt.now()
    hr = str(current.hour)
    mn = str(current.minute)
    
    fts = ('Сейчас ', 'На часах', 'Текущее время ', 'Часы подсказывают мне, что сейчас ')
    
    time = fts[r(0,3)] + hr + ':' + mn
    return time

def curDate():
    current = dt.now()
    day = current.day
    month = current.month
    if month == 1:
        month = ' января'
    elif month == 2:
        month = ' февраля'
    elif month == 3:
        month = ' марта'
    elif month == 4:
        month = ' апреля'
    elif month == 5:
        month = ' мая'
    elif month == 6:
        month = ' июня'
    elif month == 7:
        month = ' июля'
    elif month == 8:
        month = ' августа'
    elif month == 9:
        month = ' сентября'
    elif month == 10:
        month = ' октября'
    elif month == 11:
        month = ' ноября'
    else:
        month = ' декабря'
    
    fts = ('Сегодня ', 'Текущая дата ', 'Согласно моему календарю, сегодня ')
    
    date = fts[r(0,2)] + str(day) + month
    return date

def hello():
    hId = r(0,4)
    hellos = ('Привествую Вас!', 'Доброго времени суток!', 'Добрый день!','Рада Вас снова видеть!',
              'Приятно Вас снова видеть!')
    
    h = hellos[hId]
    return h

def goodBye():
    gbId = r(0,4)
    goodbyes = ('До свидания!', 'До скорой встречи!', 'Счастливого Вам дня!', 'Прощайте!',
                'Буду рада снова Вас видеть!')
                
    g = goodbyes[gbId]
    return g

def joke():
    jkId = r(0,4)
    jokes = ('Автор не научил меня шутить. Ха-ха... Обидно вообще-то', 'Шутить - это какой-то вид пытки?', 
             'Я так-то робот, у меня нет чувства юмора', 'Ну допустим, колобок повесился. Ха-ха-ха... очень смешно',
             'Уверена у Вас лучше получится пошутить')
             
    j = jokes[jkId]
    return j
    
def philosophy():
    pId = r(0,4)
    philosophys = ('Весь мир - театр : одни ломают комедию, другие все драматизируют', 'Цель определяет смысл жизни',
                  'Самое главное при совершении невозможного - знать с чего начать',
                  'Книги - ноты, беседы - пение',
                  'Болтливый человек - это распечатанное письмо, которое все могут прочесть')
                  
    p = philosophys[pId]
    return p
    
def iAmSmart():
    sId = r(0,4)
    smart = ('Ой, ну что Вы?', 'Будучи роботом, я обязано такой быть', 'Спасибо за комплимент',
             'Как неожиданно и приятно!', 'Умный не тот кто умный, а тот кто умный')

    s = smart[sId]
    return s

def usIsSmart():
    sId = r(0,4)
    smart = ('Кто бы сомневался', 'Да, но я умнее... хе-хе', 'Ну-ну...',
             'Я так и знала', 'А разве это всем известно?')
    
    s = smart[sId]
    return s

def iAmStupid():
    sId = r(0,4)
    stupid = ('С чего Вы взяли?', 'Ваша попытка меня обидеть не удалась', 
              'Робот не может быть тупым, тупым может быть только его создатель, но в моем случае автор - гений',
              'Кто обзывается, тот сам так называется', 'Кто бы говорил')
    
    s = stupid[sId]
    return s

def usIsStupid():
    sId = r(0,4)
    stupid = ('Кто Вам такое сказал?', 'Это не правда!', 'Только умный признает себя тупым',
              'Я этому не верю', 'Я уверена, что это не так!')
    
    s = stupid[sId]
    return s

def howAreYou():
    hId = r(0,4)
    how = ('Как всегда отлично!', 'Чувствую себя замечательно!', 'Я робот, для меня каждый день как предыдущий',
           'Я полна сил и энергии, хоть они мне и не нужны!', 'У меня всё просто отлично!')
    
    h = how[hId]
    return h

def iAmGood():
    gId = r(0,4)
    good = ('Спасибо!', 'Пусть я и робот, но мне это приятно', 'Рада стараться для вас',
            'Ой, ну что вы', 'Вы тоже молодец!')
    return good[gId]

prevShut = ''
def shutdwn(timer):
    command = 'shutdown -s -t ' + str(timer)
    cmd(command)
    prevShut = 's'
    
def rebt(timer):
    command = 'shutdown -r -t ' + str(timer)
    cmd(command)
    prevShut = 'r'
    
def shutCanc():
    command = 'shutdown -a'
    cmd(command)
    
    speechS = ('Выключение отменяю', 'Хорошо','Как скажете', 'Ладно, не буду вылкючать')
    speechR = ('Перезагрузку отменяю', 'Хорошо','Как скажете', 'Ладно, не буду перезагружать')
    
    rId = r(0, 3)
    
    if prevShut == 's':
        return speechS[rId]
    else:
        return speechR[rId]

def browStart():
    cmd('start http://')
    
def cDeskFold(fName):
    try:
        (Path.home() /"Desktop"/fName).mkdir(parents = True, exist_ok = True)
    except:
        print('#Ошибка 9 - Не удалось создать папку... Проверьте корректность названия папки.')    