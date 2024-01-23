import logging


logging.basicConfig(filename='test_1.log', filemode='w', encoding='utf-8',\
                    level=logging.INFO) 
logger = logging.getLogger(__name__)

"""Функция запрашивает число от пользователя до тех пор, 
пока не будет введено целое или вещественное число."""


logger.info('Функция запрашивает число от пользователя до тех пор, пока не будет введено целое или вещественное число.')

def check(text: str) -> int | float:
    while True:
        data = input(text)
        try:
            num = int(data) if data.isdigit() else float(data)
        except ValueError as e:
            logger.error(f'"Ошибка!" - {e}, ваш ввод {data} = {type(data)}')
            logger.critical(f'"Код работать не будет, ошибка!" - {e}, ваш ввод {data} = {type(data)}')
        else:
            return num


if __name__ == '__main__':
    number = check('Введите число: ')
    logger.info(number)
    


"""Семинар 1. Домашняя задача 1. Сравнение сторон треугольника"""

a = 4
b = 4
c = 25
if a + b >= c and b + c >= a and c + a >= b:
    logger.info('Треугольник существует')
    if a == b == c:
        logger.info('Треугольник равносторонний')
    elif a == c or a == b or c == b:
        logger.info('Треугольник равнобедренный')
    elif a != b != c:
        logger.info('Треугольник разносторонний')
else:
    logger.warning('Треугольник не существует!!')
    

 
"""Список вещей для похода.
logger.error('Превышено максимальное значение') - вызывается в случае, если вес вещей (items) 
превысил максимальное значение веса (max_weight) рюкзака. 
Предположим, что нам необходимо упаковать все вещи из items в backpack (вес в граммах)."""

items = {
    "ключи": 30,
    "кошелек": 50,
    "телефон": 140,
    "зажигалка": 100
}
max_weight = 280

backpack = {}

for item, weight in items.items():
    if weight <= max_weight:
        backpack[item] = weight
        max_weight -= weight
    elif weight > max_weight:
        logger.error('Превышено максимальное значение')
        
logger.info(backpack)



"""Преобразование ключей и значений словаря
функция key_params, принимает на вход только ключевые параметры и возвращающую словарь, 
где ключ - значение переданного аргумента, а значение - имя аргумента.
Если ключ не хешируем, используем его строковое представление."""

def key_params(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if value is None:
            result[value] = key
        elif isinstance(value, (int, str, float, bool, tuple)):
            try: 
                result[value] = key
            except:
                logger.error('Недопустимый тип данных для ключа')
                logger.critical('Недопустимый тип данных для ключа')
        else:
            result[str(value)] = key
    return result
               
logger.info(key_params(a=1, b='hello', c=[1, 2, 3], d={}))