def get_input():
    minutes = int(input("Enter the number of minutes: "))
    seconds = int(input("Enter the number of seconds: "))
    length = int(input("Enter the length of the track: "))
    return minutes, seconds, length

def calculate_time_on_track(minutes, seconds, length, interval):
    total_seconds = minutes * 60 + seconds
    distance_pr_time = length/1000* total_seconds
    n_intervals = length/interval
    time_pr_interval = distance_pr_time / n_intervals
    return time_pr_interval, n_intervals

def convert_seconds(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return int(minutes), int(seconds)

def print_time(time_pr_interval, n_intervals):
    time_n_intervals = 0
    time_lst = []
    n_int_list = []
    for i in range(int(n_intervals)):
        time_n_intervals += time_pr_interval
        minutes, seconds = convert_seconds(time_n_intervals)
        if len(str(seconds)) == 1:
            seconds = f'0{seconds}'
        n_int_list.append(f'{i+1}')
        time_lst.append(f'{minutes}:{seconds}')
        
        # print(f"Interval {i+1}: {minutes}:{seconds}")
    # return time_lst, range(int(n_intervals))
    return time_lst, n_int_list

def create_times(time_pr_interval, n_intervals):
    time_n_intervals = 0
    time_lst = []
    for i in range(int(n_intervals)):
        time_n_intervals += time_pr_interval
        minutes, seconds = convert_seconds(time_n_intervals)
        if len(str(seconds)) == 1:
            seconds = f'0{seconds}'
        time_lst.append(f'{minutes}:{seconds}')
        
        # print(f"Interval {i+1}: {minutes}:{seconds}")
    return time_lst, range(int(n_intervals))

def populat_empty_cells(dict):
    max_len = max(len(v) for v in dict.values())
    for k, v in dict.items():
        if len(v) < max_len:
            dict[k] = v + [''] * (max_len - len(v))

    return dict