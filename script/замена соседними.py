import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('../data/1.Обрезка и замена аномалий.csv')
dates = pd.to_datetime(df.columns, format='%d.%m.%Y')

time_series = df.values[3]


def find_gaps(time_series):
    gap_indices = []
    start_index = None

    for i in range(len(time_series)):
        if np.isnan(time_series[i]):
            if start_index is None:
                start_index = i
        else:
            if start_index is not None:
                gap_indices.append([start_index, i - 1])
                start_index = None

    # Если пропуск продолжается до конца временного ряда, сохраняем его конец
    if start_index is not None:
        gap_indices.append([start_index, len(time_series) - 1])

    return gap_indices


plt.plot(time_series)
plt.show()
