import re


def is_valid_date(date_string):
    pattern = r'^(\d{2}\.){2}\d{4}$|^\d{2}\.\d{2}$'
    return bool(re.match(pattern, date_string))


def is_valid_priority(priority_string):
    return priority_string in ['Низкий', 'Средний', 'Высокий']


def is_not_none(other_string):
    return bool(other_string)


def check_data(data):
    return is_not_none(data[0]) and is_not_none(data[1]) and is_not_none(data[2]) and is_valid_date(
        data[3]) and is_valid_priority(data[4])
