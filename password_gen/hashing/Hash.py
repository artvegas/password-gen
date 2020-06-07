import hashlib


special_characters_list = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
                           ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

upper_case_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                   'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

lower_case_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                   'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def return_hash(key, api=None, minimum_length=12, upper_case=True, numbers=True, special_characters=True):

    m = hashlib.sha256()
    s = hashlib.shake_128()
    s.update(b'{key}')
    m.update(b'{key}')
    return s.digest(minimum_length)


print(return_hash("My Password"))
