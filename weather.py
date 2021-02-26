try:
    import pyowm as p
except:
    print('#Ошибка 10 - Не удалось импортировать библиотеку "PyOWM"...\n\
           Проверьте корректность установки данной библиотеки...\n\
           Для завершения нажмите Enter')
    input()
    exit()
from random import randint as r

owm = p.OWM('aa574ac656f61b899f22317b7b105331') #API ключ

def weth(city):
    obs = owm.weather_at_place(city)
    w = obs.get_weather()

    temp = w.get_temperature('celsius')
    clouds = w.get_clouds()
    wind = w.get_wind()
    rain = w.get_status()
    if rain == 'rain':
        rain = 'идёт дождь'    
    else:
        rain = ''
    temp = round(temp['temp'],0)
    if clouds < 10:
        clouds = 'Ясно'
    elif clouds < 20:
        clouds = 'Почти ясно'
    elif clouds < 30:
        clouds = 'Переменная облачность'
    else:
        clouds = 'Пасмурно'
    forecast = [temp, clouds, rain, wind['speed']]
    frc = stringer(forecast)
    return frc

def stringer(forecast):
    t = forecast[0] #Температура в градусах цельсия
    c = forecast[1].lower() #Облачность
    rin = forecast[2] #Дожди
    w = forecast[3] #Скорость ветра
    
    if t % 1 == 0:
        t = int(t)
    if w % 1 == 0:
        w = int(w)

    #Формирование текста прогноза
    st = str('На улице ' + str(t) + ' градуса, ') 

    if rin != '':
        rand = r(0,1)
        if rand == 0:
            rn = 'идёт дождь '
        elif rand == 1:
            rn = 'дождик '
    else:
        rn = ''
    
    frc = str(st + rn + c + ', ветер ' + str(w) + ' метра в секунду')
    return frc
    #Формирование текста прогноза
     
def caser(city):
    cs1 = cs2 = cs3 = cs4 = city.lower()
    city = city.lower()
    if city[-1:] == 'е':
        cs1 = city[:-1] + 'а'
        cs2 = city[:-1]
    elif city[-2:] == 'ом':
        cs3 = city[:-2] + 'ый'
    else:
        cs4 = city

    try:
        owm.weather_at_place(cs1)
        return weth(cs1)
    except:
        try:
            owm.weather_at_place(cs2)
            return weth(cs2)
        except:
            try:
                owm.weather_at_place(cs3)
                return weth(cs3)
            except:
                try:
                    owm.weather_at_place(cs4)
                    return weth(cs4)
                except:
                    return('Увы я не нашла такой город')
                