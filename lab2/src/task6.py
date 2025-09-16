import numpy as np
from scipy.optimize import minimize

SPEED_OF_SIGNAL = 1 

receivers = np.array([
    [0, 0],   
    [10, 0],  
    [0, 10],  
    [10, 10]  
])

true_target_pos = np.array([3.5, 7.2])

print(f"истинное положение объекта: {true_target_pos}\n")

true_distances = np.linalg.norm(receivers - true_target_pos, axis=1)


true_times = true_distances / SPEED_OF_SIGNAL

measured_tdoa = true_times[1:] - true_times[0]

print(f"Измеренные TDoA (относительно R1): {measured_tdoa}\n")


def objective_function(target_pos_guess):    
    estimated_distances = np.linalg.norm(receivers - target_pos_guess, axis=1)
    estimated_times = estimated_distances / SPEED_OF_SIGNAL
    estimated_tdoa = estimated_times[1:] - estimated_times[0]
    error = np.sum((estimated_tdoa - measured_tdoa)**2)
    
    return error

initial_guess = np.array([0, 0])

print("Запускаем Scipy.optimize.minimize для поиска... \n")

result = minimize(
    objective_function, 
    initial_guess, 
    method='L-BFGS-B' 
)

if result.success:
    found_pos = result.x
    print(f"Оптимизация завершена успешно.")
    print(f"  Истинное положение:    {true_target_pos[0]:.4f}, {true_target_pos[1]:.4f}")
    print(f"  Найденное положение:   {found_pos[0]:.4f}, {found_pos[1]:.4f}")
    print(f"  Ошибка (евклидово расстояние): {np.linalg.norm(true_target_pos - found_pos):.6f}")
else:
    print(f"Оптимизация не удалась: {result.message}")