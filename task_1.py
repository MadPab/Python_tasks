import datetime

name = input()


def hello_user_by_time():
    local_time = datetime.datetime.now().hour
    if 0 <= local_time < 5:
        print("Доброй ночи,", name)
    elif 5 <= local_time < 10:
        print("Доброе утро,", name)
    elif 10 <= local_time < 17:
        print("Добрый день,", name)
    elif 17 <= local_time <= 23:
        print("Добрый вечер,", name)


hello_user_by_time()