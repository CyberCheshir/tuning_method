from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter


def custom_formatter(x, pos):
    """
    Функция для форматирования меток на шкале y в тысячах и миллионах.__

    Parameters:
    - x (float): Значение на оси y, которое нужно отформатировать.
    - pos (int): Позиция метки на оси.

    Returns:
    - str: Отформатированная строка для отображения на шкале y.
    """
    if x >= 1e6:
        return f'{x / 1e6:.0f}M'
    elif x >= 1e3:
        return f'{x / 1e3:.0f}K'
    elif x < 1e3:
        return f'{x :.0f}'


def draw_ts_market(ts, dates, title: str, path='../img/'):
    plt.figure(figsize=(13, 3))
    plt.plot(dates, ts, linewidth=0.8)

    # Настройка шкалы y
    formatter = FuncFormatter(custom_formatter)
    plt.gca().yaxis.set_major_formatter(formatter)

    # Добавление заголовков и меток осей
    plt.title(title)
    plt.xlabel('Дата')
    plt.ylabel('Выручка, руб.')
    plt.savefig(f'{path}{title}.png')
    plt.close()
