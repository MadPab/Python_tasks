class UserDB:
    def __init__(self, json_data):
        self.users = json_data
        self.age_limits = {
            "Russia": 18,
            "Japan": 20,
            "USA": 21,
            "Thailand": 20
        }

    def users_by_country(self, country):
        return [user for user in self.users if user["country"].lower() == country.lower()]

    def users_by_age(self, age):
        return [user for user in self.users if user["age"] == age]

    def users_older_age(self, age):
        return [user for user in self.users if user["age"] > age]

    def users_younger_or_equal_age(self, age):
        return [user for user in self.users if user["age"] <= age]

    def adult_users(self):
        return [user for user in self.users if user["age"] >= self.age_limits.get(user["country"], 0)]

    def teen_users(self):
        return [user for user in self.users if user["age"] < self.age_limits.get(user["country"], 0)]

    def invalid_records(self):
        return [user for user in self.users if
                user["is_teen"] == (user["age"] < self.age_limits.get(user["country"], 0))]


json_data = [
    {"id": 1, "name": "Vitalii", "fname": "Kotov", "country": "Russia", "age": 29, "is_teen": False},
    {"id": 2, "name": "Oleg", "fname": "Ibragimov", "country": "USA", "age": 12, "is_teen": True},
    {"id": 3, "name": "Slava", "fname": "Kudinov", "country": "Japan", "age": 39, "is_teen": True},
    {"id": 4, "name": "Natasha", "fname": "Olikina", "country": "Russia", "age": 42, "is_teen": False},
    {"id": 5, "name": "Kirill", "fname": "Samsonov", "country": "Thailand", "age": 11, "is_teen": False},
    {"id": 6, "name": "Sveta", "fname": "Eghova", "country": "Russia", "age": 9, "is_teen": False},
    {"id": 7, "name": "Stas", "fname": "Davidov", "country": "USA", "age": 16, "is_teen": False},
    {"id": 8, "name": "Maria", "fname": "Murina", "country": "Thailand", "age": 91, "is_teen": True},
    {"id": 9, "name": "Marina", "fname": "Lobanova", "country": "Russia", "age": 18, "is_teen": False},
    {"id": 10, "name": "Igor", "fname": "Makarov", "country": "USA", "age": 19, "is_teen": True},
    {"id": 11, "name": "Alex", "fname": "Kimberg", "country": "Russia", "age": 22, "is_teen": False},
    {"id": 12, "name": "Sergey", "fname": "Ableev", "country": "Thailand", "age": 17, "is_teen": True},
    {"id": 13, "name": "Inna", "fname": "Ivanova", "country": "USA", "age": 5, "is_teen": False},
    {"id": 14, "name": "Egor", "fname": "Smirnov", "country": "Thailand", "age": 20, "is_teen": False},
    {"id": 15, "name": "Sergey", "fname": "Menshikov", "country": "USA", "age": 33, "is_teen": True},
    {"id": 16, "name": "Elena", "fname": "Zakharova", "country": "Russia", "age": 29, "is_teen": False},
    {"id": 17, "name": "Zena", "fname": "Suvorova", "country": "USA", "age": 63, "is_teen": False},
    {"id": 18, "name": "Katerina", "fname": "Fedorova", "country": "Russia", "age": 34, "is_teen": True},
    {"id": 19, "name": "Mike", "fname": "Makarov", "country": "Thailand", "age": 28, "is_teen": True},
    {"id": 20, "name": "Andrey", "fname": "Olegichken", "country": "Russia", "age": 45, "is_teen": False}
]

db = UserDB(json_data)

country_users = db.users_by_country("Thailand")
for user in country_users:
    print("Пользователи из указанной страны: ", user)
users_with_age_18 = db.users_by_age(18)
for user in users_with_age_18:
    print("Пользователи 18-ти лет: ", user)
users_older_30 = db.users_older_age(30)
for user in users_older_30:
    print("Пользователи старше 18-ти лет: ", user)
users_younger_or_equal_age = db.users_younger_or_equal_age(18)
for user in users_younger_or_equal_age:
    print("Пользователи младше или достигшие 18-ти лет: ", user)
adult_users = db.adult_users()
for user in adult_users:
    print("Совершеннолетние пользователи: ", user)
teen_users = db.teen_users()
for user in teen_users:
    print("Подростки: ", user)
invalid_records = db.invalid_records()
for rec in invalid_records:
    print("Битые записи: ", rec)
