import numpy as np
import pandas as pd
import scipy


def task1(data):
    print("Завдання 1")
    a = np.array(data["fage"])
    print(f"Середній вік батька - {np.mean(a)}")
    print(f"Медіана - {np.median(a)}")
    print(f"Мода - {scipy.stats.mode(a)}")
    print("--------------")


def task2(data):
    print("Завдання 2")
    b = np.array(data["mppwt"])
    print("Перевіряємо чи за нормальним законом розподілена вибірка ваги матері:")
    c = scipy.stats.normaltest(b)
    if c[1] < 0.05:
        print("Вибірка не розподілена за нормальним розподілом")
    else:
        print("Є ймовірність, що сукупність розподілена за нормальним законом")
    print("--------------")


def task3(data):
    print("Завдання 3")
    smokeornon_group = np.array(data["fnocig"])
    weight_babies = np.array(data["lowbwt"])
    smoke_group = weight_babies[smokeornon_group == 0]
    nonsmoke_group = weight_babies[smokeornon_group > 0]
    res = scipy.stats.mannwhitneyu(smoke_group, nonsmoke_group)
    if res[1] < 0.05:
        print("Є велика різниця, у вагах")
    else:
        print("Не можна відхиляти гіпотезу, що немає різниці, чи чоловік палить чи ні")
    print("----------------")


def task4(data):
    print("Завдання 4")
    baby_weight = np.array(data["Birthweight"])
    mother_weight = np.array(data["mppwt"])
    res = scipy.stats.pearsonr(baby_weight, mother_weight)
    print(res)
    if -1 <= res[0] < -0.65:
        print("Зв'язок від'ємний сильний")
    elif -0.65 <= res[0] < -0.1:
        print("Зв'язок від'ємний слабкий")
    elif -0.1 <= res[0] <= 0.1:
        print("Зв'язок дуже слабкий")
    elif 0.1 <= res[0] <= 0.65:
        print("Зв'язок позитивний слабкий")
    else:
        print("Зв'язок позитивний сильний")


if __name__ == "__main__":
    data = pd.read_csv("Birthweight.csv")
    task1(data)
    task2(data)
    task3(data)
    task4(data)
