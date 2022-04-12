"""
Юнит тесты
"""

import unittest
from tictactoe import TicTacGame

class MyTestCase(unittest.TestCase):
    """ Класс для юнит тестов"""
    def test_validate_input_true_1_to_9(self):
        """Тест на правильность ввода. Правильный ввод от 1 до 9"""
        game = TicTacGame()
        result = game.validate_input("1")
        self.assertTrue(result, True)
        result = game.validate_input("2")
        self.assertTrue(result, True)
        result = game.validate_input("3")
        self.assertTrue(result, True)
        result = game.validate_input("4")
        self.assertTrue(result, True)
        result = game.validate_input("5")
        self.assertTrue(result, True)
        result = game.validate_input("6")
        self.assertTrue(result, True)
        result = game.validate_input("7")
        self.assertTrue(result, True)
        result = game.validate_input("8")
        self.assertTrue(result, True)
        result = game.validate_input("9")
        self.assertTrue(result, True)

    def test_validate_input_false(self):
        """Тест на правильность ввода. Недопустимые значения"""
        game = TicTacGame()
        """Ввели недопустимое значение ячейки"""
        result = game.validate_input("123")
        self.assertFalse(result, False)
        """Ввели недопустимое значение ячейки"""
        result = game.validate_input("asd31")
        self.assertFalse(result, False)
        """Ввели недопустимое значение ячейки"""
        result = game.validate_input("-12")
        self.assertFalse(result, False)
        """Ячейка уже занята"""
        game.x_and_o_position[4] = "X"
        result = game.validate_input("4")
        self.assertFalse(result, False)
        """Ввели краевый случай"""
        result = game.validate_input("0")
        self.assertFalse(result, False)
        """Ввели краевый случай"""
        result = game.validate_input("10")
        self.assertFalse(result, False)

    def test_check_draw_true(self):
        """Тест на ничью"""
        game = TicTacGame()
        game.x_and_o_position[1] = "X"
        game.x_and_o_position[2] = "O"
        game.x_and_o_position[3] = "O"
        game.x_and_o_position[4] = "O"
        game.x_and_o_position[5] = "X"
        game.x_and_o_position[6] = "X"
        game.x_and_o_position[7] = "X"
        game.x_and_o_position[8] = "X"
        game.x_and_o_position[9] = "O"
        result = game.check_draw()
        self.assertTrue(result, True)

    def test_check_draw_false(self):
        """Тест на ничью"""
        game = TicTacGame()
        game.x_and_o_position[1] = "X"
        game.x_and_o_position[3] = "O"
        game.x_and_o_position[2] = "X"
        game.x_and_o_position[4] = "O"
        result = game.check_draw()
        self.assertFalse(result, False)

    def test_check_winner_diagonal_true1(self):
        """Тест на победу по главной диагонали"""
        game = TicTacGame()
        game.x_and_o_position[1] = "X"
        game.x_and_o_position[4] = "O"
        game.x_and_o_position[5] = "X"
        game.x_and_o_position[2] = "O"
        game.x_and_o_position[9] = "X"
        result = game.check_winner(1)
        self.assertTrue(result, True)
        """Тест на победу по побочной горизонтали"""
        game.clear_board()
        game.x_and_o_position[3] = "X"
        game.x_and_o_position[4] = "O"
        game.x_and_o_position[5] = "X"
        game.x_and_o_position[1] = "O"
        game.x_and_o_position[7] = "X"
        result = game.check_winner(1)
        self.assertTrue(result, True)

    def test_check_winner_diagonal_true2(self):
        """Тест на победу по главной диагонали"""
        game = TicTacGame()
        game.x_and_o_position[1] = "O"
        game.x_and_o_position[4] = "X"
        game.x_and_o_position[5] = "O"
        game.x_and_o_position[2] = "X"
        game.x_and_o_position[9] = "O"
        result = game.check_winner(2)
        self.assertTrue(result, True)
        """Тест на победу по побочной горизонтали"""
        game.clear_board()
        game.x_and_o_position[3] = "O"
        game.x_and_o_position[4] = "X"
        game.x_and_o_position[5] = "O"
        game.x_and_o_position[1] = "X"
        game.x_and_o_position[7] = "O"
        result = game.check_winner(2)
        self.assertTrue(result, True)

    def test_check_winner_diagonal_False1(self):
        """Тест на победу по главной диагонали"""
        game = TicTacGame()
        game.x_and_o_position[1] = "X"
        game.x_and_o_position[4] = "O"
        game.x_and_o_position[5] = "X"
        game.x_and_o_position[2] = "O"
        result = game.check_winner(1)
        self.assertFalse(result, False)
        """Тест на победу по побочной горизонтали"""
        game.clear_board()
        game.x_and_o_position[3] = "X"
        game.x_and_o_position[4] = "O"
        game.x_and_o_position[5] = "X"
        game.x_and_o_position[1] = "O"
        result = game.check_winner(1)
        self.assertFalse(result, False)

    def test_check_winner_diagonal_false2(self):
        """Тест на победу по главной диагонали"""
        game = TicTacGame()
        game.x_and_o_position[1] = "O"
        game.x_and_o_position[4] = "X"
        game.x_and_o_position[5] = "O"
        game.x_and_o_position[2] = "X"
        result = game.check_winner(2)
        self.assertFalse(result, False)
        """Тест на победу по побочной горизонтали"""
        game.clear_board()
        game.x_and_o_position[3] = "O"
        game.x_and_o_position[4] = "X"
        game.x_and_o_position[5] = "O"
        game.x_and_o_position[1] = "X"
        result = game.check_winner(2)
        self.assertFalse(result, False)

    def test_check_winner_true2(self):
        """Тест на победу по вертикали"""
        game = TicTacGame()
        game.x_and_o_position[1] = "X"
        game.x_and_o_position[2] = "O"
        game.x_and_o_position[4] = "X"
        game.x_and_o_position[5] = "O"
        game.x_and_o_position[7] = "X"
        result = game.check_winner(1)
        self.assertTrue(result, True)
        """Тест на победу по вертикали"""
        game.clear_board()
        game.x_and_o_position[2] = "X"
        game.x_and_o_position[1] = "O"
        game.x_and_o_position[5] = "X"
        game.x_and_o_position[4] = "O"
        game.x_and_o_position[8] = "X"
        result = game.check_winner(1)
        self.assertTrue(result, True)
        """Тест на победу по вертикали"""
        game.clear_board()
        game.x_and_o_position[3] = "X"
        game.x_and_o_position[2] = "O"
        game.x_and_o_position[6] = "X"
        game.x_and_o_position[5] = "O"
        game.x_and_o_position[9] = "X"
        result = game.check_winner(1)
        self.assertTrue(result, True)
        """Тест на победу по вертикали"""
        game.clear_board()
        game.x_and_o_position[1] = "O"
        game.x_and_o_position[2] = "X"
        game.x_and_o_position[4] = "O"
        game.x_and_o_position[5] = "X"
        game.x_and_o_position[7] = "O"
        result = game.check_winner(2)
        self.assertTrue(result, True)
        """Тест на победу по вертикали"""
        game.clear_board()
        game.x_and_o_position[2] = "O"
        game.x_and_o_position[1] = "X"
        game.x_and_o_position[5] = "O"
        game.x_and_o_position[4] = "X"
        game.x_and_o_position[8] = "O"
        result = game.check_winner(2)
        self.assertTrue(result, True)
        """Тест на победу по вертикали"""
        game.clear_board()
        game.x_and_o_position[3] = "O"
        game.x_and_o_position[2] = "X"
        game.x_and_o_position[6] = "O"
        game.x_and_o_position[5] = "X"
        game.x_and_o_position[9] = "O"
        result = game.check_winner(2)
        self.assertTrue(result, True)
        """Тест на победу по вертикали"""
        game.clear_board()
        game.x_and_o_position[1] = "X"
        game.x_and_o_position[2] = "O"
        game.x_and_o_position[4] = "X"
        game.x_and_o_position[5] = "O"
        result = game.check_winner(1)
        self.assertFalse(result, False)
        """Тест на победу по вертикали"""
        game.clear_board()
        game.x_and_o_position[2] = "X"
        game.x_and_o_position[1] = "O"
        game.x_and_o_position[5] = "X"
        game.x_and_o_position[4] = "O"
        result = game.check_winner(1)
        self.assertFalse(result, False)
        """Тест на победу по вертикали"""
        game.clear_board()
        game.x_and_o_position[3] = "X"
        game.x_and_o_position[2] = "O"
        game.x_and_o_position[6] = "X"
        game.x_and_o_position[5] = "O"
        result = game.check_winner(1)
        self.assertFalse(result, False)
        """Тест на победу по вертикали"""
        game.clear_board()
        game.x_and_o_position[1] = "O"
        game.x_and_o_position[2] = "X"
        game.x_and_o_position[4] = "O"
        game.x_and_o_position[5] = "X"
        result = game.check_winner(2)
        self.assertFalse(result, False)
        """Тест на победу по вертикали"""
        game.clear_board()
        game.x_and_o_position[2] = "O"
        game.x_and_o_position[1] = "X"
        game.x_and_o_position[5] = "O"
        game.x_and_o_position[4] = "X"
        result = game.check_winner(2)
        self.assertFalse(result, False)
        """Тест на победу по вертикали"""
        game.clear_board()
        game.x_and_o_position[3] = "O"
        game.x_and_o_position[2] = "X"
        game.x_and_o_position[6] = "O"
        game.x_and_o_position[5] = "X"
        result = game.check_winner(2)
        self.assertFalse(result, False)

        def test_check_winner_true3(self):
            """Тест на победу по горизонтали"""
            game = TicTacGame()
            game.x_and_o_position[1] = "X"
            game.x_and_o_position[4] = "O"
            game.x_and_o_position[2] = "X"
            game.x_and_o_position[5] = "O"
            game.x_and_o_position[3] = "X"
            result = game.check_winner(1)
            self.assertTrue(result, True)
            """Тест на победу по горизонтали"""
            game.clear_board()
            game.x_and_o_position[4] = "X"
            game.x_and_o_position[2] = "O"
            game.x_and_o_position[5] = "X"
            game.x_and_o_position[1] = "O"
            game.x_and_o_position[6] = "X"
            result = game.check_winner(1)
            self.assertTrue(result, True)
            """Тест на победу по горизонтали"""
            game.clear_board()
            game.x_and_o_position[7] = "X"
            game.x_and_o_position[2] = "O"
            game.x_and_o_position[8] = "X"
            game.x_and_o_position[1] = "O"
            game.x_and_o_position[9] = "X"
            result = game.check_winner(1)
            self.assertTrue(result, True)
            """Тест на победу по горизонтали"""
            game.clear_board()
            game.x_and_o_position[1] = "O"
            game.x_and_o_position[4] = "X"
            game.x_and_o_position[2] = "O"
            game.x_and_o_position[5] = "X"
            game.x_and_o_position[3] = "O"
            result = game.check_winner(2)
            self.assertTrue(result, True)
            """Тест на победу по горизонтали"""
            game.clear_board()
            game.x_and_o_position[4] = "O"
            game.x_and_o_position[2] = "X"
            game.x_and_o_position[5] = "O"
            game.x_and_o_position[1] = "X"
            game.x_and_o_position[6] = "O"
            result = game.check_winner(2)
            self.assertTrue(result, True)
            """Тест на победу по горизонтали"""
            game.clear_board()
            game.x_and_o_position[7] = "O"
            game.x_and_o_position[2] = "X"
            game.x_and_o_position[8] = "O"
            game.x_and_o_position[5] = "X"
            game.x_and_o_position[9] = "O"
            result = game.check_winner(2)
            self.assertTrue(result, True)
            """Тест на победу по горизонтали"""
            game.clear_board()
            game.x_and_o_position[1] = "X"
            game.x_and_o_position[4] = "O"
            game.x_and_o_position[2] = "X"
            game.x_and_o_position[5] = "O"
            result = game.check_winner(1)
            self.assertFalse(result, False)
            """Тест на победу по горизонтали"""
            game.clear_board()
            game.x_and_o_position[4] = "X"
            game.x_and_o_position[1] = "O"
            game.x_and_o_position[5] = "X"
            game.x_and_o_position[2] = "O"
            result = game.check_winner(1)
            self.assertFalse(result, False)
            """Тест на победу по горизонтали"""
            game.clear_board()
            game.x_and_o_position[7] = "X"
            game.x_and_o_position[2] = "O"
            game.x_and_o_position[8] = "X"
            game.x_and_o_position[5] = "O"
            result = game.check_winner(1)
            self.assertFalse(result, False)
            """Тест на победу по горизонтали"""
            game.clear_board()
            game.x_and_o_position[1] = "O"
            game.x_and_o_position[4] = "X"
            game.x_and_o_position[2] = "O"
            game.x_and_o_position[5] = "X"
            result = game.check_winner(2)
            self.assertFalse(result, False)
            """Тест на победу по горизонтали"""
            game.clear_board()
            game.x_and_o_position[4] = "O"
            game.x_and_o_position[1] = "X"
            game.x_and_o_position[5] = "O"
            game.x_and_o_position[7] = "X"
            result = game.check_winner(2)
            self.assertFalse(result, False)
            """Тест на победу по горизонтали"""
            game.clear_board()
            game.x_and_o_position[7] = "O"
            game.x_and_o_position[2] = "X"
            game.x_and_o_position[8] = "O"
            game.x_and_o_position[5] = "X"
            result = game.check_winner(2)
            self.assertFalse(result, False)


if __name__ == '__main__':
    unittest.main()
