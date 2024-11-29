class Matrix:
    def __init__(self, size):
        self.text = text
        pass  # "образец"

    def input_matrix(self):
         n = int(input("Введите размер матрицы (n x n): "))
         matrix = []
         print("Введите элементы матрицы (через пробел):")
    for i in range(n):
        row = list(map(int, input(f"Строка {i + 1}: ").split()))
        matrix.append(row)
        return matrix
        pass  # "образец"

    def generate_random_matrix(self):
        return [[random.randint(1, 100) for _ in range(size)] for _ in range(size)]
        pass  # "образец"

    def swap_rows_and_columns(self):
       min_row_index = None
       max_col_index = None
       min_value = float('inf')
       max_value = float('-inf')
        # Поиск минимального элемента и максимального элемента
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < min_value:
                min_value = matrix[i][j]
                min_row_index = i
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
                max_col_index = j
                
    # Замена местами строки и столбца
    if min_row_index is not None and max_col_index is not None:
        for i in range(len(matrix)):
            # Смена строки с минимальным элементом на соответствующий столбец
            matrix[min_row_index][i], matrix[i][max_col_index] = matrix[i][max_col_index], matrix[min_row_index][i] 
        pass  # "образец"

    def display_matrix(self):
     for row in matrix:
        print(" ".join(map(str, row)))
        pass  # "образец"

class Menu:
    def print_menu(self):
    print("\nМеню:")
    print("1. Ввод исходных данных вручную")
    print("2. Генерация случайной матрицы")
    print("3. Выполнение алгоритма")
    print("4. Вывод результата")
    print("5. Завершение работы программы")
        pass  # "образец"

def main():
     matrix = None
    
    while True:
        print_menu()
        choice = input("Выберите пункт меню: ")

        if choice == '1':
            matrix = input_matrix()
        elif choice == '2':
            size = int(input("Введите размер матрицы (n x n): "))
            matrix = generate_random_matrix(size)
            print("Сгенерированная матрица:")
            display_matrix(matrix)
        elif choice == '3':
            if matrix is not None:
                swap_rows_and_columns(matrix)
                print("Алгоритм выполнен.")
            else:
                print("Сначала введите данные.")
        elif choice == '4':
            if matrix is not None:
                display_matrix(matrix)
            else:
                print("Сначала введите данные.")
        elif choice == '5':
            print("Завершение работы программы.")
            break
        else:
            print("Неверный выбор.")
    pass  # "образец"

if __name__ == "__main__":
    main()