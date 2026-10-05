import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# ==========================================
# Part 2 & Part 3: Чтение данных и производные
# ==========================================

# 1. Загружаем данные из freefall.csv
# Поля: time, y (время в секундах, высота в метрах)
data = np.genfromtxt('freefall.csv', delimiter=',', names=True)
t = data['time']
y = data['y']

# 2. Вычисляем скорость (v = dy/dt) и ускорение (a = dv/dt) через np.gradient
v = np.gradient(y, t)
a = np.gradient(v, t)

# 3. Выводим среднее значение и стандартное отклонение ускорения
mean_a = np.mean(a)
std_a = np.std(a)

print(f"--- Part 2 & 3 Results ---")
print(f"Mean acceleration: {mean_a:.3f} m/s^2")
print(f"Standard deviation of acceleration: {std_a:.3f}\n")

# ==========================================
# Part 4: Интегрирование обратно (Integrating back)
# ==========================================

# 1. Интегрируем шумное ускорение обратно до скорости
# Добавляем начальную скорость v[0]
v_rec = cumulative_trapezoid(a, t, initial=0) + v[0]

# 2. Интегрируем полученную скорость обратно до координаты
# Добавляем начальную высоту y[0]
y_rec = cumulative_trapezoid(v_rec, t, initial=0) + y[0]

# 3. Вычисляем максимальную разницу между исходной высотой и восстановленной
max_diff = np.max(np.abs(y - y_rec))

print(f"--- Part 4 Results ---")
print(f"Max difference between original and reconstructed position: {max_diff:.4f} m\n")

# ==========================================
# Part 5: Построение графиков (motion.png)
# ==========================================

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 10), sharex=True)

# Верхний график: Высота (Position)
ax1.plot(t, y, label='Original Position (y)', color='blue')
ax1.set_ylabel('Position (m)')
ax1.set_title('Motion Analysis: Freefall')
ax1.grid(True)
ax1.legend()

# Средний график: Скорость (Velocity)
ax2.plot(t, v, label='Velocity (v)', color='orange')
ax2.set_ylabel('Velocity (m/s)')
ax2.grid(True)
ax2.legend()

# Нижний график: Ускорение (Acceleration)
ax3.plot(t, a, label='Calculated Acceleration (a)', color='red', alpha=0.6)
ax3.axhline(-9.81, color='black', linestyle='--', label='Target g (-9.81 m/s²)')
ax3.set_xlabel('Time (s)')
ax3.set_ylabel('Acceleration (m/s²)')
ax3.grid(True)
ax3.legend()

plt.tight_layout()
plt.savefig('motion.png', dpi=300)
plt.close()
print("Saved motion.png successfully!")

# ==========================================
# Bonus: 2D Trajectory & Speed
# ==========================================
try:
    traj_data = np.genfromtxt('trajectory.csv', delimiter=',', names=True)
    t_2d = traj_data['time']
    x_2d = traj_data['x']
    y_2d = traj_data['y']

    vx_2d = np.gradient(x_2d, t_2d)
    vy_2d = np.gradient(y_2d, t_2d)
    speed = np.sqrt(vx_2d**2 + vy_2d**2)

    fig_b, (ax_b1, ax_b2) = plt.subplots(1, 2, figsize=(12, 5))

    # Траектория 2D
    ax_b1.plot(x_2d, y_2d, color='purple')
    ax_b1.set_xlabel('X (m)')
    ax_b1.set_ylabel('Y (m)')
    ax_b1.set_title('2D Path (x vs y)')
    ax_b1.grid(True)

    # Скорость от времени
    ax_b2.plot(t_2d, speed, color='green')
    ax_b2.set_xlabel('Time (s)')
    ax_b2.set_ylabel('Speed (m/s)')
    ax_b2.set_title('Speed over Time')
    ax_b2.grid(True)

    plt.tight_layout()
    plt.savefig('trajectory_bonus.png', dpi=300)
    plt.close()
    print("Bonus completed and trajectory_bonus.png saved!")
except Exception as e:
    print(f"Bonus skipped or file trajectory.csv missing: {e}")