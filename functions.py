def get_data_from_string(data, split_char='\n'):
    list = data.split(split_char)

    while '' in list:
        list.remove('')

    return list


def split_string(string):
    return [char for char in string]
