import numpy as np

def input_matrix():
    while True:
        try:
            rows = int(input("Введите количество строк: "))
            cols = int(input("Введите количество столбцов: "))
            if rows <= 0 or cols <= 0:
                raise ValueError("Количество строк и столбцов должно быть положительным числом.")
            matrix = []
            print("Введите элементы матрицы:")
            for i in range(rows):
                row = list(map(float, input().split()))
                if len(row) != cols:
                    raise ValueError("Количество элементов в строке должно быть равно количеству столбцов.")
                matrix.append(row)
            return np.array(matrix)
        except ValueError as e:
            print("Ошибка:", e)

def calculate_rank(matrix):
    return np.linalg.matrix_rank(matrix)

def print_matrix_rank(matrix):
    rank = calculate_rank(matrix)
    print("Ранг матрицы: ", rank)

def main():
    while True:
        print("\nМеню:")
        print("1. Ввести матрицу")
        print("2. Показать введенную матрицу")
        print("3. Показать ранг матрицы")
        print("4. Выход")

        choice = input("Выберите действие (1/2/3/4): ")

        if choice == '1':
            matrix = input_matrix()
            print("Матрица успешно введена.")
        elif choice == '2':
            if 'matrix' in locals():
                print("Введенная матрица:")
                print(matrix)
            else:
                print("Сначала введите матрицу (выберите 1 из меню)")
        elif choice == '3':
            if 'matrix' in locals():
                print_matrix_rank(matrix)
            else:
                print("Сначала введите матрицу (выберите 1 из меню)")
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main()