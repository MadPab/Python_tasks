class Helper:
    def get_string(self, input_str: str, max_len: int, end: str):
        if len(input_str) < max_len:
            return input_str

        split_str = input_str.split()
        new_str = ""

        for element in split_str:
            if len(new_str) + len(element) > max_len:
                break
            new_str += element + " "

        new_str += end
        return new_str.strip()


string = "Этот код написан на не выдуманном языке программирования"
max_len = 35
ending = 'Good job!'

result = Helper().get_string(string, max_len, ending)
print(result)
