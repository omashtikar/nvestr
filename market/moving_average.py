
def moving_average(price_list: [float], window_size: int):
    i = 0
    moving_average_list = []

    while i < len(price_list) - window_size + 1:
        this_window = price_list[i: i + window_size]
        window_average = sum(this_window) / window_size
        moving_average_list.append(window_average)
        i += 1

    return moving_average_list
