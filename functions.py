def get_data_from_string(data):
    list = data.split('\n')

    while '' in list:
        list.remove('')

    return list


def split_string(string):
    return [char for char in string]
