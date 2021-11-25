import matplotlib.pyplot as plt

movies = ['Энни Холл', 'Бен-Гур', 'Касабланка', 'Ганди', 'Вестсайдская история']
num_oscars = [5, 11, 3, 8, 10]

plt.bar(range(len(movies)), num_oscars)
plt.title("Мои любимые фильмы")
plt.ylabel("Число наград")
# Пометить ось х названиями фильмов в центре каждого столбца
plt.xticks(range(len(movies)), movies)
plt.show()

# Столбчатый график также является хорошим вариантом выбора для построения
# гистограмм сгруппированных числовых значений с целью визуального
# разведывания характера распределения значений:
from collections import Counter

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]

# Сгруппировать оценки nодецильно, но разместить 100 вместе с отметками 90 и вьnnе
histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)

plt.bar([x + 5 for x in histogram.keys()], # сдвинуть столбец влево на 5
        list(histogram.values()), 10) # высота столбца и ширина каждого столбца 10
plt.axis([-5, 105, 0, 5]) # Ось х от -5 до 105; ось у от 0 до 5
plt.xticks([10 * i for i in range(11)]) # Метки по оси x: 0, 10, ..., 100
plt.xlabel("Дециль")
plt.ylabel("Число студентов")
plt.title("Распределение оценок за экзамен №1")
plt.show()