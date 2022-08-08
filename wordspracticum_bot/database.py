import sqlite3
from sqlite3 import Cursor
from typing import Callable
import random



def db_decorator(func: Callable) -> Callable:
    """
    Декоратор - Производит подключение к БД.
    :param func: Callablе
    :return: Callable
    """
    def wrapped_func(*args, **kwargs):
        try:
            connection = sqlite3.connect('../wordspracticum/db.sqlite3')
            connection.isolation_level = None
            cursor = connection.cursor()
            result = func(*args, **kwargs, cursor=cursor)
            return result
        except TypeError as ex:
            print(ex, 'Ошибка БД')
        except Exception as ex:
            print(ex, 'Ошибка БД')
        finally:
            connection.close()
    return wrapped_func


# @db_decorator
# def select_all(param, cursor: Cursor):
#     cursor.execute("SELECT * FROM words WHERE category = ?", (param,))
#     result = cursor.fetchall()
#     return result


@db_decorator
def select_easy_level(level: str, cursor: Cursor):
    cursor.execute("SELECT * FROM words WHERE category = ?", (level, ))
    all_words = cursor.fetchall()
    return all_words


@db_decorator
def random_words(level: str, cursor: Cursor):
    cursor.execute("SELECT * FROM words WHERE category = ?", (level, ))
    all_words = cursor.fetchall()
    result = []
    data = {}
    for word in all_words:
        data[word[1]] = word[2]
        result.append(data)
    return result


@db_decorator
def translates_rnd_word(level: str, cursor: Cursor):
    cursor.execute("SELECT translate FROM words WHERE category = ?", (level, ))
    all_translates = cursor.fetchall()
    random.shuffle(all_translates)
    return all_translates[0]


@db_decorator
def all_translates_and_words(level: str, cursor: Cursor):
    cursor.execute("SELECT name FROM words WHERE category = ?", (level, ))
    words = cursor.fetchall()
    cursor.execute("SELECT translate FROM words WHERE category = ?", (level, ))
    translates = cursor.fetchall()
    data = zip(words, translates)
    return dict(data)

