def wait_for_correct_key(text, keys_list):
    while True:
        input_key = input(text)
        if input_key in keys_list:
            return input_key


def get_value_within_boundaries(value, left, right):
    if value > right:
        return right
    if value < left:
        return left
    return value
