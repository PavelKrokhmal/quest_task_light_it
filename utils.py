def wait_for_correct_key(text, keys_list):
    while True:
        input_key = input(text)
        if input_key in keys_list: 
            return input_key
