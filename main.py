def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

# Пример массива с ростом учеников
heights = (160, 165, 168, 170, 172, 175, 180)

# Рост, который мы ищем
target_height = 170

# Вызываем функцию бинарного поиска
if binary_search(heights, target_height):
    print("Ученик с ростом 170 см найден.")
else:
    print("Ученик с ростом 170 см не найден.")




def elements_above_secondary_diagonal(matrix):
    n = len(matrix)
    result = []

    for i in range(n):
        for j in range(n):
            if i + j < n - 1:  # Проверка, находится ли элемент над побочной диагональю
                result.append(matrix[i][j])

    return tuple(result)

# Пример использования:
n = 4  # Задайте размерность матрицы n x n
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

result_tuple = elements_above_secondary_diagonal(matrix)
print(result_tuple)




def shift_and_remove_element(lst, k):
    if 0 <= k < len(lst):
        for i in range(k, len(lst) - 1):
            lst[i] = lst[i + 1]  # Сдвигаем элементы влево
        lst.pop()  # Удаляем последний элемент

# Пример использования:
my_list = [1, 2, 3, 4, 5]
k = 2  # Индекс элемента, который нужно удалить

shift_and_remove_element(my_list, k)
print(my_list)  # Выводим список после удаления элемента

def diff(set1, set2, set3, symmetric=True):
    if symmetric:
        # Симметричная разность
        result = set1.symmetric_difference(set2).symmetric_difference(set3)
    else:
        # Простая разность
        result = set1.difference(set2).difference(set3)
    return result

# Пример использования:
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}
setC = {4, 5, 6, 7}

symmetric_result = diff(setA, setB, setC, symmetric=True)
difference_result = diff(setA, setB, setC, symmetric=False)

print("Симметричная разность:", symmetric_result)
print("Простая разность:", difference_result)

from collections import defaultdict


def build_genealogy_tree(N, relationships):
    graph = defaultdict(list)
    heights = {}

    for child, parent in relationships:
        graph[parent].append(child)

    def dfs(node, height):
        heights[node] = height
        for child in graph[node]:
            dfs(child, height + 1)

    dfs('Родоначальник', 0)

    return heights


# Чтение входных данных
N = int(input())
relationships = [input().split() for _ in range(N - 1)]

# Построение генеалогического древа и вычисление высот
heights = build_genealogy_tree(N, relationships)

# Вывод имен элементов и их высот
sorted_names = sorted(heights.keys())
for name in sorted_names:
    print(name, heights[name])
