import matplotlib.pyplot as plt

sizes = ['10×10', '100×100', '300×300', '500×500', '700×700', '1000×1000']
time_serial = [5.57e-05, 0.0399451, 1.40957, 5.90566, 16.388, 48.7621]
time_omp = [5.42e-05, 0.043515, 1.29846, 5.78371, 16.3683, 47.6666]

plt.figure(figsize=(12, 6))

plt.plot(time_serial, sizes, 'o-', color='blue', linewidth=2, markersize=8, label='Последовательная версия')
plt.plot(time_omp, sizes, 's-', color='green', linewidth=2, markersize=8, label='OpenMP версия')

plt.xlabel('Время выполнения (секунды)', fontsize=12)
plt.ylabel('Размер матрицы', fontsize=12)
plt.title('Сравнение времени выполнения умножения матриц', fontsize=14)

plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)
plt.tight_layout()

plt.show()