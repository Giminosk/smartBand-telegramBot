import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_dir = 'data/'
img_dir = 'images/'


def get_heart_stats(today, month, heart):
    mean_month_rate = int(np.mean(month['heartRate']))
    cur_rate = today['heartRate'].iloc[-1]
    min_rate = int(np.min(today['heartRate']))
    max_rate = int(np.max(today['heartRate']))
    mean_rate = int(np.mean(today['heartRate']))
      
    return mean_month_rate, cur_rate, min_rate, mean_rate, max_rate


def plot_heart(today, mean=None):
    fig, ax = plt.subplots(1, 1, figsize=(15,5))
    today.plot(x='time', y='heartRate', color='red', linewidth=0.8, ax=ax);
    ax.set_title('Heart rate', fontdict={'fontsize': 16})
    ax.set_xlabel('')
    ax.plot(today['time'], [mean for _ in range(len(today))], '--', linewidth=1);
    plt.savefig(img_dir + 'heart.png')
    plt.close()


def heart_main():
    heart = pd.read_csv(data_dir+'heartRate.csv')
    heart['time'] = pd.to_datetime(heart['time'].astype(str)).dt.time
    
    today = heart['date'].iloc[-1]
    today = heart[heart['date'] == today]
    month = heart['date'].unique()[-30:-1]
    month = heart[heart['date'].isin(month)]
    
    mean_month_rate, cur_rate, min_rate, mean_rate, max_rate = get_heart_stats(today, month, heart)
    
    plot_heart(today, mean_rate)
    
    out1 = f'Agerage heart rate for previous month: {mean_month_rate} bpm\n'
    out2 = f'Daily statistics:\nLast heart rate: {cur_rate} bpm\nMaximal heart rate: {max_rate} bpm\n\
Average heart rate: {mean_rate} bpm\nMinimal heart rate: {max_rate} bpm'
    
    return out1, out2