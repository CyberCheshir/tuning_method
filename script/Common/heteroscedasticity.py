import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import statsmodels.api as sm
from statsmodels.stats.diagnostic import het_breuschpagan


def breusch_pagan_test(X, y):
    """
    Проводит тест Бройша-Пагана на гетероскедастичность.


    :param X: numpy.ndarray or pandas.DataFrame
        Матрица признаков.
    :param y: numpy.ndarray or pandas.Series
        Вектор зависимой переменной.


    :return:
        - stat: float
            Значение статистики теста.
        - p_value: float
            P-значение теста.
    """
    X = sm.add_constant(X)
    model = sm.OLS(y, X)
    results = model.fit()
    stat, p_value, _, _ = het_breuschpagan(results.resid, X)

    return stat, p_value


def breusch_pagan_draw(X, y):
    """
       Рисует график зависимости переменных с учетом гетероскедастичности и выводит результаты теста Бройша-Пагана.

       :param X: numpy.ndarray or pandas.DataFrame
           Матрица признаков.
       :param y: numpy.ndarray or pandas.Series
           Вектор зависимой переменной.

       :return: None
           Визуализирует график и выводит результаты теста.
       """
    stat, p_value = breusch_pagan_test(X, y)
    cmap = sns.color_palette("plasma", as_cmap=True) if p_value < 0.05 else sns.color_palette("Blues", as_cmap=True)
    sizes = np.sqrt(y) * 3
    plt.figure(figsize=(8, 5))
    plt.scatter(
        X,
        y,
        alpha=0.4,
        c=np.log(y),
        cmap=cmap,
        s=sizes,
    )

    plt.title('График возумещений дисперсии')
    plt.ylabel(r'Площадь торгового зала, м$^2$')
    plt.xlabel('Кол-во сотрудников')
    plt.colorbar(label='Логарифм дисперсии')  # Добавляем цветовую шкалу
    plt.show()
    print(f"Тестовая статистика: {stat}")
    print(f"P-значение: {p_value}")