import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_dir = 'data/'
img_dir = 'images/'


def plot_activity_month(month):
    x_axis = month['date'].apply(lambda x: x[5:])
    
    fig, ax = plt.subplots(1, 1, figsize=(15,5))
    plt.bar(x_axis, month['steps'], color='#62d1ae')
    ax.set_xticks([x if i % 2 == 0 else '' for i, x in enumerate(x_axis)])
    
    mean = np.mean(month['steps'])
    ax.plot(x_axis, [mean for _ in range(len(month))], '--', linewidth=1, color='red')
    ax.set_title('Last month steps', fontdict={'fontsize': 16})
    ax.set_ylabel('Steps', fontdict={'fontsize': 14})

    plt.savefig(img_dir + 'activity.png')
    plt.close()


def activity_main():
    activity = pd.read_csv(data_dir+'activityDaily.csv')
    
    today = activity.iloc[-1]
    month = activity.iloc[-30:]
    
    out1 = f'Today you walked {today["steps"]} steps, which is {today["distance"]/1000} km, and burned {today["calories"]} calories'
    
    diff = int(np.mean(month['steps'])) - today['steps']
    out2 = f'\nIt is {diff} steps {"bigger" if diff >= 0 else "smaller"} than last month average:' 
    
    plot_activity_month(month)
    
    return out1, out2
