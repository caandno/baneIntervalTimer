from functions import *
import pandas as pd
import numpy as np

def main_function(minutes, seconds, length):
    intervals = [400,200,100]
    times_dict = {}
    column_headers = []
    df = pd.DataFrame()
    for interval in intervals:
        time_pr_interval, n_intervals = calculate_time_on_track(minutes, seconds, length, interval) 
        times, n_int = print_time(time_pr_interval, n_intervals)
        times_dict[interval] = times
        column_headers.append(("Interval lengde[m]",interval))
    adjuste_times_dict = populat_empty_cells(times_dict)
    df = pd.DataFrame.from_dict(adjuste_times_dict, orient='columns')
    df.columns = pd.MultiIndex.from_tuples(column_headers)
    return df




if __name__ == "__main__":
    minutes = 4
    seconds = 00
    length = 10000
    df = main_function(minutes, seconds, length)
    
    print(df)