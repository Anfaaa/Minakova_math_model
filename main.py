import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Параметры модели
lambda_rate = float(input("Введите интенсивность потока заявок (λ): "))
mu_rate = float(input("Введите интенсивность обслуживания (μ): "))

# Проверка, чтобы интенсивность потока была меньше интенсивности обслуживания
if lambda_rate >= mu_rate:
    raise ValueError("Интенсивность потока заявок должна быть меньше интенсивности обслуживания.")

# Расчёт показателей модели
L = lambda_rate / (mu_rate - lambda_rate)  # среднее количество клиентов в системе
W = 1 / (mu_rate - lambda_rate)            # среднее время в системе
L_q = (lambda_rate ** 2) / (mu_rate * (mu_rate - lambda_rate))  # среднее количество клиентов в очереди
W_q = lambda_rate / (mu_rate * (mu_rate - lambda_rate))         # среднее время ожидания в очереди

# Выводим результаты
print(f"Среднее количество клиентов в системе (L): {L:.2f}")
print(f"Среднее время пребывания в системе (W): {W:.2f} единиц времени")
print(f"Среднее количество клиентов в очереди (L_q): {L_q:.2f}")
print(f"Среднее время ожидания в очереди (W_q): {W_q:.2f} единиц времени")

# График зависимости L от lambda_rate
lambda_values = np.linspace(0.1, mu_rate - 0.1, 100)
L_values = lambda_values / (mu_rate - lambda_values)

plt.figure(figsize=(10, 6))
plt.plot(lambda_values, L_values, label='L (Среднее количество клиентов в системе)')
plt.xlabel('Интенсивность потока заявок (λ)')
plt.ylabel('L (Среднее количество клиентов в системе)')
plt.title('Зависимость L от λ')
plt.grid(True)
plt.legend()
plt.show()

# График зависимости W от lambda_rate
W_values = 1 / (mu_rate - lambda_values)

plt.figure(figsize=(10, 6))
plt.plot(lambda_values, W_values, label='W (Среднее время пребывания в системе)', color='orange')
plt.xlabel('Интенсивность потока заявок (λ)')
plt.ylabel('W (Среднее время пребывания в системе)')
plt.title('Зависимость W от λ')
plt.grid(True)
plt.legend()
plt.show()

# График зависимости L_q от lambda_rate
L_q_values = (lambda_values ** 2) / (mu_rate * (mu_rate - lambda_values))

plt.figure(figsize=(10, 6))
plt.plot(lambda_values, L_q_values, label='L_q (Среднее количество клиентов в очереди)', color='green')
plt.xlabel('Интенсивность потока заявок (λ)')
plt.ylabel('L_q (Среднее количество клиентов в очереди)')
plt.title('Зависимость L_q от λ')
plt.grid(True)
plt.legend()
plt.show()

# График зависимости W_q от lambda_rate
W_q_values = lambda_values / (mu_rate * (mu_rate - lambda_values))

plt.figure(figsize=(10, 6))
plt.plot(lambda_values, W_q_values, label='W_q (Среднее время ожидания в очереди)', color='red')
plt.xlabel('Интенсивность потока заявок (λ)')
plt.ylabel('W_q (Среднее время ожидания в очереди)')
plt.title('Зависимость W_q от λ')
plt.grid(True)
plt.legend()
plt.show()

# Сохранение результатов в таблицу
data = {
    'lambda (λ)': lambda_values,
    'L (Среднее количество клиентов)': L_values,
    'W (Среднее время пребывания в системе)': W_values,
    'L_q (Среднее количество клиентов в очереди)': L_q_values,
    'W_q (Среднее время ожидания в очереди)': W_q_values
}

df = pd.DataFrame(data)

# Показать таблицу с результатами
print(df.head())
