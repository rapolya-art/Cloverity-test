import csv
from collections import defaultdict

# Читання CSV файлу вбудованими засобами Python
def read_csv(filename):
    data = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append({
                'Область': row['Область'],
                'Місто/Район': row['Місто/Район'],
                'Значення': int(row['Значення'])
            })
    return data

# Знаходження топ-N записів
def get_top_n(data, n=20):
    sorted_data = sorted(data, key=lambda x: x['Значення'], reverse=True)
    return sorted_data[:n]

# Обчислення середніх значень по областях
def calculate_avg_by_region(data):
    region_data = defaultdict(lambda: {'sum': 0, 'count': 0})
    
    for row in data:
        region = row['Область']
        region_data[region]['sum'] += row['Значення']
        region_data[region]['count'] += 1
    
    averages = {}
    for region, values in region_data.items():
        averages[region] = values['sum'] / values['count']
    
    # Сортування за спаданням
    sorted_avg = sorted(averages.items(), key=lambda x: x[1], reverse=True)
    return sorted_avg

# Підрахунок кількості міст/районів по областях
def count_by_region(data):
    counts = defaultdict(int)
    for row in data:
        counts[row['Область']] += 1
    
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_counts

# Текстова візуалізація (замість графіків)
def print_bar_chart(data, title, max_bar_length=50):
    print(f"\n{'='*70}")
    print(f"{title:^70}")
    print(f"{'='*70}\n")
    
    if not data:
        print("Немає даних для відображення")
        return
    
    # Знаходимо максимальне значення для масштабування
    max_value = max(item[1] for item in data)
    
    for i, (label, value) in enumerate(data, 1):
        # Обчислюємо довжину стовпчика
        bar_length = int((value / max_value) * max_bar_length)
        bar = '█' * bar_length
        
        # Виводимо дані
        print(f"{i:2}. {label:30} │{bar} {value:.0f}")

# Виведення статистики
def print_statistics(data):
    values = [row['Значення'] for row in data]
    regions = set(row['Область'] for row in data)
    
    print(f"\n{'='*70}")
    print(f"{'ЗАГАЛЬНА СТАТИСТИКА':^70}")
    print(f"{'='*70}")
    print(f"Всього записів:        {len(data)}")
    print(f"Кількість областей:    {len(regions)}")
    print(f"Мінімальне значення:   {min(values)}")
    print(f"Максимальне значення:  {max(values)}")
    print(f"Середнє значення:      {sum(values)/len(values):.2f}")
    print(f"{'='*70}\n")

# Основна програма
def main():
    print("Завантаження даних з CSV...")
    
    try:
        # Читання даних
        data = read_csv('input_data.csv')
        
        # Виведення статистики
        print_statistics(data)
        
        # Топ-20 міст/районів
        top_20 = get_top_n(data, 20)
        top_20_formatted = [(row['Місто/Район'], row['Значення']) for row in top_20]
        print_bar_chart(top_20_formatted, "ТОП-20 МІСТ/РАЙОНІВ ЗА ЗНАЧЕННЯМ")
        
        # Середні значення по областях
        avg_by_region = calculate_avg_by_region(data)
        print_bar_chart(avg_by_region, "СЕРЕДНІ ЗНАЧЕННЯ ПО ОБЛАСТЯХ")
        
        # Кількість міст/районів по областях
        counts = count_by_region(data)
        print_bar_chart(counts, "КІЛЬКІСТЬ МІСТ/РАЙОНІВ ПО ОБЛАСТЯХ")
        
        print("\n✅ Аналіз завершено успішно!\n")
        
    except FileNotFoundError:
        print("❌ Помилка: Файл 'input_data.csv' не знайдено!")
    except Exception as e:
        print(f"❌ Помилка: {e}")

if __name__ == "__main__":
    main()