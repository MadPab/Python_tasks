import datetime
import requests


def get_local_time():
    try:
        response = requests.get("http://worldtimeapi.org/api/ip")
        if response.status_code == 200:
            a = response.json()
            offset = a["utc_offset"]
            offset_hours, offset_minutes = map(int, offset[1:].split(":"))
            offset_seconds = offset_hours * 3600 + offset_minutes * 60
            utc = datetime.datetime.utcnow()
            tl = utc + datetime.timedelta(seconds=offset_seconds)
            return tl.hour
        else:
            return None
    except requests.exceptions.RequestException:
        print("Сервис временно недоступен")
        return None


name = input("Введите имя: ")
if not name:
    print("Вы не ввели имя. Если вам нужна помощь, обратитесь в службу поддержки.")
else:
    def time():
        local_time = get_local_time()
        if local_time is not None:
            if 0 <= local_time < 5:
                print("Доброй ночи,", name)
            elif 5 <= local_time < 10:
                print("Доброе утро,", name)
            elif 10 <= local_time < 17:
                print("Добрый день,", name)
            elif 17 <= local_time <= 23:
                print("Добрый вечер,", name)

    time()