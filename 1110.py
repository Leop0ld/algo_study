input_number = int(input())

def get_result(number):
    count = 0
    new_number = number
    while True:
        if number == new_number and count >= 1:
            break
        else:
            new_number = (new_number % 10) * 10 + (new_number // 10 + new_number % 10) % 10
            count += 1

    return count


print(get_result(input_number))
