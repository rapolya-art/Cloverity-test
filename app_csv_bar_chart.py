import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

# Завантаження даних з CSV файлу
df = pd.read_csv('input_data.csv', encoding='utf-8')

# Налаштування для відображення українського тексту
plt.rcParams['font.family'] = 'DejaVu Sans'

# Приклад 1: Топ-20 міст/районів з найвищими значеннями
print("Створення графіку топ-20 міст/районів...")
top_20 = df.nlargest(20, 'Значення')

plt.figure(figsize=(12, 8))
plt.barh(range(len(top_20)), top_20['Значення'].values, color='steelblue')
plt.yticks(range(len(top_20)), top_20['Місто/Район'].values, fontsize=9)
plt.xlabel('Значення', fontsize=12)
plt.title('Топ-20 міст/районів за значенням', fontsize=14, fontweight='bold')
plt.gca().invert_yaxis()
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig('top_20_cities.png', dpi=300, bbox_inches='tight')
plt.show()

# Приклад 2: Середні значення по областях
print("\nСтворення графіку середніх значень по областях...")
avg_by_region = df.groupby('Область')['Значення'].mean().sort_values(ascending=False)

plt.figure(figsize=(14, 8))
colors = plt.cm.viridis(np.linspace(0, 1, len(avg_by_region)))
bars = plt.bar(range(len(avg_by_region)), avg_by_region.values, color=colors)
plt.xticks(range(len(avg_by_region)), avg_by_region.index, rotation=45, ha='right', fontsize=9)
plt.ylabel('Середнє значення', fontsize=12)
plt.title('Середні значення по областях України', fontsize=14, fontweight='bold')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('avg_by_region.png', dpi=300, bbox_inches='tight')
plt.show()

# Приклад 3: Кількість записів по областях
print("\nСтворення графіку кількості міст/районів по областях...")
count_by_region = df['Область'].value_counts().sort_values(ascending=False)

plt.figure(figsize=(14, 8))
plt.bar(range(len(count_by_region)), count_by_region.values, color='coral')
plt.xticks(range(len(count_by_region)), count_by_region.index, rotation=45, ha='right', fontsize=9)
plt.ylabel('Кількість міст/районів', fontsize=12)
plt.title('Кількість міст/районів по областях', fontsize=14, fontweight='bold')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('count_by_region.png', dpi=300, bbox_inches='tight')
plt.show()

print("\nГрафіки успішно створені та збережені!")
print(f"\nЗагальна статистика:")
print(f"Всього записів: {len(df)}")
print(f"Кількість областей: {df['Область'].nunique()}")
print(f"Мінімальне значення: {df['Значення'].min()}")
print(f"Максимальне значення: {df['Значення'].max()}")
print(f"Середнє значення: {df['Значення'].mean():.2f}")
