import json
import re

def get_parasit_words(text, max_amount):
    text_lower = text.lower()
    extract_words = re.findall(r'\b\w+\b', text_lower)

    count_parasit_words = {}

    for word in extract_words:
        no_space_punct = re.sub(r'[^a-zA-Zа-яА-Я]', '', word)
        if not no_space_punct:
            continue

        if no_space_punct in count_parasit_words:
            count_parasit_words[no_space_punct] += 1
        else:
            count_parasit_words[no_space_punct] = 1

    parasit_words = {word: count for word, count in count_parasit_words.items() if count >= max_amount}

    return json.dumps(parasit_words, ensure_ascii=False, indent=4)

text = "Ну что ж я, я найти решения правильного не смогу ж? Смогу ж конечно, я ж старательный все ж таки."
max_amount = 3

result = get_parasit_words(text, max_amount)
print(result)
