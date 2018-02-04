import unittest
from fit_object import FitObject
from fit_board import FitBoard


class FitBoardTest(unittest.TestCase):

    def test_create_object(self):
        _object = FitBoard(5, 10)
        _expected_board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertListEqual(_expected_board, _object.board)

    def _test_matrix(self, _matrix, _expected_matrix):
        _line_index = 0
        for _line in _expected_matrix:
            self.assertListEqual(_line, _matrix[_line_index])
            _line_index += 1

    def test_add_object(self):
        _board_object = FitBoard(5, 10)
        _side_a = ((1, 0), (1, 0), (1, 1), (1, 0))
        _side_b = ((1, 0), (1, 1), (1, 1), (1, 0))
        _fit_object = FitObject(_side_a, _side_b)
        _board_object.add_object(_fit_object, 0, 0)
        _expected_board = [
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self._test_matrix(_board_object.board, _expected_board)

        _fit_object.switch_active_side()
        self.assertEqual('b', _fit_object.active_side_name)
        self.assertEqual(1, len(_board_object.objects_list))
        self.assertEqual(
            'a', _board_object.objects_list[0].fit_object.active_side_name)

    def test_can_object_be_placed(self):
        _board_object = FitBoard(5, 10)
        _side_a = ((1, 0), (1, 0), (1, 1), (1, 0))
        _side_b = ((1, 0), (1, 1), (1, 1), (1, 0))
        _fit_object = FitObject(_side_a, _side_b)
        _board_object.add_object(_fit_object, 0, 0)
        self.assertFalse(_board_object.can_object_be_placed(_fit_object, 0, 0))
        self.assertFalse(_board_object.can_object_be_placed(_fit_object, 1, 0))
        self.assertTrue(_board_object.can_object_be_placed(_fit_object, 2, 0))
        self.assertTrue(_board_object.can_object_be_placed(_fit_object, 3, 0))
        self.assertTrue(_board_object.can_object_be_placed(_fit_object, 4, 0))
        self.assertFalse(_board_object.can_object_be_placed(_fit_object, 9, 0))
        self.assertFalse(_board_object.can_object_be_placed(_fit_object, 0, 4))
        _side_a_2 = ((1, 1), (1, 1), (0, 1), (1, 1))
        _side_b_2 = ((1, 0), (1, 1), (1, 1), (1, 0))
        _fit_object_2 = FitObject(_side_a_2, _side_b_2)
        _board_object.add_object(_fit_object_2, 1, 0)
        _expected_board = [
            [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self._test_matrix(_board_object.board, _expected_board)
        self.assertEqual(2, len(_board_object.objects_list))

        with self.assertRaises(Exception) as _ex:
            _board_object.add_object(_fit_object_2, 1, 0)

        self.assertEqual(
            _ex.exception.args[0], 'Object can\'t be placed on board with coordinates 1, 0')
        print(_board_object.objects_list)
