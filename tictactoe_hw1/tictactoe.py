"""
1. Допустима реалиция без использоавния классов.
Пользовательский ввод осуществляется с помощью input, который необходимо
валидировать и выводить понятное описание ошибки.
Схема класса не обязательно должна быть такой, можно добавлять и менять методы,
держа в голове грамотную организацию кода, ненужное дублирование и код-лапшу.
По желанию, можно написать вспомогательную функцию, запустив которую, компьютер
сыграет сам с собой без участия человека,либо сделать возможным игру между
человеком и компьютером.

2. Написать тесты (unittest, assert) для игры, покрыв тестами основные методы
3. Проверить корректность и стиль кода с помощью pylint или flake8
"""

class TicTacGame:
    """Класс игры Крестики vs Нолики"""
    def __init__(self):
        """конструктор"""
        # создаем словарь от 1 до 9, заполняем их номером ячейки
        self.x_and_o_position = {field: str(field) for field in range(1, 10)}


    def show_board(self):
        """функция, показывающая положение игровой доски"""
        print("\n")

        print("\t     |     |")

        print(f"\t  {self.x_and_o_position[1]} "
              f" |  {self.x_and_o_position[2]} "
              f" |  {self.x_and_o_position[3]}")

        print('\t_____|_____|_____')

        print("\t     |     |")

        print(f"\t  {self.x_and_o_position[4]} "
              f" |  {self.x_and_o_position[5]} "
              f" |  {self.x_and_o_position[6]}")

        print('\t_____|_____|_____')

        print("\t     |     |")

        print(f"\t  {self.x_and_o_position[7]} "
              f" |  {self.x_and_o_position[8]} "
              f" |  {self.x_and_o_position[9]}")

        print("\t     |     |")

        print("\n")


    def validate_input(self, field_id):
        """функция, проверяющая ввод пользователя"""
        # проверка на правильный ввод
        if not field_id.isnumeric():
            print("Неправильный ввод.")
            return False

        if not 1 <= int(field_id) <= 9:
            print("Введите допустимое значение номера поля.")
            return False

        # проверка на выбор уже занятой ячейки
        if self.x_and_o_position[int(field_id)] in ["X", "O"]:
            print("Это поле уже занято. Выберите свободное.")
            return False

        return True


    def start_game(self):
        """функция запуска игры"""
        def show_stats(user1_wins, user2_wins):
            """функция, показывающая статистику игры"""
            print(f"\t\t  Счет\n"
                  f"_______________________\n"
                  f"Игрок 1: {user1_wins}; Игрок 2: {user2_wins}\n"
                  f"_______________________")

        def print_winner(user1_wins, games_to_win):
            """функция, показывающая победителя всей серии игр"""
            if user1_wins == games_to_win:
                print("Победил игрок 1.\nДо свидания!")
            else:
                print("Победил игрок 2.\nДо свидания!")
        print("Вы запустили консольную версию игры крестики нолики.\n"
              "Игрок 1 рисует X (крестики), Игрок 2 рисует O (нолики).\n"
              "Номер игрока, начинающего партию, чередуется.")
        games_to_win = input("Введите количество игр, которые вы хотите "
                             "сыграть до подведения итогов: ")
        while not games_to_win.isnumeric() or int(games_to_win) <= 0:
            games_to_win = input("Неправильный ввод.\n"
                                 "Введите количество игр, которые вы хотите "
                                 "сыграть до подведения итогов: ")

        games_to_win = int(games_to_win)
        start_user_id = 1
        user1_wins = 0
        user2_wins = 0
        user_id = 1
        while games_to_win not in (user1_wins, user2_wins):
            self.show_board()
            field_id = input(f"Игрок {user_id}, введите номер свободного поля: ")
            while not self.validate_input(field_id):
                field_id = input(f"Игрок {user_id}, введите номер свободного поля: ")

            self.x_and_o_position[int(field_id)] = "X" if user_id == 1 else "O"

            if self.check_winner(user_id):
                self.show_board()
                self.clear_board()
                # смена хода и прибавление победы
                if user_id == 1:
                    user1_wins += 1
                    if start_user_id == 1:
                        user_id = 2
                        start_user_id = 2
                    else:
                        start_user_id = 1

                else:
                    user2_wins += 1
                    if start_user_id == 2:
                        user_id = 1
                        start_user_id = 1
                    else:
                        start_user_id = 2

                show_stats(user1_wins, user2_wins)

            elif self.check_draw():
                self.show_board()
                self.clear_board()
                show_stats(user1_wins, user2_wins)
                # смена хода
                user_id, start_user_id = (2, 2) if user_id == 1 else (1, 1)

            # смена хода
            else:
                user_id = 1 if user_id == 2 else 2
        print_winner(user1_wins, games_to_win)
        return True


    def clear_board(self):
        """функция очистки игрового поля"""
        self.x_and_o_position = {field: str(field) for field in range(1, 10)}


    def check_draw(self):
        """функция, проверяющая наличие ничьи"""
        fields_values = list(self.x_and_o_position.values())
        for field_value in fields_values:
            if field_value.isnumeric():
                return False

        print("Ничья")
        return True


    def check_winner(self, user_id):
        """функция, проверяющая наличие победителя (все комбинации)"""
        def check_combination(field1, field2, field3):
            """функция, проверяющая комбинацию"""
            if (self.x_and_o_position[int(field1)]
                    == self.x_and_o_position[int(field2)] ==
                    self.x_and_o_position[int(field3)]):
                print(f"Игрок {user_id} выиграл партию!\n"
                      f"Победная комбинация: {field1, field2, field3}")
                return True
            return False

        # проверяем по горизонтали
        for field in range(1, 10, 3):
            if check_combination(field, field + 1, field + 2):
                return True
        # проверяем по вертикали
        for field in range(1, 4):
            if check_combination(field, field + 3, field + 6):
                return True

        # проверяем диагонали
        if check_combination(1, 5, 9):
            return True

        if check_combination(3, 5, 7):
            return True

        return False


if __name__ == "__main__":
    game = TicTacGame()
    game.start_game()
