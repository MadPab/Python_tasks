import hashlib
import pickle


def salt_and_hash_generator(some_string, file_to_save_hash):
    salt = str(len(some_string))

    md5 = hashlib.md5()
    md5.update(salt.encode('utf-8'))
    md5.update(some_string.encode('utf-8'))
    hash1 = md5.hexdigest()

    data = {'salt': salt, 'data': some_string, 'hash': hash1}

    with open(file_to_save_hash, 'ab') as file:
        pickle.dump(data, file)


def find_hash(hash_to_find, file_to_save_hash):
    try:
        with open(file_to_save_hash, 'rb') as file:
            while True:
                try:
                    data = pickle.load(file)
                    if data['hash'] == hash_to_find:
                        return {'salt': data['salt'], 'data': data['data']}
                except EOFError:
                    break
        raise Exception("Хеш не найден")
    except FileNotFoundError:
        raise Exception("Файл не найден")


some_string = 'asdf123'
file_to_save_hash = 'testfile'

salt_and_hash_generator(some_string, file_to_save_hash)

hash_to_find = 'd586ea635508f14f70656a8483c02baa'

try:
    result = find_hash(hash_to_find, file_to_save_hash)
    print("Изначальное значение:", result['data'], "Соль:", result['salt'])
except Exception as e:
    print(e)
