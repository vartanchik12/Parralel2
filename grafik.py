import matplotlib.pyplot as plt

# Обновлённые данные
sizes = ['10×10', '100×100', '300×300', '500×500', '700×700', '1000×1000']
time_serial = [5.57e-05, 0.00904, 0.74892, 1.27878, 7.3885, 12.4177]
time_omp = [5.42e-05, 0.004155, 0.29846, 0.25199, 0.7683, 1.61884] 

plt.figure(figsize=(12, 6))

plt.style.use('seaborn-v0_8')

plt.plot(time_serial, sizes, 'o-', color='#1f77b4', linewidth=2.5, 
         markersize=10, label='Последовательная версия', alpha=0.8)
plt.plot(time_omp, sizes, 's-', color='#2ca02c', linewidth=2.5, 
         markersize=10, label='OpenMP версия', alpha=0.8)

for i, (serial, omp) in enumerate(zip(time_serial, time_omp)):
    plt.text(serial + max(time_serial)*0.02, i-0.1, f'{serial:.2e}' if serial < 0.1 else f'{serial:.3f}', 
             color='#1f77b4', va='center', fontsize=9)
    plt.text(omp + max(time_serial)*0.02, i+0.1, f'{omp:.2e}' if omp < 0.1 else f'{omp:.3f}', 
             color='#2ca02c', va='center', fontsize=9)

plt.xlim(0, max(time_serial)*1.1)
plt.xlabel('Время выполнения (секунды)', fontsize=12, labelpad=10)
plt.ylabel('Размер матрицы', fontsize=12, labelpad=10)
plt.title('Сравнение производительности умножения матриц', fontsize=14, pad=20)

plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=11, framealpha=1)
plt.tight_layout()

plt.savefig('matrix_performance_comparison.png', dpi=300, bbox_inches='tight')
plt.show()
