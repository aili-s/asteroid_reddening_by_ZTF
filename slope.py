import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

# Функція для перетворення ком на крапки в числових даних
def convert_comma_to_dot(value):
    if isinstance(value, str):
        return value.replace(',', '.')
    return value

# 1. Завантаження даних
df = pd.read_csv('D:\Робочий стіл\диплом\Massalia 2.0\Massalia_family_slope_for_python.csv', sep=';')  

print("Перші 5 рядків даних:")
print(df.head())
print("\nСтруктура даних:")
print(df.info())

# 2. Перетворення для всіх стовпців
for col in df.columns:
    df[col] = df[col].apply(convert_comma_to_dot)

# 3. Визначення кількості астероїдів у файлі (для кожного сімейства ~40 об'єктів)
num_asteroids = len(df.columns) // 3
print(f"\nЗнайдено астероїдів: {num_asteroids}")

# 4. Створення списку для збереження
results = []

# 5. Обробка кожного астероїда
for i in range(num_asteroids):
    start_col = i * 3
    asteroid_id = df.columns[start_col]  # ID
    phase_col = df.columns[start_col + 1]  # Фаза
    color_col = df.columns[start_col + 2]  # Кольоровий індекс
    
    print(f"\nОбробка астероїда {asteroid_id}...")
    
    # Отримання даних для поточного астероїда
    asteroid_data = df[[phase_col, color_col]].copy()
    asteroid_data = asteroid_data.dropna()  # Видаляємо пусті рядки
    
    if len(asteroid_data) < 2:
        print(f" Замало даних для астероїда {asteroid_id} (потрібно мінімум 2 точки)")
        continue
    
    try:
        phases = pd.to_numeric(asteroid_data[phase_col], errors='coerce')
        colors = pd.to_numeric(asteroid_data[color_col], errors='coerce')
        
        valid_mask = ~(np.isnan(phases) | np.isnan(colors))
        phases = phases[valid_mask]
        colors = colors[valid_mask]
        
        if len(phases) < 2:
            print(f" Замало валідних даних для астероїда {asteroid_id}")
            continue
            
    except Exception as e:
        print(f" Помилка конвертації для астероїда {asteroid_id}: {e}")
        continue
    
    # 6. Лінійна регресія (нахил + похибка)
    try:
        slope, intercept, r_value, p_value, std_err = stats.linregress(phases, colors)
        
        results.append({
            'asteroid_id': asteroid_id,
            'slope': slope,
            'slope_error': std_err,
            'intercept': intercept,
            'r_squared': r_value**2,
            'p_value': p_value,
            'data_points': len(phases)
        })
        
        print(f" Оброблено: {len(phases)} точок, нахил = {slope:.4f} ± {std_err:.4f}")
        
        if True:
            plt.figure(figsize=(8, 5))
            plt.scatter(phases, colors, alpha=0.7, s=50, color='blue', label='Дані')
            plt.plot(phases, intercept + slope * phases, 'r-', 
                    label=f'Нахил = {slope:.4f} ± {std_err:.4f}')
            plt.xlabel('Фазовий кут')
            plt.ylabel('Кольоровий індекс (G-R)')
            plt.title(f'Астероїд {asteroid_id} ({len(phases)} точок)')
            plt.legend()
            plt.grid(True, linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
        
    except Exception as e:
        print(f" Помилка регресії для астероїда {asteroid_id}: {e}")
        continue

# 7. DataFrame з результатами
if results:
    results_df = pd.DataFrame(results)
    
    # Результати впорядковані за ID
    results_df = results_df.sort_values('asteroid_id')
    pd.set_option('display.float_format', '{:.6f}'.format)
    print(results_df.to_string(index=False))
    
    # 8. Зберігаємо CSV файл
    output_filename = 'asteroid_slopes_results.csv'
    results_df.to_csv(output_filename, index=False, sep=';', decimal='.')
    print(f"\nРезультати збережено у файл: {output_filename}")
    
    # 9. Додатково: статистика результатів
    print(f"\nРЕЗУЛЬТАТ:")
    print(f"Оброблено астероїдів: {len(results_df)}")
    print(f"Середній нахил: {results_df['slope'].mean():.6f}")
    print(f"Медіанний нахил: {results_df['slope'].median():.6f}")
    print(f"Мін. нахил: {results_df['slope'].min():.6f}")
    print(f"Макс. нахил: {results_df['slope'].max():.6f}")
    print(f"Середня похибка: {results_df['slope_error'].mean():.6f}")
    
else:
    print("\nДані відсутні")

print("\nОбробка завершена!")