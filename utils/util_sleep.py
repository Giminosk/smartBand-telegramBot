import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_dir = 'data/'
img_dir = 'images/'


def convert_minutes(time):
    return float(f'{int(np.floor(time / 60))}.{round(time / 60 % 1 * 60)}')


def get_sleep_stats(today):
    deep = (convert_minutes(today['deepSleepTime']), today['deepSleepTime'] / today['totalSleepTime'] // 0.01)
    shallow = (convert_minutes(today['shallowSleepTime']), today['shallowSleepTime'] / today['totalSleepTime'] // 0.01)
    rem = (convert_minutes(today['REMTime']), today['REMTime'] / today['totalSleepTime'] // 0.01) 
    wake = today['wakeTime']
    
    return convert_minutes(today['totalSleepTime']), deep, shallow, rem, wake


def sleep_compare(month, today):
    total_diff = np.mean(month['totalSleepTime']) - today['totalSleepTime']
    deep_diff = np.mean(month['deepSleepTime']) - today['deepSleepTime']
    
    return convert_minutes(total_diff), convert_minutes(deep_diff)


def plot_sleep(today):
    stats = [today['deepSleepTime'], today['shallowSleepTime'], today['REMTime']]
    fig, ax = plt.subplots(1, 1, figsize=(15,5))
    plt.pie(stats, labels = ['Deep sleep', 'Shallow sleep', 'REM'], autopct='%.2f%%')
    plt.title(f'You slept {convert_minutes(today["totalSleepTime"])} hours:', fontdict={'fontsize': 16})
    plt.savefig(img_dir + 'sleep.png')
    plt.close()


def sleep_main():
    sleep = pd.read_csv(data_dir+'sleep.csv')
    sleep = sleep[sleep.columns[:7]]
    
    today = sleep.iloc[-1]
    month = sleep.iloc[-30:-1]
    
    total, deep, shallow, rem, wake = get_sleep_stats(today)
    out1 = f'Your last sleep:\n\nTotal sleep time: {total} hours\
\n\nDeep sleep: {deep[0]} hour is {deep[1]}% of total sleep time\
\n\nShallow sleep: {shallow[0]} hour is {shallow[1]}% of total sleep time\
\n\nREM phase: {rem[0]} hour is {rem[1]}% of total sleep time\
\n\nWake period: {wake} minutes'
    
    total_diff, deep_diff = sleep_compare(month, today)
    out2 = f'\nThis night you slept {abs(total_diff)} hours {"more" if total_diff >= 0 else "less"} than last month, \n\nand your deep sleep was \
{abs(deep_diff)} hours {"longer" if deep_diff >= 0 else "shorter"}'

    plot_sleep(today)
    
    return out1, out2