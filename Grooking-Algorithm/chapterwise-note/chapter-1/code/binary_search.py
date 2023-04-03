def binary_search(list, item):
    # define high, low
    low_pos = 0
    high_pos = len(list) - 1
    while low_pos <= high_pos:
        mid_pos = int((low_pos + high_pos) / 2)
        guess = list[mid_pos]
        if guess == item:
            return mid_pos
        if guess > item:
            high_pos = mid_pos - 1
        else:
            low_pos = mid_pos + 1
    return None


if __name__ == '__main__':
    search_list = [1, 3, 5, 7, 9]
    print(binary_search(search_list, 3))
