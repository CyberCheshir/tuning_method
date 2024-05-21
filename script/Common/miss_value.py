import numpy as np


def replace_nan(time_series: np.array, k: int = 7):
    """
        Заменяет значения NaN во временном ряде значениями из окружающих точек в заданном окне.
        :param time_series: numpy.array
            Одномерный массив, представляющий временной ряд данных.
        :param k: int, optional
            Половина размера окна вокруг каждого значения NaN, где используются окружающие значения для замены. По умолчанию равно 7.

        :return: numpy.array
            Копия входного временного ряда с замененными значениями NaN на окружающие значения в указанном окне.
    """
    copy_ts = time_series.copy()
    for i, value in enumerate(time_series):
        if np.isnan(value):
            copy_ts[i - k: i + k] = np.nan
    return copy_ts
