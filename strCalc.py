from fuzzywuzzy import fuzz

def cmdRec(string):
    nums = []
    recCom = {'cmd' : '', 'percent' : 0}
    s = list(string.split())
    string = ''

    for i in range(len(s)):
        a = s[i]
        if a.isdigit():
            nums.append(float(s[i]))
        else:
            string += str(a)
    for i in coms:
        for c,v in coms.items():
            for i in v:
                var = fuzz.ratio(string, i)
                if var > recCom['percent']:
                    recCom['cmd'] = c
                    recCom['percent'] = var
    if recCom['percent'] < 0:
        recCom['cmd'] = 'unknown'
    return calc(recCom['cmd'],nums)

def calc(cmd, nums):
    ans = 0
    if cmd == 'plus':
        ans = nums[0] + nums[1]
    elif cmd == 'minus':
        ans = nums[0] - nums[1]
    elif cmd == 'multi':
        ans = nums[0] * nums[1]
    elif cmd == 'devide':
        if nums[1] == 0:
            return 'Увы, но делить на ноль нельзя'
        ans = nums[0] / nums[1]
    elif cmd == 'sqr':
        ans = nums[0] ** 2
    elif cmd == '3sqr':
        ans = nums[0] ** 3
    elif cmd == 'sqrt':
        ans = nums[0] ** 0.5
    elif cmd == 'step':
        ans = nums[0] ** nums[1]

    ans = round(ans,3)
    if ans == 300:
        return 'Знаю я ваши шутки... 3 сотни получается'

    if ans % 1 == 0:
        ans = int(ans)
    return ans

coms = {
    'plus' : ('прибавь', 'плюс', 'сложить', '+'),
    'minus' : ('вычти', 'вычесть', 'минус', '-'),
    'multi' : ('умножь', 'умножить', 'произведение', 'x'),
    'devide' : ('раздели', 'разделить', 'делить', 'подели', '/'),
    'sqr' : ('в квадрате',  'квадрат'),
    '3sqr' : ('в кубе',  'куб'),
    'sqrt' : ('корень','вычти корень из', 'корень из'),
    'step' : ('возведи в степень', 'в степени')
    }
