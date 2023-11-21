"Генератор паролей, использующий имена (или слов вместо имен, которые начинаются на одну букву)"""

"""Генератор цитат"""

class PasswordEncryptor:
    def __init__(self):
        self.name_dict = {
            '0': 'Отец',
            '1': 'Онуфрий',
            '2': 'Осматривал',
            '3': 'Озеро',
            '4': 'Объекты',
            '5': 'Озадачены',
            '6': 'Обезличивание',
            '7': 'Оценка',
            '8': 'Оттождествлять',
            '9': 'Особенный'
        }

    def encrypt_password(self, password):
        encrypted_password = ''.join(self.name_dict.get(char, char) for char in password)
        return encrypted_password

    def decrypt_password(self, encrypted_password):
        reversed_name_dict = {v.lower(): k for k, v in self.name_dict.items()}
        decrypted_password = ''.join(reversed_name_dict.get(word.lower(), word) for word in encrypted_password.split())
        return decrypted_password


encryptor = PasswordEncryptor()

password = "16379032458"
encrypted_password = encryptor.encrypt_password(password)
print("Encrypted Password:", encrypted_password)

decrypted_password = encryptor.decrypt_password(encrypted_password)
print("Decrypted Password:", decrypted_password)



from numba import njit

@njit
def get_solution():
    total = 0
    for a in range(1, 151):
        for b in range(a, 151):
            for c in range(b, 151):
                for d in range(c, 151):
                    for e in range(d, 151):
                        if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
                            total += 1
                            print(a, b, c, d, e)
                            print('a + b + c + d + e =', a + b + c + d + e)
                            if total == 1:
                                break
    print('Общее количество натуральных решений =', total)


if __name__ == "__main__":
    get_solution()