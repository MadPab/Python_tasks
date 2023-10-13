def split_words(words):
    fixed_list = []
    for word in words:
        split_words = word.split()
        fixed_list.extend(split_words)
    print(fixed_list)


words = ["apple banana", "orange", "banana", "kiwi strawberry blueberry"]

split_words(words)