#!/usr/bin/env python


def main():
    input_numbers = get_numbers()

    max_number_len = len(str(max(input_numbers)))

    (remainder, result) = initiate_remainder_result(max_number_len)

    dict_numbers = numbers_to_dict(input_numbers, max_number_len)

    loop = 1
    while loop:
        for key, r in reversed(list(enumerate(remainder))):
            tmp_res = numbers_addition(key, remainder, dict_numbers)
            if tmp_res > 9:
                if addition_with_remainders(key, tmp_res, remainder,
                                            dict_numbers, result):
                    break
            else:
                result[key] = tmp_res

            if key == 0:
                loop = 0

    print(result)


def addition_with_remainders(key, tmp_res, remainder, dict_numbers, result):
    (rem_value, res_value) = (int(str(tmp_res)[0]), int(str(tmp_res)[1]))

    if key:
        remainder[key-1] = rem_value
        result[key] = res_value
        return 0

    remainder.insert(0, rem_value)
    prepend_new_column(dict_numbers)
    result.pop(key)
    result.insert(key, res_value)
    result.insert(0, 0)
    return 1


def prepend_new_column(dict_numbers):
    for n_key2, n in dict_numbers.items():
        n.insert(0, 0)


def numbers_addition(row, remainder, dict_numbers):
    tmp_res = 0
    for key, numbers in dict_numbers.items():
        tmp_res += numbers[row]
    tmp_res += remainder[row]
    return tmp_res


def numbers_to_dict(input_numbers, max_number_len):
    dict_numbers = {}
    for key, number in enumerate(input_numbers):
        dict_numbers[key] = numbers_to_list(number, max_number_len)

    return dict_numbers


def numbers_to_list(number, max_number_len):
    str_number = str(number)
    number_list = []

    for n in str_number:
        number_list.append(int(n))

    # adjust numbers' list length
    if len(str_number) < max_number_len:
        diff = max_number_len - len(str_number)
        for d in range(diff):
            number_list.insert(0, 0)

    return number_list


def initiate_remainder_result(max_number_len):
    rem = []
    res = []
    for x in range(max_number_len):
        rem.append(0)
        res.append(0)

    return rem, res


def get_numbers():
    input_numbers = []
    input_text = 'Enter number to add (enter to stop): '
    input_number = int(input(input_text) or 0)

    while input_number:
        input_numbers.append(input_number)
        input_number = int(input(input_text) or 0)

    return input_numbers


if __name__ == '__main__':
    main()
