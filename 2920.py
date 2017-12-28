
def get_result(arr):
    if sorted(arr) == arr:
        print('ascending')
    elif sorted(arr, reverse=True) == arr:
        print('descending')
    else:
        print('mixed')


input_arr = list(map(int, input().split(' ')))

get_result(input_arr)
