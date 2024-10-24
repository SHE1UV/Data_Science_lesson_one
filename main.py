import pandas as pd
from random import randint
import argparse

def analyze_students(table, n, pivot_columns):
    matem_grade = [randint(3, 5) for _ in range(len(table))]
    rus_grade = [randint(3, 5) for _ in range(len(table))]
    info_grade = [randint(3, 5) for _ in range(len(table))]
    
    table['matem'] = matem_grade
    table['rus'] = rus_grade
    table['info'] = info_grade

    table['mean'] = (table['matem'] + table['rus'] + table['info']) / 3

    table['paral'] = [9 if i % 2 == 1 else 10 for i in range(len(table))]
    
    students = table.sort_values(by='mean', ascending=False).reset_index(drop=True)

    students = students[['paral', 'bykva', 'name', 'matem', 'rus', 'info', 'mean']]
    
    top_students = students.head(n).reset_index(drop=True)

    pivot_table = students.pivot_table(index=pivot_columns, values='mean', aggfunc='mean').round(2).fillna(0)
    
    return top_students, pivot_table


def main():
    parser = argparse.ArgumentParser(description='Анализ успеваемости учеников')
    parser.add_argument('--n', type=int, default=10, help='Количество лучших учеников для вывода')
    parser.add_argument('--pivot', nargs='*', required=True, help='Столбцы для сводной таблицы (например: bykva paral)')
    parser.add_argument('--class_name', choices=['A', 'B'], default='A', help='Выбор класса для анализа (A или B)')

    args = parser.parse_args()

    klass = {
        'A': [
            'Иванов', 'Смирнов', 'Кузнецов', 'Попов', 
            'Васильев', 'Петров', 'Соколов', 'Михайлов', 
            'Новиков', 'Федоров'
        ],
        'B': [
            'Морозов', 'Волков', 'Алексеев', 'Лебедев', 
            'Семенов', 'Егоров', 'Павлов', 'Козлов', 
            'Степанов', 'Николаев'
        ]
    }

    selected_class = args.class_name
    table = pd.DataFrame(klass[selected_class], columns=['name'])
    table['bykva'] = selected_class  

    top_students, pivot_table = analyze_students(table, n=args.n, pivot_columns=args.pivot)

    print(f"Лучшие ученики:\n{top_students}")
    print(f"\nСредняя успеваемость по классам и параллелям:\n{pivot_table}")


if __name__ == "__main__":
    main()

